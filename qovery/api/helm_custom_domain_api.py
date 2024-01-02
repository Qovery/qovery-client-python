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
from qovery.model.custom_domain import CustomDomain
from qovery.model.custom_domain_request import CustomDomainRequest


class HelmCustomDomainApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_helm_custom_domain_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/helm/{helmId}/customDomain/{customDomainId}',
                'operation_id': 'delete_helm_custom_domain',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'helm_id',
                    'custom_domain_id',
                ],
                'required': [
                    'helm_id',
                    'custom_domain_id',
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
                    'helm_id':
                        (str,),
                    'custom_domain_id':
                        (str,),
                },
                'attribute_map': {
                    'helm_id': 'helmId',
                    'custom_domain_id': 'customDomainId',
                },
                'location_map': {
                    'helm_id': 'path',
                    'custom_domain_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.edit_helm_custom_domain_endpoint = _Endpoint(
            settings={
                'response_type': (CustomDomain,),
                'auth': [
                    'ApiKeyAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/helm/{helmId}/customDomain/{customDomainId}',
                'operation_id': 'edit_helm_custom_domain',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'helm_id',
                    'custom_domain_id',
                    'custom_domain_request',
                ],
                'required': [
                    'helm_id',
                    'custom_domain_id',
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
                    'helm_id':
                        (str,),
                    'custom_domain_id':
                        (str,),
                    'custom_domain_request':
                        (CustomDomainRequest,),
                },
                'attribute_map': {
                    'helm_id': 'helmId',
                    'custom_domain_id': 'customDomainId',
                },
                'location_map': {
                    'helm_id': 'path',
                    'custom_domain_id': 'path',
                    'custom_domain_request': 'body',
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
        self.get_helm_custom_domain_endpoint = _Endpoint(
            settings={
                'response_type': (CustomDomain,),
                'auth': [
                    'ApiKeyAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/helm/{helmId}/customDomain/{customDomainId}',
                'operation_id': 'get_helm_custom_domain',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'helm_id',
                    'custom_domain_id',
                ],
                'required': [
                    'helm_id',
                    'custom_domain_id',
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
                    'helm_id':
                        (str,),
                    'custom_domain_id':
                        (str,),
                },
                'attribute_map': {
                    'helm_id': 'helmId',
                    'custom_domain_id': 'customDomainId',
                },
                'location_map': {
                    'helm_id': 'path',
                    'custom_domain_id': 'path',
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

    def delete_helm_custom_domain(
        self,
        helm_id,
        custom_domain_id,
        **kwargs
    ):
        """Delete a Custom Domain  # noqa: E501

        To delete an CustomDomain you must have the project user permission  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_helm_custom_domain(helm_id, custom_domain_id, async_req=True)
        >>> result = thread.get()

        Args:
            helm_id (str): Helm ID
            custom_domain_id (str): Custom Domain ID

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
            None
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
        kwargs['helm_id'] = \
            helm_id
        kwargs['custom_domain_id'] = \
            custom_domain_id
        return self.delete_helm_custom_domain_endpoint.call_with_http_info(**kwargs)

    def edit_helm_custom_domain(
        self,
        helm_id,
        custom_domain_id,
        **kwargs
    ):
        """Edit a Custom Domain  # noqa: E501

        To edit a Custom Domain you must have the project user permission  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_helm_custom_domain(helm_id, custom_domain_id, async_req=True)
        >>> result = thread.get()

        Args:
            helm_id (str): Helm ID
            custom_domain_id (str): Custom Domain ID

        Keyword Args:
            custom_domain_request (CustomDomainRequest): [optional]
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
            CustomDomain
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
        kwargs['helm_id'] = \
            helm_id
        kwargs['custom_domain_id'] = \
            custom_domain_id
        return self.edit_helm_custom_domain_endpoint.call_with_http_info(**kwargs)

    def get_helm_custom_domain(
        self,
        helm_id,
        custom_domain_id,
        **kwargs
    ):
        """Get a Custom Domain  # noqa: E501

        Get a custom domain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_helm_custom_domain(helm_id, custom_domain_id, async_req=True)
        >>> result = thread.get()

        Args:
            helm_id (str): Helm ID
            custom_domain_id (str): Custom Domain ID

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
            CustomDomain
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
        kwargs['helm_id'] = \
            helm_id
        kwargs['custom_domain_id'] = \
            custom_domain_id
        return self.get_helm_custom_domain_endpoint.call_with_http_info(**kwargs)

