"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.base import Base
from qovery.model.environment_deployment_rule_all_of import EnvironmentDeploymentRuleAllOf
from qovery.model.weekday_enum import WeekdayEnum
globals()['Base'] = Base
globals()['EnvironmentDeploymentRuleAllOf'] = EnvironmentDeploymentRuleAllOf
globals()['WeekdayEnum'] = WeekdayEnum
from qovery.model.environment_deployment_rule import EnvironmentDeploymentRule


class TestEnvironmentDeploymentRule(unittest.TestCase):
    """EnvironmentDeploymentRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnvironmentDeploymentRule(self):
        """Test EnvironmentDeploymentRule"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnvironmentDeploymentRule()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
