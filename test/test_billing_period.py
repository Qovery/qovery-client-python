"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.billing_end import BillingEnd
from qovery.model.billing_start import BillingStart
globals()['BillingEnd'] = BillingEnd
globals()['BillingStart'] = BillingStart
from qovery.model.billing_period import BillingPeriod


class TestBillingPeriod(unittest.TestCase):
    """BillingPeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBillingPeriod(self):
        """Test BillingPeriod"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BillingPeriod()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
