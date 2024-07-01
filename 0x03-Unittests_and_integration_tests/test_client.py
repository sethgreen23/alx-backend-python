#!/usr/bin/env python3
"""Test client for github org client."""
import unittest
import requests
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from utils import (access_nested_map,
                   get_json,
                   memoize)
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test github org client."""
    @parameterized.expand([
		("google", {'google': True}),
		("abc", {'abc': True}),
	])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: dict, mocked_get_json: Any) -> None:
        """Test org"""
        mocked_get_json.return_value = expected
        client_object = GithubOrgClient(org_name)
        self.assertEqual(client_object.org, expected)
        mocked_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))
