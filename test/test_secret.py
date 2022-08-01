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
from qovery.model.aliased_secret import AliasedSecret
from qovery.model.base import Base
from qovery.model.environment_variable_scope_enum import EnvironmentVariableScopeEnum
from qovery.model.linked_service_type_enum import LinkedServiceTypeEnum
from qovery.model.overridden_secret import OverriddenSecret
from qovery.model.secret_all_of import SecretAllOf
globals()['AliasedSecret'] = AliasedSecret
globals()['Base'] = Base
globals()['EnvironmentVariableScopeEnum'] = EnvironmentVariableScopeEnum
globals()['LinkedServiceTypeEnum'] = LinkedServiceTypeEnum
globals()['OverriddenSecret'] = OverriddenSecret
globals()['SecretAllOf'] = SecretAllOf
from qovery.model.secret import Secret


class TestSecret(unittest.TestCase):
    """Secret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecret(self):
        """Test Secret"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Secret()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
