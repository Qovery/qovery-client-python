"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.helms_api import HelmsApi  # noqa: E501


class TestHelmsApi(unittest.TestCase):
    """HelmsApi unit test stubs"""

    def setUp(self):
        self.api = HelmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_helm(self):
        """Test case for create_helm

        Create a helm  # noqa: E501
        """
        pass

    def test_get_environment_helm_status(self):
        """Test case for get_environment_helm_status

        List all environment helm statuses  # noqa: E501
        """
        pass

    def test_list_helms(self):
        """Test case for list_helms

        List helms  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
