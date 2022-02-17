"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.git_repositories_api import GitRepositoriesApi  # noqa: E501


class TestGitRepositoriesApi(unittest.TestCase):
    """GitRepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = GitRepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_bitbucket_repositories(self):
        """Test case for get_bitbucket_repositories

        Get bitbucket repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_bitbucket_repository_branches(self):
        """Test case for get_bitbucket_repository_branches

        Get bitbucket branches of the specified repository  # noqa: E501
        """
        pass

    def test_get_git_provider_account(self):
        """Test case for get_git_provider_account

        Get git provider accounts  # noqa: E501
        """
        pass

    def test_get_github_repositories(self):
        """Test case for get_github_repositories

        Get github repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_github_repository_branches(self):
        """Test case for get_github_repository_branches

        Get github branches of the specified repository  # noqa: E501
        """
        pass

    def test_get_gitlab_repositories(self):
        """Test case for get_gitlab_repositories

        Get gitlab repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_gitlab_repository_branches(self):
        """Test case for get_gitlab_repository_branches

        Get gitlab branches of the specified repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
