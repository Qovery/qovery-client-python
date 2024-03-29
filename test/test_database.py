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

from qovery.models.database import Database  # noqa: E501

class TestDatabase(unittest.TestCase):
    """Database unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Database:
        """Test Database
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Database`
        """
        model = Database()  # noqa: E501
        if include_optional:
            return Database(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                description = '',
                type = 'MONGODB',
                version = '10.1',
                mode = 'CONTAINER',
                accessibility = 'PRIVATE',
                cpu = 1250,
                instance_type = 'db.t3.medium',
                memory = 1024,
                storage = 56,
                environment = qovery.models.reference_object.ReferenceObject(
                    id = '', ),
                host = '',
                port = 5432,
                maximum_cpu = 1250,
                maximum_memory = 1024,
                disk_encrypted = True
            )
        else:
            return Database(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                type = 'MONGODB',
                version = '10.1',
                mode = 'CONTAINER',
                environment = qovery.models.reference_object.ReferenceObject(
                    id = '', ),
        )
        """

    def testDatabase(self):
        """Test Database"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
