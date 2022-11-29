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
from qovery.model.base import Base
from qovery.model.job_request_all_of_schedule import JobRequestAllOfSchedule
from qovery.model.job_response_all_of import JobResponseAllOf
from qovery.model.job_response_all_of_source import JobResponseAllOfSource
from qovery.model.reference_object import ReferenceObject
globals()['Base'] = Base
globals()['JobRequestAllOfSchedule'] = JobRequestAllOfSchedule
globals()['JobResponseAllOf'] = JobResponseAllOf
globals()['JobResponseAllOfSource'] = JobResponseAllOfSource
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.job_response import JobResponse


class TestJobResponse(unittest.TestCase):
    """JobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobResponse(self):
        """Test JobResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()