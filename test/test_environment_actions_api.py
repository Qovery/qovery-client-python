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

from qovery.api.environment_actions_api import EnvironmentActionsApi  # noqa: E501


class TestEnvironmentActionsApi(unittest.TestCase):
    """EnvironmentActionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EnvironmentActionsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_cancel_environment_deployment(self) -> None:
        """Test case for cancel_environment_deployment

        Cancel environment deployment  # noqa: E501
        """
        pass

    def test_clone_environment(self) -> None:
        """Test case for clone_environment

        Clone environment  # noqa: E501
        """
        pass

    def test_delete_selected_services(self) -> None:
        """Test case for delete_selected_services

        Delete services  # noqa: E501
        """
        pass

    def test_deploy_all_services(self) -> None:
        """Test case for deploy_all_services

        Deploy services  # noqa: E501
        """
        pass

    def test_deploy_environment(self) -> None:
        """Test case for deploy_environment

        Deploy environment  # noqa: E501
        """
        pass

    def test_reboot_services(self) -> None:
        """Test case for reboot_services

        Reboot services  # noqa: E501
        """
        pass

    def test_restart_environment(self) -> None:
        """Test case for restart_environment

        Deprecated - Restart environment  # noqa: E501
        """
        pass

    def test_stop_environment(self) -> None:
        """Test case for stop_environment

        Stop environment  # noqa: E501
        """
        pass

    def test_stop_selected_services(self) -> None:
        """Test case for stop_selected_services

        Stop services  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
