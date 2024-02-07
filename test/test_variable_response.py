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

from qovery.models.variable_response import VariableResponse

class TestVariableResponse(unittest.TestCase):
    """VariableResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableResponse:
        """Test VariableResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableResponse`
        """
        model = VariableResponse()
        if include_optional:
            return VariableResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key = '',
                value = '',
                mount_path = '',
                overridden_variable = qovery.models.variable_override.VariableOverride(
                    id = '', 
                    key = '', 
                    value = '', 
                    mount_path = '', 
                    scope = 'APPLICATION', 
                    variable_type = 'VALUE', ),
                aliased_variable = qovery.models.variable_alias.VariableAlias(
                    id = '', 
                    key = 'DATABASE_PSQL_NAME', 
                    value = '', 
                    mount_path = '', 
                    scope = 'APPLICATION', 
                    variable_type = 'VALUE', ),
                scope = 'APPLICATION',
                variable_type = 'VALUE',
                service_id = '',
                service_name = '',
                service_type = 'APPLICATION',
                owned_by = '',
                is_secret = True
            )
        else:
            return VariableResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key = '',
                value = '',
                scope = 'APPLICATION',
                is_secret = True,
        )
        """

    def testVariableResponse(self):
        """Test VariableResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
