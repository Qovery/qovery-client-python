"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.event_response import EventResponse
from qovery.model.pagination_data_response import PaginationDataResponse
globals()['EventResponse'] = EventResponse
globals()['PaginationDataResponse'] = PaginationDataResponse
from qovery.model.event_paginated_response_list import EventPaginatedResponseList


class TestEventPaginatedResponseList(unittest.TestCase):
    """EventPaginatedResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventPaginatedResponseList(self):
        """Test EventPaginatedResponseList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventPaginatedResponseList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
