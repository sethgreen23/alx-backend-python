#!/usr/bin/env python3

import os
import unittest
import requests
from functools import wraps
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map"""
    @parameterized.expand([
        ('depth1', {"a": 1}, ['a'], 1),
        ('depth2', {"a": {"b": 2}}, ['a'], {"b": 2}),
        ('depth2_with_2_paths', {"a": {"b": 2}}, ['a', 'b'], 2)
        ])
    def test_access_nested_map(self, name: str,
                               nestd_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Test access nested map"""
        self.assertEqual(access_nested_map(nestd_map, path), expected)


if __name__ == "__main__":
    unittest.main()
