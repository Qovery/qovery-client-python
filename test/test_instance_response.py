"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.environment_databases_current_metric_response_cpu import EnvironmentDatabasesCurrentMetricResponseCpu
from qovery.model.environment_databases_current_metric_response_memory import EnvironmentDatabasesCurrentMetricResponseMemory
globals()['EnvironmentDatabasesCurrentMetricResponseCpu'] = EnvironmentDatabasesCurrentMetricResponseCpu
globals()['EnvironmentDatabasesCurrentMetricResponseMemory'] = EnvironmentDatabasesCurrentMetricResponseMemory
from qovery.model.instance_response import InstanceResponse


class TestInstanceResponse(unittest.TestCase):
    """InstanceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstanceResponse(self):
        """Test InstanceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InstanceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
