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

from qovery.models.helm_response_all_of_values_override_file import HelmResponseAllOfValuesOverrideFile

class TestHelmResponseAllOfValuesOverrideFile(unittest.TestCase):
    """HelmResponseAllOfValuesOverrideFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HelmResponseAllOfValuesOverrideFile:
        """Test HelmResponseAllOfValuesOverrideFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HelmResponseAllOfValuesOverrideFile`
        """
        model = HelmResponseAllOfValuesOverrideFile()
        if include_optional:
            return HelmResponseAllOfValuesOverrideFile(
                raw = qovery.models.helm_response_all_of_values_override_file_raw.HelmResponse_allOf_values_override_file_raw(
                    values = [
                        qovery.models.helm_response_all_of_values_override_file_raw_values.HelmResponse_allOf_values_override_file_raw_values(
                            name = '', 
                            content = '', )
                        ], ),
                git = qovery.models.helm_response_all_of_values_override_file_git.HelmResponse_allOf_values_override_file_git(
                    git_repository = qovery.models.application_git_repository.ApplicationGitRepository(
                        has_access = True, 
                        provider = 'BITBUCKET', 
                        owner = 'John Doe', 
                        url = '', 
                        name = 'simple-node-app', 
                        branch = '', 
                        root_path = '', 
                        deployed_commit_id = '', 
                        deployed_commit_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deployed_commit_contributor = '', 
                        deployed_commit_tag = 'v1.0.1', 
                        git_token_id = '', 
                        git_token_name = '', ), 
                    paths = [
                        ''
                        ], )
            )
        else:
            return HelmResponseAllOfValuesOverrideFile(
        )
        """

    def testHelmResponseAllOfValuesOverrideFile(self):
        """Test HelmResponseAllOfValuesOverrideFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
