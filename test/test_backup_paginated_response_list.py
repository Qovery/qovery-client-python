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
from qovery.model.backup import Backup
from qovery.model.backup_response_list import BackupResponseList
from qovery.model.pagination_data import PaginationData
globals()['Backup'] = Backup
globals()['BackupResponseList'] = BackupResponseList
globals()['PaginationData'] = PaginationData
from qovery.model.backup_paginated_response_list import BackupPaginatedResponseList


class TestBackupPaginatedResponseList(unittest.TestCase):
    """BackupPaginatedResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBackupPaginatedResponseList(self):
        """Test BackupPaginatedResponseList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BackupPaginatedResponseList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
