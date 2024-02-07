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

from qovery.models.list_database_deployment_history200_response import ListDatabaseDeploymentHistory200Response

class TestListDatabaseDeploymentHistory200Response(unittest.TestCase):
    """ListDatabaseDeploymentHistory200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDatabaseDeploymentHistory200Response:
        """Test ListDatabaseDeploymentHistory200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDatabaseDeploymentHistory200Response`
        """
        model = ListDatabaseDeploymentHistory200Response()
        if include_optional:
            return ListDatabaseDeploymentHistory200Response(
                page = 1,
                page_size = 20,
                results = [
                    null
                    ]
            )
        else:
            return ListDatabaseDeploymentHistory200Response(
                page = 1,
                page_size = 20,
        )
        """

    def testListDatabaseDeploymentHistory200Response(self):
        """Test ListDatabaseDeploymentHistory200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
