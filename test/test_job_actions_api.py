"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.job_actions_api import JobActionsApi  # noqa: E501


class TestJobActionsApi(unittest.TestCase):
    """JobActionsApi unit test stubs"""

    def setUp(self):
        self.api = JobActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deploy_job(self):
        """Test case for deploy_job

        Deploy job  # noqa: E501
        """
        pass

    def test_restart_job(self):
        """Test case for restart_job

        Deprecated - Restart job  # noqa: E501
        """
        pass

    def test_stop_job(self):
        """Test case for stop_job

        Stop job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
