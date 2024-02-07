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

from qovery.api.environment_export_api import EnvironmentExportApi


class TestEnvironmentExportApi(unittest.TestCase):
    """EnvironmentExportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EnvironmentExportApi()

    def tearDown(self) -> None:
        pass

    def test_export_environment_configuration_into_terraform(self) -> None:
        """Test case for export_environment_configuration_into_terraform

        Export full environment and its resources into Terraform manifests
        """
        pass


if __name__ == '__main__':
    unittest.main()
