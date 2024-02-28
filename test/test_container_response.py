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
from qovery.model.base import Base
from qovery.model.container_registry_provider_details_response import ContainerRegistryProviderDetailsResponse
from qovery.model.container_response_all_of import ContainerResponseAllOf
from qovery.model.container_source import ContainerSource
from qovery.model.healthcheck import Healthcheck
from qovery.model.reference_object import ReferenceObject
from qovery.model.service_port_response_list import ServicePortResponseList
from qovery.model.service_storage import ServiceStorage
from qovery.model.service_storage_storage_inner import ServiceStorageStorageInner
globals()['Base'] = Base
globals()['ContainerRegistryProviderDetailsResponse'] = ContainerRegistryProviderDetailsResponse
globals()['ContainerResponseAllOf'] = ContainerResponseAllOf
globals()['ContainerSource'] = ContainerSource
globals()['Healthcheck'] = Healthcheck
globals()['ReferenceObject'] = ReferenceObject
globals()['ServicePortResponseList'] = ServicePortResponseList
globals()['ServiceStorage'] = ServiceStorage
globals()['ServiceStorageStorageInner'] = ServiceStorageStorageInner
from qovery.model.container_response import ContainerResponse


class TestContainerResponse(unittest.TestCase):
    """ContainerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContainerResponse(self):
        """Test ContainerResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContainerResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
