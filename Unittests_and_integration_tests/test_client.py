#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from utils import get_json


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
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
            }
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test_org/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        mock_payload = [
            {"name": "repo1", "full_name": "org/repo1"},
            {"name": "repo2", "full_name": "org/repo2"},
        ]
        mock_get_json.return_value = mock_payload
        mock_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
        client = GithubOrgClient("test_org")
        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("test_org")
        with patch.object(client,
                          'repos', new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = [repo]
            result = client.has_license(license_key)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
