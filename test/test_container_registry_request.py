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
from qovery.model.container_registry_kind_enum import ContainerRegistryKindEnum
from qovery.model.container_registry_request_config import ContainerRegistryRequestConfig
globals()['ContainerRegistryKindEnum'] = ContainerRegistryKindEnum
globals()['ContainerRegistryRequestConfig'] = ContainerRegistryRequestConfig
from qovery.model.container_registry_request import ContainerRegistryRequest


class TestContainerRegistryRequest(unittest.TestCase):
    """ContainerRegistryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContainerRegistryRequest(self):
        """Test ContainerRegistryRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContainerRegistryRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
