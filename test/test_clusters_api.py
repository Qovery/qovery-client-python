"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.clusters_api import ClustersApi  # noqa: E501


class TestClustersApi(unittest.TestCase):
    """ClustersApi unit test stubs"""

    def setUp(self):
        self.api = ClustersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster(self):
        """Test case for create_cluster

        Create a cluster  # noqa: E501
        """
        pass

    def test_delete_cluster(self):
        """Test case for delete_cluster

        Delete a cluster  # noqa: E501
        """
        pass

    def test_deploy_cluster(self):
        """Test case for deploy_cluster

        Deploy a cluster  # noqa: E501
        """
        pass

    def test_edit_cluster(self):
        """Test case for edit_cluster

        Edit a cluster  # noqa: E501
        """
        pass

    def test_edit_routing_table(self):
        """Test case for edit_routing_table

        Edit routing table  # noqa: E501
        """
        pass

    def test_get_cluster_readiness_status(self):
        """Test case for get_cluster_readiness_status

        Know if a cluster is ready to be deployed or not  # noqa: E501
        """
        pass

    def test_get_cluster_status(self):
        """Test case for get_cluster_status

        Get cluster status  # noqa: E501
        """
        pass

    def test_get_organization_cloud_provider_info(self):
        """Test case for get_organization_cloud_provider_info

        Get cluster cloud provider info and credentials  # noqa: E501
        """
        pass

    def test_get_organization_cluster_status(self):
        """Test case for get_organization_cluster_status

        List all clusters statuses  # noqa: E501
        """
        pass

    def test_get_routing_table(self):
        """Test case for get_routing_table

        Get routing table  # noqa: E501
        """
        pass

    def test_list_organization_cluster(self):
        """Test case for list_organization_cluster

        List organization clusters  # noqa: E501
        """
        pass

    def test_specify_cluster_cloud_provider_info(self):
        """Test case for specify_cluster_cloud_provider_info

        Specify cluster cloud provider info and credentials  # noqa: E501
        """
        pass

    def test_stop_cluster(self):
        """Test case for stop_cluster

        Stop cluster  # noqa: E501
        """
        pass

    def test_update_cluster(self):
        """Test case for update_cluster

        Update a cluster Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
