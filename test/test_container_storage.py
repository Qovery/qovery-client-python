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
from qovery.model.application_storage import ApplicationStorage
from qovery.model.application_storage_storage import ApplicationStorageStorage
globals()['ApplicationStorage'] = ApplicationStorage
globals()['ApplicationStorageStorage'] = ApplicationStorageStorage
from qovery.model.container_storage import ContainerStorage


class TestContainerStorage(unittest.TestCase):
    """ContainerStorage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContainerStorage(self):
        """Test ContainerStorage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContainerStorage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
