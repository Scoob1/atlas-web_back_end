#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ("simple_key", {"a": 1}, ("a",), 1),
        ("nested_key", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deep_nested_key", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("missing_key", {}, ("a",)),
        ("nested_missing_key", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, name, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("example", "http://example.com", {"payload": True}),
        ("holberton", "http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, name, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        with patch("utils.requests.get", return_value=mock_response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        instance = self.TestClass()
        with patch.object(instance, 'a_method', return_value=42) as mocked_method:
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mocked_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
