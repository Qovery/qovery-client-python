"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
from qovery.model.database_current_metric_response import DatabaseCurrentMetricResponse
from qovery.model.metric_cpu_datapoint_response_list import MetricCPUDatapointResponseList
from qovery.model.metric_generic_response_list import MetricGenericResponseList
from qovery.model.metric_memory_datapoint_response_list import MetricMemoryDatapointResponseList
from qovery.model.metric_restart_response import MetricRestartResponse
from qovery.model.metric_storage_datapoint_response_list import MetricStorageDatapointResponseList


class DatabaseMetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_database_current_metric_endpoint = _Endpoint(
            settings={
                'response_type': (DatabaseCurrentMetricResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/currentMetric',
                'operation_id': 'get_database_current_metric',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                },
                'location_map': {
                    'database_id': 'path',
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
        self.get_database_metric_cpu_endpoint = _Endpoint(
            settings={
                'response_type': (MetricCPUDatapointResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/metric/cpu',
                'operation_id': 'get_database_metric_cpu',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                    'last_seconds',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'database_id': 'path',
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
        self.get_database_metric_health_check_endpoint = _Endpoint(
            settings={
                'response_type': (MetricGenericResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/metric/healthCheck',
                'operation_id': 'get_database_metric_health_check',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                    'last_seconds',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'database_id': 'path',
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
        self.get_database_metric_memory_endpoint = _Endpoint(
            settings={
                'response_type': (MetricMemoryDatapointResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/metric/memory',
                'operation_id': 'get_database_metric_memory',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                    'last_seconds',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'database_id': 'path',
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
        self.get_database_metric_restart_endpoint = _Endpoint(
            settings={
                'response_type': (MetricRestartResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/metric/restart',
                'operation_id': 'get_database_metric_restart',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                    'last_seconds',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'database_id': 'path',
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
        self.get_database_metric_storage_endpoint = _Endpoint(
            settings={
                'response_type': (MetricStorageDatapointResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/database/{databaseId}/metric/storage',
                'operation_id': 'get_database_metric_storage',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'database_id',
                    'last_seconds',
                ],
                'required': [
                    'database_id',
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
                    'database_id':
                        (str,),
                    'last_seconds':
                        (float,),
                },
                'attribute_map': {
                    'database_id': 'databaseId',
                    'last_seconds': 'lastSeconds',
                },
                'location_map': {
                    'database_id': 'path',
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

    def get_database_current_metric(
        self,
        database_id,
        **kwargs
    ):
        """Get current metric consumption of the database   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_current_metric(database_id, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID

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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DatabaseCurrentMetricResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        return self.get_database_current_metric_endpoint.call_with_http_info(**kwargs)

    def get_database_metric_cpu(
        self,
        database_id,
        last_seconds,
        **kwargs
    ):
        """Get CPU consumption metric over time for the database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_metric_cpu(database_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricCPUDatapointResponseList
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_database_metric_cpu_endpoint.call_with_http_info(**kwargs)

    def get_database_metric_health_check(
        self,
        database_id,
        last_seconds,
        **kwargs
    ):
        """Get Health Check latency  metric over time for the database  # noqa: E501

        The value returned corresponds to the 95th centile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_metric_health_check(database_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_database_metric_health_check_endpoint.call_with_http_info(**kwargs)

    def get_database_metric_memory(
        self,
        database_id,
        last_seconds,
        **kwargs
    ):
        """Get Memory consumption metric over time for the database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_metric_memory(database_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricMemoryDatapointResponseList
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_database_metric_memory_endpoint.call_with_http_info(**kwargs)

    def get_database_metric_restart(
        self,
        database_id,
        last_seconds,
        **kwargs
    ):
        """List database restarts  # noqa: E501

        Get database restart message and timestamp.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_metric_restart(database_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricRestartResponse
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_database_metric_restart_endpoint.call_with_http_info(**kwargs)

    def get_database_metric_storage(
        self,
        database_id,
        last_seconds,
        **kwargs
    ):
        """Get Storage consumption metric over time for the database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_database_metric_storage(database_id, last_seconds, async_req=True)
        >>> result = thread.get()

        Args:
            database_id (str): Database ID
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricStorageDatapointResponseList
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['database_id'] = \
            database_id
        kwargs['last_seconds'] = \
            last_seconds
        return self.get_database_metric_storage_endpoint.call_with_http_info(**kwargs)

