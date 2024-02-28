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

from qovery.models.deployment_history_application import DeploymentHistoryApplication  # noqa: E501

class TestDeploymentHistoryApplication(unittest.TestCase):
    """DeploymentHistoryApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentHistoryApplication:
        """Test DeploymentHistoryApplication
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentHistoryApplication`
        """
        model = DeploymentHistoryApplication()  # noqa: E501
        if include_optional:
            return DeploymentHistoryApplication(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                commit = qovery.models.commit.Commit(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    git_commit_id = '', 
                    tag = 'v2.1.1', 
                    message = '', 
                    author_name = '', 
                    author_avatar_url = '', 
                    commit_page_url = '', ),
                status = 'BUILDING'
            )
        else:
            return DeploymentHistoryApplication(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDeploymentHistoryApplication(self):
        """Test DeploymentHistoryApplication"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
