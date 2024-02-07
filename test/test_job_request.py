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

from qovery.models.job_request import JobRequest

class TestJobRequest(unittest.TestCase):
    """JobRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobRequest:
        """Test JobRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobRequest`
        """
        model = JobRequest()
        if include_optional:
            return JobRequest(
                name = '',
                description = '',
                cpu = 1250,
                memory = 1024,
                max_nb_restart = 0,
                max_duration_seconds = 0,
                auto_preview = True,
                port = 1,
                source = qovery.models.job_request_all_of_source.JobRequest_allOf_source(
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
                            git_token_id = '', ), ), ),
                healthchecks = qovery.models.healthcheck.Healthcheck(
                    readiness_probe = qovery.models.probe.Probe(
                        type = qovery.models.probe_type.Probe_type(
                            tcp = qovery.models.probe_type_tcp.Probe_type_tcp(
                                port = 56, 
                                host = '', ), 
                            http = qovery.models.probe_type_http.Probe_type_http(
                                path = '/', 
                                scheme = 'HTTP', 
                                port = 56, ), 
                            exec = qovery.models.probe_type_exec.Probe_type_exec(
                                command = [
                                    ''
                                    ], ), 
                            grpc = qovery.models.probe_type_grpc.Probe_type_grpc(
                                service = '', 
                                port = 56, ), ), 
                        initial_delay_seconds = 56, 
                        period_seconds = 56, 
                        timeout_seconds = 56, 
                        success_threshold = 56, 
                        failure_threshold = 56, ), 
                    liveness_probe = qovery.models.probe.Probe(
                        initial_delay_seconds = 56, 
                        period_seconds = 56, 
                        timeout_seconds = 56, 
                        success_threshold = 56, 
                        failure_threshold = 56, ), ),
                schedule = qovery.models.job_request_all_of_schedule.JobRequest_allOf_schedule(
                    on_start = qovery.models.job_request_all_of_schedule_on_start.JobRequest_allOf_schedule_on_start(
                        arguments = [
                            ''
                            ], 
                        entrypoint = '', ), 
                    on_stop = qovery.models.job_request_all_of_schedule_on_start.JobRequest_allOf_schedule_on_start(
                        entrypoint = '', ), 
                    on_delete = , 
                    cronjob = qovery.models.job_request_all_of_schedule_cronjob.JobRequest_allOf_schedule_cronjob(
                        entrypoint = '', 
                        timezone = '', 
                        scheduled_at = '', ), ),
                auto_deploy = True
            )
        else:
            return JobRequest(
                name = '',
                healthchecks = qovery.models.healthcheck.Healthcheck(
                    readiness_probe = qovery.models.probe.Probe(
                        type = qovery.models.probe_type.Probe_type(
                            tcp = qovery.models.probe_type_tcp.Probe_type_tcp(
                                port = 56, 
                                host = '', ), 
                            http = qovery.models.probe_type_http.Probe_type_http(
                                path = '/', 
                                scheme = 'HTTP', 
                                port = 56, ), 
                            exec = qovery.models.probe_type_exec.Probe_type_exec(
                                command = [
                                    ''
                                    ], ), 
                            grpc = qovery.models.probe_type_grpc.Probe_type_grpc(
                                service = '', 
                                port = 56, ), ), 
                        initial_delay_seconds = 56, 
                        period_seconds = 56, 
                        timeout_seconds = 56, 
                        success_threshold = 56, 
                        failure_threshold = 56, ), 
                    liveness_probe = qovery.models.probe.Probe(
                        initial_delay_seconds = 56, 
                        period_seconds = 56, 
                        timeout_seconds = 56, 
                        success_threshold = 56, 
                        failure_threshold = 56, ), ),
        )
        """

    def testJobRequest(self):
        """Test JobRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
