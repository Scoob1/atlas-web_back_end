#!/usr/bin/env python3

from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from utils import get_json
import unittest


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", "google"),
        ("abc", "abc"),
    ])
    @patch("client.get_json")
    def test_org(self, name, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test_org/repos")

    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url):
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos, "https://api.github.com/orgs/test_org/repos")

if __name__ == "__main__":
    unittest.main()
