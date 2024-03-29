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

from qovery.models.environment_deployment_rule_edit_request import EnvironmentDeploymentRuleEditRequest  # noqa: E501

class TestEnvironmentDeploymentRuleEditRequest(unittest.TestCase):
    """EnvironmentDeploymentRuleEditRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentDeploymentRuleEditRequest:
        """Test EnvironmentDeploymentRuleEditRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentDeploymentRuleEditRequest`
        """
        model = EnvironmentDeploymentRuleEditRequest()  # noqa: E501
        if include_optional:
            return EnvironmentDeploymentRuleEditRequest(
                on_demand_preview = True,
                auto_preview = True,
                auto_stop = True,
                timezone = 'UTC',
                start_time = '1970-01-01T08:00Z',
                stop_time = '1970-01-01T19:00Z',
                weekdays = [
                    'MONDAY'
                    ]
            )
        else:
            return EnvironmentDeploymentRuleEditRequest(
                timezone = 'UTC',
                start_time = '1970-01-01T08:00Z',
                stop_time = '1970-01-01T19:00Z',
                weekdays = [
                    'MONDAY'
                    ],
        )
        """

    def testEnvironmentDeploymentRuleEditRequest(self):
        """Test EnvironmentDeploymentRuleEditRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
