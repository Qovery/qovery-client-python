"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.github_app_api import GithubAppApi  # noqa: E501


class TestGithubAppApi(unittest.TestCase):
    """GithubAppApi unit test stubs"""

    def setUp(self):
        self.api = GithubAppApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organization_github_app_connect(self):
        """Test case for organization_github_app_connect

        Connect a github account to an organization  # noqa: E501
        """
        pass

    def test_organization_github_app_disconnect(self):
        """Test case for organization_github_app_disconnect

        Disconnect a github account from an organization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
