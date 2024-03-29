# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qovery.api.git_repositories_api import GitRepositoriesApi  # noqa: E501


class TestGitRepositoriesApi(unittest.TestCase):
    """GitRepositoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GitRepositoriesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_bitbucket_repositories(self) -> None:
        """Test case for get_bitbucket_repositories

        Get bitbucket repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_bitbucket_repository_branches(self) -> None:
        """Test case for get_bitbucket_repository_branches

        Get bitbucket branches of the specified repository  # noqa: E501
        """
        pass

    def test_get_git_provider_account(self) -> None:
        """Test case for get_git_provider_account

        Get git provider accounts  # noqa: E501
        """
        pass

    def test_get_github_repositories(self) -> None:
        """Test case for get_github_repositories

        Get github repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_github_repository_branches(self) -> None:
        """Test case for get_github_repository_branches

        Get github branches of the specified repository  # noqa: E501
        """
        pass

    def test_get_gitlab_repositories(self) -> None:
        """Test case for get_gitlab_repositories

        Get gitlab repositories of the connected user  # noqa: E501
        """
        pass

    def test_get_gitlab_repository_branches(self) -> None:
        """Test case for get_gitlab_repository_branches

        Get gitlab branches of the specified repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
