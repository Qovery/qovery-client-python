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
from qovery.model.commit_response import CommitResponse
from qovery.model.deployment_history_response_all_of import DeploymentHistoryResponseAllOf
globals()['BaseResponse'] = BaseResponse
globals()['CommitResponse'] = CommitResponse
globals()['DeploymentHistoryResponseAllOf'] = DeploymentHistoryResponseAllOf
from qovery.model.deployment_history_response import DeploymentHistoryResponse


class TestDeploymentHistoryResponse(unittest.TestCase):
    """DeploymentHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryResponse(self):
        """Test DeploymentHistoryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
