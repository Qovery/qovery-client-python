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

from qovery.models.organization_event_response_list import OrganizationEventResponseList  # noqa: E501

class TestOrganizationEventResponseList(unittest.TestCase):
    """OrganizationEventResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationEventResponseList:
        """Test OrganizationEventResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationEventResponseList`
        """
        model = OrganizationEventResponseList()  # noqa: E501
        if include_optional:
            return OrganizationEventResponseList(
                links = qovery.models.organization_event_response_list_links.OrganizationEventResponseList_links(
                    previous = '', 
                    next = '', ),
                events = [
                    qovery.models.organization_event_response.OrganizationEventResponse(
                        id = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        event_type = 'CREATE', 
                        target_id = '', 
                        target_name = '', 
                        target_type = 'APPLICATION', 
                        sub_target_type = 'ADVANCED_SETTINGS', 
                        change = '', 
                        origin = 'API', 
                        triggered_by = '', 
                        project_id = '', 
                        project_name = '', 
                        environment_id = '', 
                        environment_name = '', )
                    ]
            )
        else:
            return OrganizationEventResponseList(
        )
        """

    def testOrganizationEventResponseList(self):
        """Test OrganizationEventResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
