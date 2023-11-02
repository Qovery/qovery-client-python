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
from qovery.model.helm_request_all_of import HelmRequestAllOf
from qovery.model.helm_request_all_of_source import HelmRequestAllOfSource
from qovery.model.helm_request_all_of_values_override import HelmRequestAllOfValuesOverride
globals()['HelmRequestAllOf'] = HelmRequestAllOf
globals()['HelmRequestAllOfSource'] = HelmRequestAllOfSource
globals()['HelmRequestAllOfValuesOverride'] = HelmRequestAllOfValuesOverride
from qovery.model.helm_request import HelmRequest


class TestHelmRequest(unittest.TestCase):
    """HelmRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHelmRequest(self):
        """Test HelmRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HelmRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()