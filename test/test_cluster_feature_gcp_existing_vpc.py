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

from qovery.models.cluster_feature_gcp_existing_vpc import ClusterFeatureGcpExistingVpc  # noqa: E501

class TestClusterFeatureGcpExistingVpc(unittest.TestCase):
    """ClusterFeatureGcpExistingVpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterFeatureGcpExistingVpc:
        """Test ClusterFeatureGcpExistingVpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterFeatureGcpExistingVpc`
        """
        model = ClusterFeatureGcpExistingVpc()  # noqa: E501
        if include_optional:
            return ClusterFeatureGcpExistingVpc(
                vpc_name = '',
                vpc_project_id = '',
                subnetwork_name = '',
                ip_range_services_name = '',
                ip_range_pods_name = '',
                additional_ip_range_pods_names = [
                    ''
                    ]
            )
        else:
            return ClusterFeatureGcpExistingVpc(
                vpc_name = '',
        )
        """

    def testClusterFeatureGcpExistingVpc(self):
        """Test ClusterFeatureGcpExistingVpc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
