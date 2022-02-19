"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.members_api import MembersApi  # noqa: E501


class TestMembersApi(unittest.TestCase):
    """MembersApi unit test stubs"""

    def setUp(self):
        self.api = MembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_invite_member(self):
        """Test case for delete_invite_member

        Remove an invited member  # noqa: E501
        """
        pass

    def test_delete_member(self):
        """Test case for delete_member

        Remove a member  # noqa: E501
        """
        pass

    def test_get_organization_invited_members(self):
        """Test case for get_organization_invited_members

        Get invited members  # noqa: E501
        """
        pass

    def test_get_organization_members(self):
        """Test case for get_organization_members

        Get organization members  # noqa: E501
        """
        pass

    def test_post_accept_invite_member(self):
        """Test case for post_accept_invite_member

        Accept Invite in the organization  # noqa: E501
        """
        pass

    def test_post_invite_member(self):
        """Test case for post_invite_member

        Invite someone in the organization  # noqa: E501
        """
        pass

    def test_post_organization_transfer_ownership(self):
        """Test case for post_organization_transfer_ownership

        Transfer organization ownership to another user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
