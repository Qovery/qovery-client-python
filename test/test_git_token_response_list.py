# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qovery.models.git_token_response_list import GitTokenResponseList

class TestGitTokenResponseList(unittest.TestCase):
    """GitTokenResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitTokenResponseList:
        """Test GitTokenResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitTokenResponseList`
        """
        model = GitTokenResponseList()
        if include_optional:
            return GitTokenResponseList(
                results = [
                    null
                    ]
            )
        else:
            return GitTokenResponseList(
        )
        """

    def testGitTokenResponseList(self):
        """Test GitTokenResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
