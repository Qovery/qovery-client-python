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

from qovery.models.helm_response_all_of_ports import HelmResponseAllOfPorts

class TestHelmResponseAllOfPorts(unittest.TestCase):
    """HelmResponseAllOfPorts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HelmResponseAllOfPorts:
        """Test HelmResponseAllOfPorts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HelmResponseAllOfPorts`
        """
        model = HelmResponseAllOfPorts()
        if include_optional:
            return HelmResponseAllOfPorts(
                id = '',
                name = '',
                internal_port = 8080,
                external_port = 8080,
                service_name = '',
                namespace = '',
                protocol = 'HTTP',
                is_default = True
            )
        else:
            return HelmResponseAllOfPorts(
                id = '',
                internal_port = 8080,
                service_name = '',
                protocol = 'HTTP',
        )
        """

    def testHelmResponseAllOfPorts(self):
        """Test HelmResponseAllOfPorts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
