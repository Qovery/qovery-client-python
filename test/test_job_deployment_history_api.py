"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.job_deployment_history_api import JobDeploymentHistoryApi  # noqa: E501


class TestJobDeploymentHistoryApi(unittest.TestCase):
    """JobDeploymentHistoryApi unit test stubs"""

    def setUp(self):
        self.api = JobDeploymentHistoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_job_deployment_history(self):
        """Test case for list_job_deployment_history

        List job deployments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()