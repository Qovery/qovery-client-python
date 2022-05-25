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
from qovery.model.event_all_of import EventAllOf
from qovery.model.reference_object import ReferenceObject
from qovery.model.status import Status
from qovery.model.user import User
globals()['Base'] = Base
globals()['Commit'] = Commit
globals()['EventAllOf'] = EventAllOf
globals()['ReferenceObject'] = ReferenceObject
globals()['Status'] = Status
globals()['User'] = User
from qovery.model.event import Event


class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvent(self):
        """Test Event"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Event()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()