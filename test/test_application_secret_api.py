"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.application_secret_api import ApplicationSecretApi  # noqa: E501


class TestApplicationSecretApi(unittest.TestCase):
    """ApplicationSecretApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationSecretApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application_secret(self):
        """Test case for create_application_secret

        Add a secret to the application  # noqa: E501
        """
        pass

    def test_create_application_secret_alias(self):
        """Test case for create_application_secret_alias

        Create a secret alias at the application level  # noqa: E501
        """
        pass

    def test_create_application_secret_override(self):
        """Test case for create_application_secret_override

        Create a secret override at the application level  # noqa: E501
        """
        pass

    def test_delete_application_secret(self):
        """Test case for delete_application_secret

        Delete a secret from an application  # noqa: E501
        """
        pass

    def test_edit_application_secret(self):
        """Test case for edit_application_secret

        Edit a secret belonging to the application  # noqa: E501
        """
        pass

    def test_list_application_secrets(self):
        """Test case for list_application_secrets

        List application secrets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
