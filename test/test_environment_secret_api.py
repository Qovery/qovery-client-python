"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.environment_secret_api import EnvironmentSecretApi  # noqa: E501


class TestEnvironmentSecretApi(unittest.TestCase):
    """EnvironmentSecretApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentSecretApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_environment_secret(self):
        """Test case for create_environment_secret

        Add a secret to the environment  # noqa: E501
        """
        pass

    def test_create_environment_secret_alias(self):
        """Test case for create_environment_secret_alias

        Create a secret alias at the environment level  # noqa: E501
        """
        pass

    def test_create_environment_secret_override(self):
        """Test case for create_environment_secret_override

        Create a secret override at the environment level  # noqa: E501
        """
        pass

    def test_delete_environment_secret(self):
        """Test case for delete_environment_secret

        Delete a secret from the environment  # noqa: E501
        """
        pass

    def test_edit_environment_secret(self):
        """Test case for edit_environment_secret

        Edit a secret belonging to the environment  # noqa: E501
        """
        pass

    def test_list_environment_secrets(self):
        """Test case for list_environment_secrets

        List environment secrets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
