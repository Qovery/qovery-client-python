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
from qovery.model.deployment_stage_response_all_of import DeploymentStageResponseAllOf
from qovery.model.deployment_stage_service_response_list import DeploymentStageServiceResponseList
from qovery.model.reference_object import ReferenceObject
globals()['Base'] = Base
globals()['DeploymentStageResponseAllOf'] = DeploymentStageResponseAllOf
globals()['DeploymentStageServiceResponseList'] = DeploymentStageServiceResponseList
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.deployment_stage_response import DeploymentStageResponse


class TestDeploymentStageResponse(unittest.TestCase):
    """DeploymentStageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentStageResponse(self):
        """Test DeploymentStageResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentStageResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()