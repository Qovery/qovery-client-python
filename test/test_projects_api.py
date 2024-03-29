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

from qovery.api.projects_api import ProjectsApi  # noqa: E501


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_project(self) -> None:
        """Test case for create_project

        Create a project  # noqa: E501
        """
        pass

    def test_get_organization_project_stats(self) -> None:
        """Test case for get_organization_project_stats

        List total number of services and environments for each project of the organization  # noqa: E501
        """
        pass

    def test_list_project(self) -> None:
        """Test case for list_project

        List projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
