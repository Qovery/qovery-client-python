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
from qovery.model.service_deployment_status_enum import ServiceDeploymentStatusEnum
from qovery.model.state_enum import StateEnum
globals()['ServiceDeploymentStatusEnum'] = ServiceDeploymentStatusEnum
globals()['StateEnum'] = StateEnum
from qovery.model.status import Status


class TestStatus(unittest.TestCase):
    """Status unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatus(self):
        """Test Status"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Status()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
