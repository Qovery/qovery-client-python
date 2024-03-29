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

from qovery.api.job_secret_api import JobSecretApi  # noqa: E501


class TestJobSecretApi(unittest.TestCase):
    """JobSecretApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobSecretApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_job_secret(self) -> None:
        """Test case for create_job_secret

        Add a secret to the job  # noqa: E501
        """
        pass

    def test_create_job_secret_alias(self) -> None:
        """Test case for create_job_secret_alias

        Create a secret alias at the job level  # noqa: E501
        """
        pass

    def test_create_job_secret_override(self) -> None:
        """Test case for create_job_secret_override

        Create a secret override at the job level  # noqa: E501
        """
        pass

    def test_delete_job_secret(self) -> None:
        """Test case for delete_job_secret

        Delete a secret from an job  # noqa: E501
        """
        pass

    def test_edit_job_secret(self) -> None:
        """Test case for edit_job_secret

        Edit a secret belonging to the job  # noqa: E501
        """
        pass

    def test_list_job_secrets(self) -> None:
        """Test case for list_job_secrets

        List job secrets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
