"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.service_step_metric_name_enum import ServiceStepMetricNameEnum
from qovery.model.step_metric_status_enum import StepMetricStatusEnum
globals()['ServiceStepMetricNameEnum'] = ServiceStepMetricNameEnum
globals()['StepMetricStatusEnum'] = StepMetricStatusEnum
from qovery.model.service_step_metric import ServiceStepMetric


class TestServiceStepMetric(unittest.TestCase):
    """ServiceStepMetric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceStepMetric(self):
        """Test ServiceStepMetric"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceStepMetric()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
