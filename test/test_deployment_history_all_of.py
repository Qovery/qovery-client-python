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
from qovery.model.commit import Commit
from qovery.model.deployment_history_status_enum import DeploymentHistoryStatusEnum
globals()['Commit'] = Commit
globals()['DeploymentHistoryStatusEnum'] = DeploymentHistoryStatusEnum
from qovery.model.deployment_history_all_of import DeploymentHistoryAllOf


class TestDeploymentHistoryAllOf(unittest.TestCase):
    """DeploymentHistoryAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryAllOf(self):
        """Test DeploymentHistoryAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
