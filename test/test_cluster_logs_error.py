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
from qovery.model.cluster_logs_error_event_details import ClusterLogsErrorEventDetails
from qovery.model.cluster_logs_error_underlying_error import ClusterLogsErrorUnderlyingError
globals()['ClusterLogsErrorEventDetails'] = ClusterLogsErrorEventDetails
globals()['ClusterLogsErrorUnderlyingError'] = ClusterLogsErrorUnderlyingError
from qovery.model.cluster_logs_error import ClusterLogsError


class TestClusterLogsError(unittest.TestCase):
    """ClusterLogsError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterLogsError(self):
        """Test ClusterLogsError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterLogsError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
