#!/usr/bin/env python3

"""
Test utilities for functions: access_nested_map, get_json, and memoize.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import memoize
from unittest.mock import Mock, patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test accessing values in a nested dictionary
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test accessing values in a nested dictionary.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test missing key raises KeyError.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Test get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test getting JSON data from a URL.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("utils.requests.get",
                   return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test memoize decorator function.
    """

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """
        Test the memoization of a method.
        """
        instance = self.TestClass()
        with patch.object(instance, 'a_method',
                          return_value=42) as mocked_method:
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
