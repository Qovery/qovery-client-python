"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.job_configuration_api import JobConfigurationApi  # noqa: E501


class TestJobConfigurationApi(unittest.TestCase):
    """JobConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = JobConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_edit_job_advanced_settings(self):
        """Test case for edit_job_advanced_settings

        Edit advanced settings  # noqa: E501
        """
        pass

    def test_get_job_advanced_settings(self):
        """Test case for get_job_advanced_settings

        Get advanced settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()