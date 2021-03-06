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
from qovery.model.deployment_history_application import DeploymentHistoryApplication
from qovery.model.deployment_history_database import DeploymentHistoryDatabase
from qovery.model.state_enum import StateEnum
globals()['DeploymentHistoryApplication'] = DeploymentHistoryApplication
globals()['DeploymentHistoryDatabase'] = DeploymentHistoryDatabase
globals()['StateEnum'] = StateEnum
from qovery.model.deployment_history_environment_all_of import DeploymentHistoryEnvironmentAllOf


class TestDeploymentHistoryEnvironmentAllOf(unittest.TestCase):
    """DeploymentHistoryEnvironmentAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryEnvironmentAllOf(self):
        """Test DeploymentHistoryEnvironmentAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryEnvironmentAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
