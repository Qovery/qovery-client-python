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
from qovery.model.log import Log
from qovery.model.log_paginated_response_list_all_of import LogPaginatedResponseListAllOf
from qovery.model.pagination_data import PaginationData
globals()['Log'] = Log
globals()['LogPaginatedResponseListAllOf'] = LogPaginatedResponseListAllOf
globals()['PaginationData'] = PaginationData
from qovery.model.log_paginated_response_list import LogPaginatedResponseList


class TestLogPaginatedResponseList(unittest.TestCase):
    """LogPaginatedResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogPaginatedResponseList(self):
        """Test LogPaginatedResponseList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogPaginatedResponseList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
