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
from qovery.model.commit import Commit
from qovery.model.deployment_history_application_all_of import DeploymentHistoryApplicationAllOf
from qovery.model.state_enum import StateEnum
globals()['Base'] = Base
globals()['Commit'] = Commit
globals()['DeploymentHistoryApplicationAllOf'] = DeploymentHistoryApplicationAllOf
globals()['StateEnum'] = StateEnum
from qovery.model.deployment_history_application import DeploymentHistoryApplication


class TestDeploymentHistoryApplication(unittest.TestCase):
    """DeploymentHistoryApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryApplication(self):
        """Test DeploymentHistoryApplication"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryApplication()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()