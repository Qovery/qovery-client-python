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
from qovery.model.service_all_of import ServiceAllOf
from qovery.model.service_type_enum import ServiceTypeEnum
globals()['Base'] = Base
globals()['ServiceAllOf'] = ServiceAllOf
globals()['ServiceTypeEnum'] = ServiceTypeEnum
from qovery.model.service import Service


class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testService(self):
        """Test Service"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Service()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
