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

from qovery.api.job_deployment_history_api import JobDeploymentHistoryApi


class TestJobDeploymentHistoryApi(unittest.TestCase):
    """JobDeploymentHistoryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobDeploymentHistoryApi()

    def tearDown(self) -> None:
        pass

    def test_list_job_deployment_history(self) -> None:
        """Test case for list_job_deployment_history

        List job deployments
        """
        pass


if __name__ == '__main__':
    unittest.main()
