"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.base_response import BaseResponse
from qovery.model.deployment_history_application_response import DeploymentHistoryApplicationResponse
from qovery.model.deployment_history_database_response import DeploymentHistoryDatabaseResponse
globals()['BaseResponse'] = BaseResponse
globals()['DeploymentHistoryApplicationResponse'] = DeploymentHistoryApplicationResponse
globals()['DeploymentHistoryDatabaseResponse'] = DeploymentHistoryDatabaseResponse
from qovery.model.deployment_history_environment_response import DeploymentHistoryEnvironmentResponse


class TestDeploymentHistoryEnvironmentResponse(unittest.TestCase):
    """DeploymentHistoryEnvironmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryEnvironmentResponse(self):
        """Test DeploymentHistoryEnvironmentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryEnvironmentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
