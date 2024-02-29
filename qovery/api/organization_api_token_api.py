# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from typing import Optional

from qovery.models.organization_api_token_create import OrganizationApiTokenCreate
from qovery.models.organization_api_token_create_request import OrganizationApiTokenCreateRequest
from qovery.models.organization_api_token_response_list import OrganizationApiTokenResponseList

from qovery.api_client import ApiClient
from qovery.api_response import ApiResponse
from qovery.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OrganizationApiTokenApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_organization_api_token(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], organization_api_token_create_request : Optional[OrganizationApiTokenCreateRequest] = None, **kwargs) -> OrganizationApiTokenCreate:  # noqa: E501
        """Create an organization api token  # noqa: E501

        Create an organization api token. You can use the generated token to interact in a programmatic way with our API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_organization_api_token(organization_id, organization_api_token_create_request, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param organization_api_token_create_request:
        :type organization_api_token_create_request: OrganizationApiTokenCreateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: OrganizationApiTokenCreate
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_organization_api_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_organization_api_token_with_http_info(organization_id, organization_api_token_create_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_organization_api_token_with_http_info(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], organization_api_token_create_request : Optional[OrganizationApiTokenCreateRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create an organization api token  # noqa: E501

        Create an organization api token. You can use the generated token to interact in a programmatic way with our API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_organization_api_token_with_http_info(organization_id, organization_api_token_create_request, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param organization_api_token_create_request:
        :type organization_api_token_create_request: OrganizationApiTokenCreateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(OrganizationApiTokenCreate, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'organization_id',
            'organization_api_token_create_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization_api_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization_id']:
            _path_params['organizationId'] = _params['organization_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['organization_api_token_create_request'] is not None:
            _body_params = _params['organization_api_token_create_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'bearerAuth']  # noqa: E501

        _response_types_map = {
            '201': "OrganizationApiTokenCreate",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
        }

        return self.api_client.call_api(
            '/organization/{organizationId}/apiToken', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_organization_api_token(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], api_token_id : Annotated[StrictStr, Field(..., description="Organization Api Token ID")], **kwargs) -> None:  # noqa: E501
        """Delete organization api token  # noqa: E501

        Delete organization api token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_organization_api_token(organization_id, api_token_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param api_token_id: Organization Api Token ID (required)
        :type api_token_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_organization_api_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_organization_api_token_with_http_info(organization_id, api_token_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_organization_api_token_with_http_info(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], api_token_id : Annotated[StrictStr, Field(..., description="Organization Api Token ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete organization api token  # noqa: E501

        Delete organization api token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_organization_api_token_with_http_info(organization_id, api_token_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param api_token_id: Organization Api Token ID (required)
        :type api_token_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'organization_id',
            'api_token_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_organization_api_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization_id']:
            _path_params['organizationId'] = _params['organization_id']

        if _params['api_token_id']:
            _path_params['apiTokenId'] = _params['api_token_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'bearerAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/organization/{organizationId}/apiToken/{apiTokenId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_organization_api_tokens(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], **kwargs) -> OrganizationApiTokenResponseList:  # noqa: E501
        """List organization api tokens  # noqa: E501

        List organization api tokens  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_organization_api_tokens(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: OrganizationApiTokenResponseList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_organization_api_tokens_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_organization_api_tokens_with_http_info(organization_id, **kwargs)  # noqa: E501

    @validate_arguments
    def list_organization_api_tokens_with_http_info(self, organization_id : Annotated[StrictStr, Field(..., description="Organization ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """List organization api tokens  # noqa: E501

        List organization api tokens  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_organization_api_tokens_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param organization_id: Organization ID (required)
        :type organization_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(OrganizationApiTokenResponseList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'organization_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_organization_api_tokens" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization_id']:
            _path_params['organizationId'] = _params['organization_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKeyAuth', 'bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "OrganizationApiTokenResponseList",
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/organization/{organizationId}/apiToken', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
