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

from qovery.models.deployment_rule_request import DeploymentRuleRequest

class TestDeploymentRuleRequest(unittest.TestCase):
    """DeploymentRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentRuleRequest:
        """Test DeploymentRuleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentRuleRequest`
        """
        model = DeploymentRuleRequest()
        if include_optional:
            return DeploymentRuleRequest(
                name = '',
                description = '',
                mode = 'PRODUCTION',
                cluster = '',
                auto_stop = True,
                timezone = 'Europe/London',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                stop_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                weekdays = [
                    'MONDAY'
                    ]
            )
        else:
            return DeploymentRuleRequest(
                name = '',
                mode = 'PRODUCTION',
                cluster = '',
                auto_stop = True,
        )
        """

    def testDeploymentRuleRequest(self):
        """Test DeploymentRuleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
