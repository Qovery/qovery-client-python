"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.projects_api import ProjectsApi  # noqa: E501


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a project  # noqa: E501
        """
        pass

    def test_get_organization_project_stats(self):
        """Test case for get_organization_project_stats

        List total number of services and environments for each project of the organization  # noqa: E501
        """
        pass

    def test_list_project(self):
        """Test case for list_project

        List projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
