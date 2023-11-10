"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.helm_main_calls_api import HelmMainCallsApi  # noqa: E501


class TestHelmMainCallsApi(unittest.TestCase):
    """HelmMainCallsApi unit test stubs"""

    def setUp(self):
        self.api = HelmMainCallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_helm(self):
        """Test case for delete_helm

        Delete helm  # noqa: E501
        """
        pass

    def test_edit_helm(self):
        """Test case for edit_helm

        Edit helm  # noqa: E501
        """
        pass

    def test_get_default_values(self):
        """Test case for get_default_values

        Display the contents of the values.yaml file  # noqa: E501
        """
        pass

    def test_get_helm(self):
        """Test case for get_helm

        Get helm by ID  # noqa: E501
        """
        pass

    def test_get_helm_status(self):
        """Test case for get_helm_status

        Get helm status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
