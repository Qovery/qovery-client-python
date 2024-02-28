"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.organization_main_calls_api import OrganizationMainCallsApi  # noqa: E501


class TestOrganizationMainCallsApi(unittest.TestCase):
    """OrganizationMainCallsApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationMainCallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_git_token(self):
        """Test case for create_git_token

        Create a git token  # noqa: E501
        """
        pass

    def test_create_organization(self):
        """Test case for create_organization

        Create an organization  # noqa: E501
        """
        pass

    def test_delete_git_token(self):
        """Test case for delete_git_token

        Delete a git token  # noqa: E501
        """
        pass

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete an organization  # noqa: E501
        """
        pass

    def test_edit_git_token(self):
        """Test case for edit_git_token

        Edit a git token  # noqa: E501
        """
        pass

    def test_edit_organization(self):
        """Test case for edit_organization

        Edit an organization  # noqa: E501
        """
        pass

    def test_get_git_token_associated_services(self):
        """Test case for get_git_token_associated_services

        Get organization git token associated services  # noqa: E501
        """
        pass

    def test_get_organization(self):
        """Test case for get_organization

        Get organization by ID  # noqa: E501
        """
        pass

    def test_get_organization_git_token(self):
        """Test case for get_organization_git_token

        Get organization git token  # noqa: E501
        """
        pass

    def test_list_organization(self):
        """Test case for list_organization

        List user organizations  # noqa: E501
        """
        pass

    def test_list_organization_available_roles(self):
        """Test case for list_organization_available_roles

        List organization available roles  # noqa: E501
        """
        pass

    def test_list_organization_git_tokens(self):
        """Test case for list_organization_git_tokens

        List organization git tokens  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
