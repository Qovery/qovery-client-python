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
from qovery.model.application_current_scale import ApplicationCurrentScale
from qovery.model.instance_response_list import InstanceResponseList
from qovery.model.metric_cpu_response_list import MetricCPUResponseList
from qovery.model.metric_generic_response_list import MetricGenericResponseList
from qovery.model.metric_memory_response_list import MetricMemoryResponseList
from qovery.model.metric_storage_response_list import MetricStorageResponseList
from qovery.model.storage_disk_response_list import StorageDiskResponseList


class ApplicationMetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_application_current_instance_endpoint = _Endpoint(
            settings={
                'response_type': (InstanceResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/instance',
                'operation_id': 'get_application_current_instance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                ],
                'required': [
                    'application_id',
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
                    'application_id':
                        (str,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                },
                'location_map': {
                    'application_id': 'path',
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
        self.get_application_current_scale_endpoint = _Endpoint(
            settings={
                'response_type': (ApplicationCurrentScale,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/currentScale',
                'operation_id': 'get_application_current_scale',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                ],
                'required': [
                    'application_id',
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
                    'application_id':
                        (str,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                },
                'location_map': {
                    'application_id': 'path',
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
        self.get_application_current_storage_disk_endpoint = _Endpoint(
            settings={
                'response_type': (StorageDiskResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/currentStorage',
                'operation_id': 'get_application_current_storage_disk',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                ],
                'required': [
                    'application_id',
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
                    'application_id':
                        (str,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                },
                'location_map': {
                    'application_id': 'path',
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
        self.get_application_metric_cpu_endpoint = _Endpoint(
            settings={
                'response_type': (MetricCPUResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/metric/cpu',
                'operation_id': 'get_application_metric_cpu',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                    'last_seconds',
                ],
                'required': [
                    'application_id',
                    'last_seconds',
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
                    'application_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'application_id': 'path',
                    'last_seconds': 'query',
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
        self.get_application_metric_health_check_endpoint = _Endpoint(
            settings={
                'response_type': (MetricGenericResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/metric/healthCheck',
                'operation_id': 'get_application_metric_health_check',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                    'last_seconds',
                ],
                'required': [
                    'application_id',
                    'last_seconds',
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
                    'application_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'application_id': 'path',
                    'last_seconds': 'query',
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
        self.get_application_metric_memory_endpoint = _Endpoint(
            settings={
                'response_type': (MetricMemoryResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/metric/memory',
                'operation_id': 'get_application_metric_memory',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                    'last_seconds',
                ],
                'required': [
                    'application_id',
                    'last_seconds',
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
                    'application_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'application_id': 'path',
                    'last_seconds': 'query',
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
        self.get_application_metric_storage_endpoint = _Endpoint(
            settings={
                'response_type': (MetricStorageResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/application/{applicationId}/metric/storage',
                'operation_id': 'get_application_metric_storage',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'application_id',
                    'last_seconds',
                ],
                'required': [
                    'application_id',
                    'last_seconds',
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
                    'application_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'application_id': 'applicationId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'application_id': 'path',
                    'last_seconds': 'query',
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

    def get_application_current_instance(
        self,
        application_id,
        **kwargs
    ):
        """List currently running instances of the application with their CPU and RAM metrics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_current_instance(application_id, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID

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
            InstanceResponseList
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
        kwargs['application_id'] = \
            application_id
        return self.get_application_current_instance_endpoint.call_with_http_info(**kwargs)

    def get_application_current_scale(
        self,
        application_id,
        **kwargs
    ):
        """Get current scaling of the application  # noqa: E501

        Returns min, max, and running number of instances of the application  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_current_scale(application_id, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID

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
            ApplicationCurrentScale
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
        kwargs['application_id'] = \
            application_id
        return self.get_application_current_scale_endpoint.call_with_http_info(**kwargs)

    def get_application_current_storage_disk(
        self,
        application_id,
        **kwargs
    ):
        """List current storage disk usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_current_storage_disk(application_id, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID

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
            StorageDiskResponseList
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
        kwargs['application_id'] = \
            application_id
        return self.get_application_current_storage_disk_endpoint.call_with_http_info(**kwargs)

    def get_application_metric_cpu(
        self,
        application_id,
        last_seconds,
        **kwargs
    ):
        """Get CPU consumption metric over time for the application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_metric_cpu(application_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID
            last_seconds (float): Up to how many seconds in the past to ask analytics results

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
            MetricCPUResponseList
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
        kwargs['application_id'] = \
            application_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_application_metric_cpu_endpoint.call_with_http_info(**kwargs)

    def get_application_metric_health_check(
        self,
        application_id,
        last_seconds,
        **kwargs
    ):
        """Get Health Check latency  metric over time for the application  # noqa: E501

        The value returned corresponds to the 95th centile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_metric_health_check(application_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID
            last_seconds (float): Up to how many seconds in the past to ask analytics results

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
            MetricGenericResponseList
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
        kwargs['application_id'] = \
            application_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_application_metric_health_check_endpoint.call_with_http_info(**kwargs)

    def get_application_metric_memory(
        self,
        application_id,
        last_seconds,
        **kwargs
    ):
        """Get Memory consumption metric over time for the application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_metric_memory(application_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID
            last_seconds (float): Up to how many seconds in the past to ask analytics results

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
            MetricMemoryResponseList
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
        kwargs['application_id'] = \
            application_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_application_metric_memory_endpoint.call_with_http_info(**kwargs)

    def get_application_metric_storage(
        self,
        application_id,
        last_seconds,
        **kwargs
    ):
        """Get Storage consumption metric over time for the application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_application_metric_storage(application_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            application_id (str): Application ID
            last_seconds (float): Up to how many seconds in the past to ask analytics results

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
            MetricStorageResponseList
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
        kwargs['application_id'] = \
            application_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_application_metric_storage_endpoint.call_with_http_info(**kwargs)

