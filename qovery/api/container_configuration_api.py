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

from qovery.models.container_advanced_settings import ContainerAdvancedSettings
from qovery.models.container_network import ContainerNetwork
from qovery.models.container_network_request import ContainerNetworkRequest

from qovery.api_client import ApiClient
from qovery.api_response import ApiResponse
from qovery.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContainerConfigurationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def edit_container_advanced_settings(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], container_advanced_settings : Optional[ContainerAdvancedSettings] = None, **kwargs) -> ContainerAdvancedSettings:  # noqa: E501
        """Edit advanced settings  # noqa: E501

        Edit advanced settings by returning table of advanced settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_container_advanced_settings(container_id, container_advanced_settings, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param container_advanced_settings:
        :type container_advanced_settings: ContainerAdvancedSettings
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ContainerAdvancedSettings
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the edit_container_advanced_settings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.edit_container_advanced_settings_with_http_info(container_id, container_advanced_settings, **kwargs)  # noqa: E501

    @validate_arguments
    def edit_container_advanced_settings_with_http_info(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], container_advanced_settings : Optional[ContainerAdvancedSettings] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Edit advanced settings  # noqa: E501

        Edit advanced settings by returning table of advanced settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_container_advanced_settings_with_http_info(container_id, container_advanced_settings, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param container_advanced_settings:
        :type container_advanced_settings: ContainerAdvancedSettings
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
        :rtype: tuple(ContainerAdvancedSettings, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'container_id',
            'container_advanced_settings'
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
                    " to method edit_container_advanced_settings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['container_id']:
            _path_params['containerId'] = _params['container_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['container_advanced_settings'] is not None:
            _body_params = _params['container_advanced_settings']

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
            '201': "ContainerAdvancedSettings",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/container/{containerId}/advancedSettings', 'PUT',
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
    def edit_container_network(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], container_network_request : Optional[ContainerNetworkRequest] = None, **kwargs) -> ContainerNetwork:  # noqa: E501
        """Edit Container Network  # noqa: E501

        Edit the Network settings of the container.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_container_network(container_id, container_network_request, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param container_network_request:
        :type container_network_request: ContainerNetworkRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ContainerNetwork
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the edit_container_network_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.edit_container_network_with_http_info(container_id, container_network_request, **kwargs)  # noqa: E501

    @validate_arguments
    def edit_container_network_with_http_info(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], container_network_request : Optional[ContainerNetworkRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Edit Container Network  # noqa: E501

        Edit the Network settings of the container.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_container_network_with_http_info(container_id, container_network_request, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param container_network_request:
        :type container_network_request: ContainerNetworkRequest
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
        :rtype: tuple(ContainerNetwork, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'container_id',
            'container_network_request'
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
                    " to method edit_container_network" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['container_id']:
            _path_params['containerId'] = _params['container_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['container_network_request'] is not None:
            _body_params = _params['container_network_request']

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
            '201': "ContainerNetwork",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/container/{containerId}/network', 'PUT',
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
    def get_container_advanced_settings(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], **kwargs) -> ContainerAdvancedSettings:  # noqa: E501
        """Get advanced settings  # noqa: E501

        Get list and values of the advanced settings of the container. Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/advanced-settings/)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_container_advanced_settings(container_id, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ContainerAdvancedSettings
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_container_advanced_settings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_container_advanced_settings_with_http_info(container_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_container_advanced_settings_with_http_info(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get advanced settings  # noqa: E501

        Get list and values of the advanced settings of the container. Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/advanced-settings/)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_container_advanced_settings_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
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
        :rtype: tuple(ContainerAdvancedSettings, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'container_id'
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
                    " to method get_container_advanced_settings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['container_id']:
            _path_params['containerId'] = _params['container_id']


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
            '200': "ContainerAdvancedSettings",
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/container/{containerId}/advancedSettings', 'GET',
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
    def get_container_network(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], **kwargs) -> ContainerNetwork:  # noqa: E501
        """Get Container Network information  # noqa: E501

        Get status of the container network settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_container_network(container_id, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ContainerNetwork
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_container_network_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_container_network_with_http_info(container_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_container_network_with_http_info(self, container_id : Annotated[StrictStr, Field(..., description="Container ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Container Network information  # noqa: E501

        Get status of the container network settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_container_network_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param container_id: Container ID (required)
        :type container_id: str
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
        :rtype: tuple(ContainerNetwork, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'container_id'
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
                    " to method get_container_network" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['container_id']:
            _path_params['containerId'] = _params['container_id']


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
            '200': "ContainerNetwork",
            '401': None,
            '403': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/container/{containerId}/network', 'GET',
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
