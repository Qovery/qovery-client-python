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

from qovery.models.secret import Secret

class TestSecret(unittest.TestCase):
    """Secret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Secret:
        """Test Secret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Secret`
        """
        model = Secret()
        if include_optional:
            return Secret(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key = '',
                overridden_secret = qovery.models.secret_override.SecretOverride(
                    id = '', 
                    key = '', 
                    mount_path = '', 
                    scope = 'APPLICATION', 
                    variable_type = 'VALUE', ),
                aliased_secret = qovery.models.secret_alias.SecretAlias(
                    id = '', 
                    key = 'QOVERY_DATABASE_PSQL_NAME', 
                    mount_path = '', 
                    scope = 'APPLICATION', 
                    variable_type = 'VALUE', ),
                scope = 'APPLICATION',
                variable_type = 'VALUE',
                service_id = '',
                service_name = '',
                service_type = 'APPLICATION',
                owned_by = ''
            )
        else:
            return Secret(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key = '',
                scope = 'APPLICATION',
        )
        """

    def testSecret(self):
        """Test Secret"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
