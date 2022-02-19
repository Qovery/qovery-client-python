"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.logical_database_api import LogicalDatabaseApi  # noqa: E501


class TestLogicalDatabaseApi(unittest.TestCase):
    """LogicalDatabaseApi unit test stubs"""

    def setUp(self):
        self.api = LogicalDatabaseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logical_database_on_database(self):
        """Test case for create_logical_database_on_database

        Create a logical database on the database  # noqa: E501
        """
        pass

    def test_delete_logical_database(self):
        """Test case for delete_logical_database

        Delete a Logical database  # noqa: E501
        """
        pass

    def test_edit_logical_database(self):
        """Test case for edit_logical_database

        Edit a logical database  # noqa: E501
        """
        pass

    def test_edit_logical_database_credentials(self):
        """Test case for edit_logical_database_credentials

        Edit logical database credentials  # noqa: E501
        """
        pass

    def test_get_logical_database(self):
        """Test case for get_logical_database

        Get logical database by ID  # noqa: E501
        """
        pass

    def test_get_logical_database_credentials(self):
        """Test case for get_logical_database_credentials

        Get  credentials of the logical database  # noqa: E501
        """
        pass

    def test_list_logical_database_application(self):
        """Test case for list_logical_database_application

        List linked applications  # noqa: E501
        """
        pass

    def test_list_logical_database_database(self):
        """Test case for list_logical_database_database

        List logical databases of a database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
