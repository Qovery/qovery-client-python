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
from qovery.model.git_provider_enum import GitProviderEnum
globals()['GitProviderEnum'] = GitProviderEnum
from qovery.model.git_token_request import GitTokenRequest


class TestGitTokenRequest(unittest.TestCase):
    """GitTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGitTokenRequest(self):
        """Test GitTokenRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GitTokenRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()