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
from qovery.model.git_provider_enum import GitProviderEnum
from qovery.model.git_token_response_all_of import GitTokenResponseAllOf
globals()['Base'] = Base
globals()['GitProviderEnum'] = GitProviderEnum
globals()['GitTokenResponseAllOf'] = GitTokenResponseAllOf
from qovery.model.git_token_response import GitTokenResponse


class TestGitTokenResponse(unittest.TestCase):
    """GitTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGitTokenResponse(self):
        """Test GitTokenResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GitTokenResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()