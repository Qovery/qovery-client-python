"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from qovery.api_client import ApiClient, Endpoint as _Endpoint
from qovery.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from qovery.model.environment_deployment_rule import EnvironmentDeploymentRule
from qovery.model.environment_deployment_rule_edit_request import EnvironmentDeploymentRuleEditRequest


class EnvironmentDeploymentRuleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.edit_environment_deployment_rule_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentDeploymentRule,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/deploymentRule/{deploymentRuleId}',
                'operation_id': 'edit_environment_deployment_rule',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'deployment_rule_id',
                    'environment_deployment_rule_edit_request',
                ],
                'required': [
                    'environment_id',
                    'deployment_rule_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_id':
                        (str,),
                    'deployment_rule_id':
                        (str,),
                    'environment_deployment_rule_edit_request':
                        (EnvironmentDeploymentRuleEditRequest,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                    'deployment_rule_id': 'deploymentRuleId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'deployment_rule_id': 'path',
                    'environment_deployment_rule_edit_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_environment_deployment_rule_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentDeploymentRule,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/deploymentRule',
                'operation_id': 'get_environment_deployment_rule',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                ],
                'required': [
                    'environment_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'environment_id':
                        (str,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                },
                'location_map': {
                    'environment_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def edit_environment_deployment_rule(
        self,
        environment_id,
        deployment_rule_id,
        **kwargs
    ):
        """Edit an environment deployment rule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_environment_deployment_rule(environment_id, deployment_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID
            deployment_rule_id (str): Deployment Rule ID

        Keyword Args:
            environment_deployment_rule_edit_request (EnvironmentDeploymentRuleEditRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentDeploymentRule
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment_id'] = \
            environment_id
        kwargs['deployment_rule_id'] = \
            deployment_rule_id
        return self.edit_environment_deployment_rule_endpoint.call_with_http_info(**kwargs)

    def get_environment_deployment_rule(
        self,
        environment_id,
        **kwargs
    ):
        """Get environment deployment rule  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_environment_deployment_rule(environment_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentDeploymentRule
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['environment_id'] = \
            environment_id
        return self.get_environment_deployment_rule_endpoint.call_with_http_info(**kwargs)

