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

from qovery.models.cluster_advanced_settings import ClusterAdvancedSettings  # noqa: E501

class TestClusterAdvancedSettings(unittest.TestCase):
    """ClusterAdvancedSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterAdvancedSettings:
        """Test ClusterAdvancedSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterAdvancedSettings`
        """
        model = ClusterAdvancedSettings()  # noqa: E501
        if include_optional:
            return ClusterAdvancedSettings(
                aws_cloudwatch_eks_logs_retention_days = 56,
                aws_vpc_enable_s3_flow_logs = True,
                aws_vpc_flow_logs_retention_days = 56,
                loki_log_retention_in_week = 56,
                registry_image_retention_time = 56,
                cloud_provider_container_registry_tags = {
                    'key' : ''
                    },
                load_balancer_size = '',
                database_postgresql_deny_public_access = True,
                database_postgresql_allowed_cidrs = [
                    ''
                    ],
                database_mysql_deny_public_access = True,
                database_mysql_allowed_cidrs = [
                    ''
                    ],
                database_mongodb_deny_public_access = True,
                database_mongodb_allowed_cidrs = [
                    ''
                    ],
                database_redis_deny_public_access = True,
                database_redis_allowed_cidrs = [
                    ''
                    ],
                aws_iam_admin_group = '',
                aws_eks_ec2_metadata_imds = 'optional',
                pleco_resources_ttl = 56,
                registry_mirroring_mode = 'SERVICE',
                nginx_vcpu_request_in_milli_cpu = 56,
                nginx_vcpu_limit_in_milli_cpu = 56,
                nginx_memory_request_in_mib = 56,
                nginx_memory_limit_in_mib = 56,
                nginx_hpa_cpu_utilization_percentage_threshold = 56,
                nginx_hpa_min_number_instances = 56,
                nginx_hpa_max_number_instances = 56
            )
        else:
            return ClusterAdvancedSettings(
        )
        """

    def testClusterAdvancedSettings(self):
        """Test ClusterAdvancedSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
