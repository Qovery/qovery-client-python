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

from qovery.api.helms_api import HelmsApi  # noqa: E501


class TestHelmsApi(unittest.TestCase):
    """HelmsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HelmsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_clone_helm(self) -> None:
        """Test case for clone_helm

        Clone helm  # noqa: E501
        """
        pass

    def test_create_helm(self) -> None:
        """Test case for create_helm

        Create a helm  # noqa: E501
        """
        pass

    def test_create_helm_default_values(self) -> None:
        """Test case for create_helm_default_values

        Get helm default values  # noqa: E501
        """
        pass

    def test_get_default_helm_advanced_settings(self) -> None:
        """Test case for get_default_helm_advanced_settings

        List default helm advanced settings  # noqa: E501
        """
        pass

    def test_get_environment_helm_status(self) -> None:
        """Test case for get_environment_helm_status

        List all environment helm statuses  # noqa: E501
        """
        pass

    def test_list_helms(self) -> None:
        """Test case for list_helms

        List helms  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
