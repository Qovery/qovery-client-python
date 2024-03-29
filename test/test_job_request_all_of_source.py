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

from qovery.models.job_request_all_of_source import JobRequestAllOfSource  # noqa: E501

class TestJobRequestAllOfSource(unittest.TestCase):
    """JobRequestAllOfSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobRequestAllOfSource:
        """Test JobRequestAllOfSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobRequestAllOfSource`
        """
        model = JobRequestAllOfSource()  # noqa: E501
        if include_optional:
            return JobRequestAllOfSource(
                image = qovery.models.job_request_all_of_source_image.JobRequest_allOf_source_image(
                    image_name = '', 
                    tag = '', 
                    registry_id = '', ),
                docker = qovery.models.job_request_all_of_source_docker.JobRequest_allOf_source_docker(
                    dockerfile_path = '', 
                    git_repository = qovery.models.application_git_repository_request.ApplicationGitRepositoryRequest(
                        url = 'https://github.com/Qovery/simple-node-app', 
                        branch = 'feat/text_xxx', 
                        root_path = '/', 
                        git_token_id = '', ), )
            )
        else:
            return JobRequestAllOfSource(
        )
        """

    def testJobRequestAllOfSource(self):
        """Test JobRequestAllOfSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
