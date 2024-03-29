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

from qovery.models.cluster_logs_error import ClusterLogsError  # noqa: E501

class TestClusterLogsError(unittest.TestCase):
    """ClusterLogsError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterLogsError:
        """Test ClusterLogsError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterLogsError`
        """
        model = ClusterLogsError()  # noqa: E501
        if include_optional:
            return ClusterLogsError(
                tag = 'CANNOT_UNINSTALL_HELM_CHART',
                user_log_message = 'Wasn't able to delete all objects type Cert-Manager',
                link = '',
                hint_message = '',
                event_details = qovery.models.cluster_logs_error_event_details.ClusterLogs_error_event_details(
                    provider_kind = 'aws', 
                    region = 'eu-west-3', 
                    transmitter = qovery.models.cluster_logs_error_event_details_transmitter.ClusterLogs_error_event_details_transmitter(
                        type = 'kubernetes', 
                        id = 'za6ecdf3f', 
                        name = 'cluster-name', ), ),
                underlying_error = qovery.models.cluster_logs_error_underlying_error.ClusterLogs_error_underlying_error(
                    message = '', )
            )
        else:
            return ClusterLogsError(
        )
        """

    def testClusterLogsError(self):
        """Test ClusterLogsError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
