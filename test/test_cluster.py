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
from qovery.model.cloud_provider_enum import CloudProviderEnum
from qovery.model.cluster_all_of import ClusterAllOf
from qovery.model.cluster_all_of_ssh_keys import ClusterAllOfSshKeys
from qovery.model.cluster_feature import ClusterFeature
from qovery.model.kubernetes_enum import KubernetesEnum
from qovery.model.state_enum import StateEnum
globals()['Base'] = Base
globals()['CloudProviderEnum'] = CloudProviderEnum
globals()['ClusterAllOf'] = ClusterAllOf
globals()['ClusterAllOfSshKeys'] = ClusterAllOfSshKeys
globals()['ClusterFeature'] = ClusterFeature
globals()['KubernetesEnum'] = KubernetesEnum
globals()['StateEnum'] = StateEnum
from qovery.model.cluster import Cluster


class TestCluster(unittest.TestCase):
    """Cluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCluster(self):
        """Test Cluster"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Cluster()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
