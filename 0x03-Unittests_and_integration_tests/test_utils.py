#!/usr/bin/env python3
"""Test utils for github org client."""
import unittest
import requests
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self,
                               nestd_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Test access nested map"""
        real_output = access_nested_map(nestd_map, path)
        self.assertEqual(real_output, expected)

    @parameterized.expand([
        ({}, ("a",), ),
        ({"a": 1}, ("a", "b"), ),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access nested map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: Dict,
                      mock_get: Any) -> None:
        """Test get json"""
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
