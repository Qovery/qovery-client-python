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
import datetime

from qovery.models.organization_webhook_response import OrganizationWebhookResponse

class TestOrganizationWebhookResponse(unittest.TestCase):
    """OrganizationWebhookResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationWebhookResponse:
        """Test OrganizationWebhookResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationWebhookResponse`
        """
        model = OrganizationWebhookResponse()
        if include_optional:
            return OrganizationWebhookResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                kind = 'STANDARD',
                target_url = '',
                target_secret_set = True,
                description = '',
                enabled = True,
                events = [
                    'DEPLOYMENT_STARTED'
                    ],
                project_names_filter = [
                    ''
                    ],
                environment_types_filter = [
                    'PRODUCTION'
                    ]
            )
        else:
            return OrganizationWebhookResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testOrganizationWebhookResponse(self):
        """Test OrganizationWebhookResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
