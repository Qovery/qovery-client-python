"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.database_event_api import DatabaseEventApi  # noqa: E501


class TestDatabaseEventApi(unittest.TestCase):
    """DatabaseEventApi unit test stubs"""

    def setUp(self):
        self.api = DatabaseEventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_database_event(self):
        """Test case for list_database_event

        List database  events  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
