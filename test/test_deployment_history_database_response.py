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
from qovery.model.base_response import BaseResponse
from qovery.model.deployment_history_database_response_all_of import DeploymentHistoryDatabaseResponseAllOf
from qovery.model.global_deployment_status import GlobalDeploymentStatus
globals()['BaseResponse'] = BaseResponse
globals()['DeploymentHistoryDatabaseResponseAllOf'] = DeploymentHistoryDatabaseResponseAllOf
globals()['GlobalDeploymentStatus'] = GlobalDeploymentStatus
from qovery.model.deployment_history_database_response import DeploymentHistoryDatabaseResponse


class TestDeploymentHistoryDatabaseResponse(unittest.TestCase):
    """DeploymentHistoryDatabaseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryDatabaseResponse(self):
        """Test DeploymentHistoryDatabaseResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryDatabaseResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
