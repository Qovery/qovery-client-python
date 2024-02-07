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

from qovery.models.service_step_metrics import ServiceStepMetrics

class TestServiceStepMetrics(unittest.TestCase):
    """ServiceStepMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceStepMetrics:
        """Test ServiceStepMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceStepMetrics`
        """
        model = ServiceStepMetrics()
        if include_optional:
            return ServiceStepMetrics(
                total_duration_sec = 56,
                total_computing_duration_sec = 56,
                details = [
                    qovery.models.service_step_metric.ServiceStepMetric(
                        step_name = 'REGISTRY_CREATE_REPOSITORY', 
                        status = 'SUCCESS', 
                        duration_sec = 56, )
                    ]
            )
        else:
            return ServiceStepMetrics(
        )
        """

    def testServiceStepMetrics(self):
        """Test ServiceStepMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
