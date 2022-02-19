"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.cloud_provider_api import CloudProviderApi  # noqa: E501


class TestCloudProviderApi(unittest.TestCase):
    """CloudProviderApi unit test stubs"""

    def setUp(self):
        self.api = CloudProviderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_aws_features(self):
        """Test case for list_aws_features

        List AWS features available  # noqa: E501
        """
        pass

    def test_list_aws_regions(self):
        """Test case for list_aws_regions

        List AWS regions  # noqa: E501
        """
        pass

    def test_list_cloud_provider(self):
        """Test case for list_cloud_provider

        List Cloud providers available  # noqa: E501
        """
        pass

    def test_list_do_features(self):
        """Test case for list_do_features

        List DO features available  # noqa: E501
        """
        pass

    def test_list_do_regions(self):
        """Test case for list_do_regions

        List DO regions  # noqa: E501
        """
        pass

    def test_list_scaleway_features(self):
        """Test case for list_scaleway_features

        List Scaleway features available  # noqa: E501
        """
        pass

    def test_list_scaleway_regions(self):
        """Test case for list_scaleway_regions

        List Scaleway regions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
