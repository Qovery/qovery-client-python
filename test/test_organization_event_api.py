"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.organization_event_api import OrganizationEventApi  # noqa: E501


class TestOrganizationEventApi(unittest.TestCase):
    """OrganizationEventApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationEventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_organization_event_targets(self):
        """Test case for get_organization_event_targets

        Get available event targets to filter events  # noqa: E501
        """
        pass

    def test_get_organization_events(self):
        """Test case for get_organization_events

        Get all events inside the organization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
