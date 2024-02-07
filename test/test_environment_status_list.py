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

from qovery.models.environment_status_list import EnvironmentStatusList

class TestEnvironmentStatusList(unittest.TestCase):
    """EnvironmentStatusList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentStatusList:
        """Test EnvironmentStatusList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentStatusList`
        """
        model = EnvironmentStatusList()
        if include_optional:
            return EnvironmentStatusList(
                results = [
                    qovery.models.environment_status.EnvironmentStatus(
                        id = '', 
                        state = 'BUILDING', 
                        last_deployment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_deployment_state = 'BUILDING', 
                        last_deployment_id = '', 
                        total_deployment_duration_in_seconds = 56, 
                        origin = 'API', 
                        triggered_by = '', )
                    ]
            )
        else:
            return EnvironmentStatusList(
        )
        """

    def testEnvironmentStatusList(self):
        """Test EnvironmentStatusList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
