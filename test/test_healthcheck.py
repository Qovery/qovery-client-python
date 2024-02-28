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
from qovery.model.probe import Probe
globals()['Probe'] = Probe
from qovery.model.healthcheck import Healthcheck


class TestHealthcheck(unittest.TestCase):
    """Healthcheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHealthcheck(self):
        """Test Healthcheck"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Healthcheck()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
