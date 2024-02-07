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

from qovery.models.cluster import Cluster

class TestCluster(unittest.TestCase):
    """Cluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Cluster:
        """Test Cluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Cluster`
        """
        model = Cluster()
        if include_optional:
            return Cluster(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = qovery.models.reference_object.ReferenceObject(
                    id = '', ),
                name = '',
                description = '',
                region = '',
                cloud_provider = 'AWS',
                min_running_nodes = 56,
                max_running_nodes = 56,
                disk_size = 50,
                instance_type = 'T3A_LARGE',
                kubernetes = 'MANAGED',
                cpu = 10000,
                memory = 4096,
                estimated_cloud_provider_cost = 56,
                status = 'BUILDING',
                has_access = True,
                version = '',
                is_default = True,
                production = True,
                ssh_keys = [
                    ''
                    ],
                features = [
                    qovery.models.cluster_feature.ClusterFeature(
                        id = '', 
                        title = '', 
                        description = '', 
                        cost_per_month_in_cents = 9900, 
                        cost_per_month = 99, 
                        currency_code = 'USD', 
                        value_type = 'BOOLEAN', 
                        value = null, 
                        is_value_updatable = True, 
                        accepted_values = [
                            null
                            ], )
                    ],
                deployment_status = 'NEVER_DEPLOYED'
            )
        else:
            return Cluster(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = qovery.models.reference_object.ReferenceObject(
                    id = '', ),
                name = '',
                region = '',
                cloud_provider = 'AWS',
        )
        """

    def testCluster(self):
        """Test Cluster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
