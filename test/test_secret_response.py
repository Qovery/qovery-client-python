"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.aliased_secret import AliasedSecret
from qovery.model.base_response import BaseResponse
from qovery.model.overridden_secret import OverriddenSecret
globals()['AliasedSecret'] = AliasedSecret
globals()['BaseResponse'] = BaseResponse
globals()['OverriddenSecret'] = OverriddenSecret
from qovery.model.secret_response import SecretResponse


class TestSecretResponse(unittest.TestCase):
    """SecretResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretResponse(self):
        """Test SecretResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
