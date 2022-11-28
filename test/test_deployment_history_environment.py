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
from qovery.model.base import Base
from qovery.model.deployment_history_application import DeploymentHistoryApplication
from qovery.model.deployment_history_container import DeploymentHistoryContainer
from qovery.model.deployment_history_database import DeploymentHistoryDatabase
from qovery.model.deployment_history_environment_all_of import DeploymentHistoryEnvironmentAllOf
from qovery.model.deployment_history_job_response import DeploymentHistoryJobResponse
from qovery.model.state_enum import StateEnum
globals()['Base'] = Base
globals()['DeploymentHistoryApplication'] = DeploymentHistoryApplication
globals()['DeploymentHistoryContainer'] = DeploymentHistoryContainer
globals()['DeploymentHistoryDatabase'] = DeploymentHistoryDatabase
globals()['DeploymentHistoryEnvironmentAllOf'] = DeploymentHistoryEnvironmentAllOf
globals()['DeploymentHistoryJobResponse'] = DeploymentHistoryJobResponse
globals()['StateEnum'] = StateEnum
from qovery.model.deployment_history_environment import DeploymentHistoryEnvironment


class TestDeploymentHistoryEnvironment(unittest.TestCase):
    """DeploymentHistoryEnvironment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryEnvironment(self):
        """Test DeploymentHistoryEnvironment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryEnvironment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
