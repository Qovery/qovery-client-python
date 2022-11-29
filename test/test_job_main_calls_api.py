"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.job_main_calls_api import JobMainCallsApi  # noqa: E501


class TestJobMainCallsApi(unittest.TestCase):
    """JobMainCallsApi unit test stubs"""

    def setUp(self):
        self.api = JobMainCallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_job(self):
        """Test case for delete_job

        Delete job  # noqa: E501
        """
        pass

    def test_edit_job(self):
        """Test case for edit_job

        Edit job  # noqa: E501
        """
        pass

    def test_get_job(self):
        """Test case for get_job

        Get job by ID  # noqa: E501
        """
        pass

    def test_get_job_status(self):
        """Test case for get_job_status

        Get job status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()