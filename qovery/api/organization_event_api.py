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
from qovery.model.organization_event_origin import OrganizationEventOrigin
from qovery.model.organization_event_response_list import OrganizationEventResponseList
from qovery.model.organization_event_sub_target_type import OrganizationEventSubTargetType
from qovery.model.organization_event_target_type import OrganizationEventTargetType
from qovery.model.organization_event_type import OrganizationEventType


class OrganizationEventApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_organization_events_endpoint = _Endpoint(
            settings={
                'response_type': (OrganizationEventResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/organization/{organizationId}/events',
                'operation_id': 'get_organization_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_id',
                    'page_size',
                    'from_timestamp',
                    'to_timestamp',
                    'continue_token',
                    'step_back_token',
                    'event_type',
                    'target_type',
                    'target_id',
                    'sub_target_type',
                    'triggered_by',
                    'origin',
                ],
                'required': [
                    'organization_id',
                ],
                'nullable': [
                    'page_size',
                    'from_timestamp',
                    'to_timestamp',
                    'target_id',
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
                    'page_size':
                        (float, none_type,),
                    'from_timestamp':
                        (str, none_type,),
                    'to_timestamp':
                        (str, none_type,),
                    'continue_token':
                        (str,),
                    'step_back_token':
                        (str,),
                    'event_type':
                        (OrganizationEventType,),
                    'target_type':
                        (OrganizationEventTargetType,),
                    'target_id':
                        (str, none_type,),
                    'sub_target_type':
                        (OrganizationEventSubTargetType,),
                    'triggered_by':
                        (str,),
                    'origin':
                        (OrganizationEventOrigin,),
                },
                'attribute_map': {
                    'organization_id': 'organizationId',
                    'page_size': 'pageSize',
                    'from_timestamp': 'fromTimestamp',
                    'to_timestamp': 'toTimestamp',
                    'continue_token': 'continueToken',
                    'step_back_token': 'stepBackToken',
                    'event_type': 'eventType',
                    'target_type': 'targetType',
                    'target_id': 'targetId',
                    'sub_target_type': 'subTargetType',
                    'triggered_by': 'triggeredBy',
                    'origin': 'origin',
                },
                'location_map': {
                    'organization_id': 'path',
                    'page_size': 'query',
                    'from_timestamp': 'query',
                    'to_timestamp': 'query',
                    'continue_token': 'query',
                    'step_back_token': 'query',
                    'event_type': 'query',
                    'target_type': 'query',
                    'target_id': 'query',
                    'sub_target_type': 'query',
                    'triggered_by': 'query',
                    'origin': 'query',
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

    def get_organization_events(
        self,
        organization_id,
        **kwargs
    ):
        """Get all events inside the organization  # noqa: E501

        Get all events inside the organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_organization_events(organization_id, async_req=True)
        >>> result = thread.get()

        Args:
            organization_id (str): Organization ID

        Keyword Args:
            page_size (float, none_type): The number of events to display in the current page. [optional] if omitted the server will use the default value of 10
            from_timestamp (str, none_type): Display events triggered since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp` The format is a timestamp with nano precision . [optional]
            to_timestamp (str, none_type): Display events triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp` The format is a timestamp with nano precision . [optional]
            continue_token (str): Token used to fetch the next page results The format is a timestamp with nano precision . [optional]
            step_back_token (str): Token used to fetch the previous page results The format is a timestamp with nano precision . [optional]
            event_type (OrganizationEventType): [optional]
            target_type (OrganizationEventTargetType): [optional]
            target_id (str, none_type): The target resource id to search.   Must be specified with the corresponding `target_type` . [optional]
            sub_target_type (OrganizationEventSubTargetType): [optional]
            triggered_by (str): Information about the owner of the event (user name / apitoken / automatic action). [optional]
            origin (OrganizationEventOrigin): [optional]
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
            OrganizationEventResponseList
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
        return self.get_organization_events_endpoint.call_with_http_info(**kwargs)

