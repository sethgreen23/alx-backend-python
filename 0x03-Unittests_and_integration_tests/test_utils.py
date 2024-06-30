#!/usr/bin/env python3
"""Test utils for github org client."""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


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
