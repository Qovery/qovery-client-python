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
from qovery.model.cost_response import CostResponse
from qovery.model.invoice_response_all_of import InvoiceResponseAllOf
globals()['CostResponse'] = CostResponse
globals()['InvoiceResponseAllOf'] = InvoiceResponseAllOf
from qovery.model.invoice_response import InvoiceResponse


class TestInvoiceResponse(unittest.TestCase):
    """InvoiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoiceResponse(self):
        """Test InvoiceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InvoiceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
