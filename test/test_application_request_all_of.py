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
from qovery.model.application_git_repository_request import ApplicationGitRepositoryRequest
from qovery.model.build_mode_enum import BuildModeEnum
from qovery.model.build_pack_language_enum import BuildPackLanguageEnum
from qovery.model.healthcheck import Healthcheck
from qovery.model.service_port_response_list import ServicePortResponseList
globals()['ApplicationGitRepositoryRequest'] = ApplicationGitRepositoryRequest
globals()['BuildModeEnum'] = BuildModeEnum
globals()['BuildPackLanguageEnum'] = BuildPackLanguageEnum
globals()['Healthcheck'] = Healthcheck
globals()['ServicePortResponseList'] = ServicePortResponseList
from qovery.model.application_request_all_of import ApplicationRequestAllOf


class TestApplicationRequestAllOf(unittest.TestCase):
    """ApplicationRequestAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationRequestAllOf(self):
        """Test ApplicationRequestAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationRequestAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
