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
from qovery.model.helm_default_values_request_all_of import HelmDefaultValuesRequestAllOf
from qovery.model.helm_git_repository_request import HelmGitRepositoryRequest
globals()['HelmDefaultValuesRequestAllOf'] = HelmDefaultValuesRequestAllOf
globals()['HelmGitRepositoryRequest'] = HelmGitRepositoryRequest
from qovery.model.helm_default_values_request import HelmDefaultValuesRequest


class TestHelmDefaultValuesRequest(unittest.TestCase):
    """HelmDefaultValuesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHelmDefaultValuesRequest(self):
        """Test HelmDefaultValuesRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HelmDefaultValuesRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
