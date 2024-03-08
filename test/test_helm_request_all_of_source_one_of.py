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

from qovery.models.helm_request_all_of_source_one_of import HelmRequestAllOfSourceOneOf  # noqa: E501

class TestHelmRequestAllOfSourceOneOf(unittest.TestCase):
    """HelmRequestAllOfSourceOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HelmRequestAllOfSourceOneOf:
        """Test HelmRequestAllOfSourceOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HelmRequestAllOfSourceOneOf`
        """
        model = HelmRequestAllOfSourceOneOf()  # noqa: E501
        if include_optional:
            return HelmRequestAllOfSourceOneOf(
                git_repository = qovery.models.helm_git_repository_request.HelmGitRepositoryRequest(
                    url = 'https://github.com/Qovery/simple-node-app', 
                    branch = 'feat/text_xxx', 
                    root_path = '/', 
                    git_token_id = '', )
            )
        else:
            return HelmRequestAllOfSourceOneOf(
        )
        """

    def testHelmRequestAllOfSourceOneOf(self):
        """Test HelmRequestAllOfSourceOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()