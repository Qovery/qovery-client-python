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
import datetime

from qovery.models.cluster_cloud_provider_info import ClusterCloudProviderInfo  # noqa: E501

class TestClusterCloudProviderInfo(unittest.TestCase):
    """ClusterCloudProviderInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterCloudProviderInfo:
        """Test ClusterCloudProviderInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterCloudProviderInfo`
        """
        model = ClusterCloudProviderInfo()  # noqa: E501
        if include_optional:
            return ClusterCloudProviderInfo(
                cloud_provider = 'AWS',
                credentials = qovery.models.cluster_cloud_provider_info_credentials.ClusterCloudProviderInfo_credentials(
                    id = '', 
                    name = '', ),
                region = ''
            )
        else:
            return ClusterCloudProviderInfo(
        )
        """

    def testClusterCloudProviderInfo(self):
        """Test ClusterCloudProviderInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
