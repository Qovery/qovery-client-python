"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from api.application_event_api import ApplicationEventApi  # noqa: E501


class TestApplicationEventApi(unittest.TestCase):
    """ApplicationEventApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationEventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_application_event(self):
        """Test case for list_application_event

        List application events  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
