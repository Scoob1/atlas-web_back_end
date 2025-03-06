#!/usr/bin/env python3

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from utils import get_json
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos},
    {"org_payload": org_payload, "repos_payload": apache2_repos, "expected_repos": ["repo1", "repo2"]},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Mock requests.get to return example payloads."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def mock_get(url):
            """Return different payloads based on the requested URL."""
            response = unittest.mock.Mock()
            if url == "https://api.github.com/orgs/test_org":
                response.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/test_org/repos":
                response.json.return_value = cls.repos_payload
            else:
                response.json.return_value = {}
            return response

        cls.mock_get.side_effect = mock_get

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method using mocked requests.get."""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)


if __name__ == "__main__":
    unittest.main()
