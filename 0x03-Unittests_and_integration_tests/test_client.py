#!/usr/bin/env python3
"""Test client for github org client."""
import unittest
import requests
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any, Dict
from utils import (access_nested_map,
                   get_json,
                   memoize)
from unittest.mock import patch, PropertyMock, call, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test github org client."""
    @parameterized.expand([
        ("google", {'google': True}),
        ("abc", {'abc': True}),
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 expected: dict,
                 mocked_get_json: Any) -> None:
        """Test org"""
        mocked_get_json.return_value = expected
        client_object = GithubOrgClient(org_name)
        self.assertEqual(client_object.org, expected)
        mocked_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))

    def test_public_repos_url(self) -> None:
        """Test public repos url"""
        expected = 'www.google.com'
        payload = {'repos_url': expected}
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            client_object = GithubOrgClient(expected)
            mock_org.return_value = payload
            self.assertEqual(client_object._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any) -> None:
        """Test public repos"""
        seth = {'name': 'seth', 'license': {'key': 'mit'}}
        maria = {'name': 'maria', 'license': {'key': 'apache-2.0'}}
        cristopher = {'name': 'cristopher', 'license': {'key': 'mpl-2.0'}}
        mock_path = 'client.GithubOrgClient._public_repos_url'
        mock_get_json.return_value = [seth, maria, cristopher]
        with patch(mock_path) as mock_public_repos_url:
            client_object = GithubOrgClient('google')
            self.assertEqual(
                client_object.public_repos(),
                ['seth', 'maria', 'cristopher'])
            self.assertEqual(
                client_object.public_repos(license='mit'),
                ['seth'])
            self.assertEqual(
                client_object.public_repos(license='mpl-2.0'),
                ['cristopher'])
            self.assertEqual(
                client_object.public_repos(license='apache-2.0'),
                ['maria'])
            self.assertEqual(client_object.public_repos(45), [])
            self.assertEqual(client_object.public_repos('c'), [])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self,
                         repo: Dict[str, Dict],
                         license_key: str,
                         expected: bool) -> None:
        """Test has license"""
        self.assertEqual(
            GithubOrgClient.has_license(
                repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for github org client """

    @classmethod
    def setUpClass(cls):
        """ prepare for testing """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])
