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

from qovery.models.job_advanced_settings import JobAdvancedSettings  # noqa: E501

class TestJobAdvancedSettings(unittest.TestCase):
    """JobAdvancedSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobAdvancedSettings:
        """Test JobAdvancedSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobAdvancedSettings`
        """
        model = JobAdvancedSettings()  # noqa: E501
        if include_optional:
            return JobAdvancedSettings(
                build_timeout_max_sec = 56,
                build_cpu_max_in_milli = 56,
                build_ram_max_in_gib = 56,
                deployment_termination_grace_period_seconds = 56,
                deployment_affinity_node_required = {
                    'key' : ''
                    },
                job_delete_ttl_seconds_after_finished = 56,
                cronjob_concurrency_policy = '',
                cronjob_failed_jobs_history_limit = 56,
                cronjob_success_jobs_history_limit = 56,
                security_service_account_name = '',
                security_automount_service_account_token = True,
                security_read_only_root_filesystem = True
            )
        else:
            return JobAdvancedSettings(
        )
        """

    def testJobAdvancedSettings(self):
        """Test JobAdvancedSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
