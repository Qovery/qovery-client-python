"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.jobs_api import JobsApi  # noqa: E501


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_job(self):
        """Test case for create_job

        Create a job  # noqa: E501
        """
        pass

    def test_get_environment_job_status(self):
        """Test case for get_environment_job_status

        List all environment job statuses  # noqa: E501
        """
        pass

    def test_list_jobs(self):
        """Test case for list_jobs

        List jobs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()