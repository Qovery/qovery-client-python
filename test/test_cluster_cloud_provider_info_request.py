"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.cloud_provider_enum import CloudProviderEnum
from qovery.model.cluster_cloud_provider_info_credentials import ClusterCloudProviderInfoCredentials
globals()['CloudProviderEnum'] = CloudProviderEnum
globals()['ClusterCloudProviderInfoCredentials'] = ClusterCloudProviderInfoCredentials
from qovery.model.cluster_cloud_provider_info_request import ClusterCloudProviderInfoRequest


class TestClusterCloudProviderInfoRequest(unittest.TestCase):
    """ClusterCloudProviderInfoRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterCloudProviderInfoRequest(self):
        """Test ClusterCloudProviderInfoRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterCloudProviderInfoRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
