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

from qovery.models.organization_webhook_create_response import OrganizationWebhookCreateResponse

class TestOrganizationWebhookCreateResponse(unittest.TestCase):
    """OrganizationWebhookCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationWebhookCreateResponse:
        """Test OrganizationWebhookCreateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationWebhookCreateResponse`
        """
        model = OrganizationWebhookCreateResponse()
        if include_optional:
            return OrganizationWebhookCreateResponse(
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
            return OrganizationWebhookCreateResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testOrganizationWebhookCreateResponse(self):
        """Test OrganizationWebhookCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
