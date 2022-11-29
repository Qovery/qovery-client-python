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
from qovery.model.commit import Commit
from qovery.model.deployment_history_job_response_all_of import DeploymentHistoryJobResponseAllOf
from qovery.model.deployment_history_status_enum import DeploymentHistoryStatusEnum
from qovery.model.job_request_all_of_schedule import JobRequestAllOfSchedule
globals()['Base'] = Base
globals()['Commit'] = Commit
globals()['DeploymentHistoryJobResponseAllOf'] = DeploymentHistoryJobResponseAllOf
globals()['DeploymentHistoryStatusEnum'] = DeploymentHistoryStatusEnum
globals()['JobRequestAllOfSchedule'] = JobRequestAllOfSchedule
from qovery.model.deployment_history_job_response import DeploymentHistoryJobResponse


class TestDeploymentHistoryJobResponse(unittest.TestCase):
    """DeploymentHistoryJobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeploymentHistoryJobResponse(self):
        """Test DeploymentHistoryJobResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeploymentHistoryJobResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()