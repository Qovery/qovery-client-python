"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from api.database_metrics_api import DatabaseMetricsApi  # noqa: E501


class TestDatabaseMetricsApi(unittest.TestCase):
    """DatabaseMetricsApi unit test stubs"""

    def setUp(self):
        self.api = DatabaseMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_database_current_metric(self):
        """Test case for get_database_current_metric

        Get current metric consumption of the database   # noqa: E501
        """
        pass

    def test_get_database_metric_cpu(self):
        """Test case for get_database_metric_cpu

        Get CPU consumption metric over time for the database  # noqa: E501
        """
        pass

    def test_get_database_metric_health_check(self):
        """Test case for get_database_metric_health_check

        Get Health Check latency  metric over time for the database  # noqa: E501
        """
        pass

    def test_get_database_metric_memory(self):
        """Test case for get_database_metric_memory

        Get Memory consumption metric over time for the database  # noqa: E501
        """
        pass

    def test_get_database_metric_restart(self):
        """Test case for get_database_metric_restart

        List database restarts  # noqa: E501
        """
        pass

    def test_get_database_metric_storage(self):
        """Test case for get_database_metric_storage

        Get Storage consumption metric over time for the database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
