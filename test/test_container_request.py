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
from qovery.model.container_request_all_of import ContainerRequestAllOf
from qovery.model.service_port_request import ServicePortRequest
from qovery.model.service_port_request_ports_inner import ServicePortRequestPortsInner
from qovery.model.service_storage_request import ServiceStorageRequest
from qovery.model.service_storage_request_storage_inner import ServiceStorageRequestStorageInner
globals()['ContainerRequestAllOf'] = ContainerRequestAllOf
globals()['ServicePortRequest'] = ServicePortRequest
globals()['ServicePortRequestPortsInner'] = ServicePortRequestPortsInner
globals()['ServiceStorageRequest'] = ServiceStorageRequest
globals()['ServiceStorageRequestStorageInner'] = ServiceStorageRequestStorageInner
from qovery.model.container_request import ContainerRequest


class TestContainerRequest(unittest.TestCase):
    """ContainerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContainerRequest(self):
        """Test ContainerRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContainerRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
