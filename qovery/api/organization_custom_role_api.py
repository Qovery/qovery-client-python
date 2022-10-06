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
from qovery.model.organization_custom_role import OrganizationCustomRole
from qovery.model.organization_custom_role_create_request import OrganizationCustomRoleCreateRequest
from qovery.model.organization_custom_role_list import OrganizationCustomRoleList
from qovery.model.organization_custom_role_update_request import OrganizationCustomRoleUpdateRequest


class OrganizationCustomRoleApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_organization_custom_role_endpoint = _Endpoint(
            settings={
                'response_type': (OrganizationCustomRole,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/customRole',
                'operation_id': 'create_organization_custom_role',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                    'organization_custom_role_create_request',
                ],
                'required': [
                    'organization_id',
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
                    'organization_id':
                        (str,),
                    'organization_custom_role_create_request':
                        (OrganizationCustomRoleCreateRequest,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                },
                'location_map': {
                    'organization_id': 'path',
                    'organization_custom_role_create_request': 'body',
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
        self.delete_organization_custom_role_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/customRole/{customRoleId}',
                'operation_id': 'delete_organization_custom_role',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                    'custom_role_id',
                ],
                'required': [
                    'organization_id',
                    'custom_role_id',
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
                    'organization_id':
                        (str,),
                    'custom_role_id':
                        (str,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                    'custom_role_id': 'customRoleId',
                },
                'location_map': {
                    'organization_id': 'path',
                    'custom_role_id': 'path',
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
        self.edit_organization_custom_role_endpoint = _Endpoint(
            settings={
                'response_type': (OrganizationCustomRole,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/customRole/{customRoleId}',
                'operation_id': 'edit_organization_custom_role',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                    'custom_role_id',
                    'organization_custom_role_update_request',
                ],
                'required': [
                    'organization_id',
                    'custom_role_id',
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
                    'organization_id':
                        (str,),
                    'custom_role_id':
                        (str,),
                    'organization_custom_role_update_request':
                        (OrganizationCustomRoleUpdateRequest,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                    'custom_role_id': 'customRoleId',
                },
                'location_map': {
                    'organization_id': 'path',
                    'custom_role_id': 'path',
                    'organization_custom_role_update_request': 'body',
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
        self.get_organization_custom_role_endpoint = _Endpoint(
            settings={
                'response_type': (OrganizationCustomRole,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/customRole/{customRoleId}',
                'operation_id': 'get_organization_custom_role',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                    'custom_role_id',
                ],
                'required': [
                    'organization_id',
                    'custom_role_id',
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
                    'organization_id':
                        (str,),
                    'custom_role_id':
                        (str,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                    'custom_role_id': 'customRoleId',
                },
                'location_map': {
                    'organization_id': 'path',
                    'custom_role_id': 'path',
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
        self.list_organization_custom_roles_endpoint = _Endpoint(
            settings={
                'response_type': (OrganizationCustomRoleList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/customRole',
                'operation_id': 'list_organization_custom_roles',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                ],
                'required': [
                    'organization_id',
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
                    'organization_id':
                        (str,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                },
                'location_map': {
                    'organization_id': 'path',
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

    def create_organization_custom_role(
        self,
        organization_id,
        **kwargs
    ):
        """Create an organization custom role  # noqa: E501

        Create an organization custom role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_organization_custom_role(organization_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID

        Keyword Args:
            organization_custom_role_create_request (OrganizationCustomRoleCreateRequest): [optional]
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
            OrganizationCustomRole
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
        kwargs['organization_id'] = \
            organization_id
        return self.create_organization_custom_role_endpoint.call_with_http_info(**kwargs)

    def delete_organization_custom_role(
        self,
        organization_id,
        custom_role_id,
        **kwargs
    ):
        """Delete organization custom role  # noqa: E501

        Delete organization custom role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_organization_custom_role(organization_id, custom_role_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID
            custom_role_id (str): Custom Role ID

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
        kwargs['organization_id'] = \
            organization_id
        kwargs['custom_role_id'] = \
            custom_role_id
        return self.delete_organization_custom_role_endpoint.call_with_http_info(**kwargs)

    def edit_organization_custom_role(
        self,
        organization_id,
        custom_role_id,
        **kwargs
    ):
        """Edit an organization custom role  # noqa: E501

        Edit an organization custom role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_organization_custom_role(organization_id, custom_role_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID
            custom_role_id (str): Custom Role ID

        Keyword Args:
            organization_custom_role_update_request (OrganizationCustomRoleUpdateRequest): [optional]
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
            OrganizationCustomRole
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
        kwargs['organization_id'] = \
            organization_id
        kwargs['custom_role_id'] = \
            custom_role_id
        return self.edit_organization_custom_role_endpoint.call_with_http_info(**kwargs)

    def get_organization_custom_role(
        self,
        organization_id,
        custom_role_id,
        **kwargs
    ):
        """Get an organization custom role   # noqa: E501

        Get an organization custom role   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_organization_custom_role(organization_id, custom_role_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID
            custom_role_id (str): Custom Role ID

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
            OrganizationCustomRole
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
        kwargs['organization_id'] = \
            organization_id
        kwargs['custom_role_id'] = \
            custom_role_id
        return self.get_organization_custom_role_endpoint.call_with_http_info(**kwargs)

    def list_organization_custom_roles(
        self,
        organization_id,
        **kwargs
    ):
        """List organization custom roles  # noqa: E501

        List organization custom roles  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_organization_custom_roles(organization_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID

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
            OrganizationCustomRoleList
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
        kwargs['organization_id'] = \
            organization_id
        return self.list_organization_custom_roles_endpoint.call_with_http_info(**kwargs)

