"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.cloud_provider_credentials_api import CloudProviderCredentialsApi  # noqa: E501


class TestCloudProviderCredentialsApi(unittest.TestCase):
    """CloudProviderCredentialsApi unit test stubs"""

    def setUp(self):
        self.api = CloudProviderCredentialsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_aws_credentials(self):
        """Test case for create_aws_credentials

        Create AWS credentials set  # noqa: E501
        """
        pass

    def test_create_do_credentials(self):
        """Test case for create_do_credentials

        Create Digital Ocean credentials set  # noqa: E501
        """
        pass

    def test_create_scaleway_credentials(self):
        """Test case for create_scaleway_credentials

        Create Scaleway credentials set  # noqa: E501
        """
        pass

    def test_delete_aws_credentials(self):
        """Test case for delete_aws_credentials

        Delete a set of AWS credentials  # noqa: E501
        """
        pass

    def test_delete_do_credentials(self):
        """Test case for delete_do_credentials

        Delete a set of Digital Ocean credentials  # noqa: E501
        """
        pass

    def test_delete_scaleway_credentials(self):
        """Test case for delete_scaleway_credentials

        Delete a set of Scaleway credentials  # noqa: E501
        """
        pass

    def test_edit_aws_credentials(self):
        """Test case for edit_aws_credentials

        Edit a set of AWS credentials  # noqa: E501
        """
        pass

    def test_edit_do_credentials(self):
        """Test case for edit_do_credentials

        Edit a set of Digital Ocean credentials  # noqa: E501
        """
        pass

    def test_edit_scaleway_credentials(self):
        """Test case for edit_scaleway_credentials

        Edit a set of Scaleway credentials  # noqa: E501
        """
        pass

    def test_list_aws_credentials(self):
        """Test case for list_aws_credentials

        List AWS credentials  # noqa: E501
        """
        pass

    def test_list_do_credentials(self):
        """Test case for list_do_credentials

        List DO credentials  # noqa: E501
        """
        pass

    def test_list_scaleway_credentials(self):
        """Test case for list_scaleway_credentials

        List Scaleway credentials  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
