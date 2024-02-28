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

from qovery.models.log_paginated_response_list import LogPaginatedResponseList  # noqa: E501

class TestLogPaginatedResponseList(unittest.TestCase):
    """LogPaginatedResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogPaginatedResponseList:
        """Test LogPaginatedResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogPaginatedResponseList`
        """
        model = LogPaginatedResponseList()  # noqa: E501
        if include_optional:
            return LogPaginatedResponseList(
                page = 1,
                page_size = 20,
                results = [
                    qovery.models.log.Log(
                        id = '4aa76065-68b3-41ef-aa1d-46be67012bef', 
                        created_at = '2022-04-19T15:36:12.024Z', 
                        message = '', 
                        pod_name = 'app-z4aa76065-57d84cbbdb-xcg8v', 
                        version = '2bfd61fe45946c74f318050b26210be486c43a39', )
                    ]
            )
        else:
            return LogPaginatedResponseList(
                page = 1,
                page_size = 20,
        )
        """

    def testLogPaginatedResponseList(self):
        """Test LogPaginatedResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
