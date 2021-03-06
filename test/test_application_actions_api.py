"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.application_actions_api import ApplicationActionsApi  # noqa: E501


class TestApplicationActionsApi(unittest.TestCase):
    """ApplicationActionsApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deploy_application(self):
        """Test case for deploy_application

        Deploy application  # noqa: E501
        """
        pass

    def test_restart_application(self):
        """Test case for restart_application

        Restart application  # noqa: E501
        """
        pass

    def test_stop_application(self):
        """Test case for stop_application

        Stop application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
