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
from qovery.model.deployment_history_helm_response_all_of_repository import DeploymentHistoryHelmResponseAllOfRepository
from qovery.model.state_enum import StateEnum
globals()['Commit'] = Commit
globals()['DeploymentHistoryHelmResponseAllOfRepository'] = DeploymentHistoryHelmResponseAllOfRepository
globals()['StateEnum'] = StateEnum
from qovery.model.deployment_history_helm_response_all_of import DeploymentHistoryHelmResponseAllOf


class TestDeploymentHistoryHelmResponseAllOf(unittest.TestCase):
    """DeploymentHistoryHelmResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryHelmResponseAllOf(self):
        """Test DeploymentHistoryHelmResponseAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryHelmResponseAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
