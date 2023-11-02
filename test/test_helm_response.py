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
from qovery.model.helm_request_all_of_source import HelmRequestAllOfSource
from qovery.model.helm_request_all_of_values_override import HelmRequestAllOfValuesOverride
from qovery.model.helm_response_all_of import HelmResponseAllOf
from qovery.model.reference_object import ReferenceObject
globals()['Base'] = Base
globals()['HelmRequestAllOfSource'] = HelmRequestAllOfSource
globals()['HelmRequestAllOfValuesOverride'] = HelmRequestAllOfValuesOverride
globals()['HelmResponseAllOf'] = HelmResponseAllOf
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.helm_response import HelmResponse


class TestHelmResponse(unittest.TestCase):
    """HelmResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHelmResponse(self):
        """Test HelmResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HelmResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()