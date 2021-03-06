"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.project_secret_api import ProjectSecretApi  # noqa: E501


class TestProjectSecretApi(unittest.TestCase):
    """ProjectSecretApi unit test stubs"""

    def setUp(self):
        self.api = ProjectSecretApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_secret(self):
        """Test case for create_project_secret

        Add a secret to the project  # noqa: E501
        """
        pass

    def test_create_project_secret_alias(self):
        """Test case for create_project_secret_alias

        Create a secret alias at the project level  # noqa: E501
        """
        pass

    def test_create_project_secret_override(self):
        """Test case for create_project_secret_override

        Create a secret override at the project level  # noqa: E501
        """
        pass

    def test_delete_project_secret(self):
        """Test case for delete_project_secret

        Delete a secret from a project  # noqa: E501
        """
        pass

    def test_edit_project_secret(self):
        """Test case for edit_project_secret

        Edit a secret belonging to the project  # noqa: E501
        """
        pass

    def test_list_project_secrets(self):
        """Test case for list_project_secrets

        List project secrets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
