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
from qovery.model.key import Key
from qovery.model.secret_edit_request import SecretEditRequest
from qovery.model.secret_request import SecretRequest
from qovery.model.secret_response import SecretResponse
from qovery.model.secret_response_list import SecretResponseList
from qovery.model.value import Value


class EnvironmentSecretApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_environment_secret_endpoint = _Endpoint(
            settings={
                'response_type': (SecretResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret',
                'operation_id': 'create_environment_secret',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'secret_request',
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
                    'secret_request':
                        (SecretRequest,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'secret_request': 'body',
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
        self.create_environment_secret_alias_endpoint = _Endpoint(
            settings={
                'response_type': (SecretResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret/{secretId}/alias',
                'operation_id': 'create_environment_secret_alias',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'secret_id',
                    'key',
                ],
                'required': [
                    'environment_id',
                    'secret_id',
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
                    'secret_id':
                        (str,),
                    'key':
                        (Key,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                    'secret_id': 'secretId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'secret_id': 'path',
                    'key': 'body',
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
        self.create_environment_secret_override_endpoint = _Endpoint(
            settings={
                'response_type': (SecretResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret/{secretId}/override',
                'operation_id': 'create_environment_secret_override',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'secret_id',
                    'value',
                ],
                'required': [
                    'environment_id',
                    'secret_id',
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
                    'secret_id':
                        (str,),
                    'value':
                        (Value,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                    'secret_id': 'secretId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'secret_id': 'path',
                    'value': 'body',
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
        self.edit_environment_secret_endpoint = _Endpoint(
            settings={
                'response_type': (SecretResponse,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret/{secretId}',
                'operation_id': 'edit_environment_secret',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'secret_id',
                    'secret_edit_request',
                ],
                'required': [
                    'environment_id',
                    'secret_id',
                    'secret_edit_request',
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
                    'secret_id':
                        (str,),
                    'secret_edit_request':
                        (SecretEditRequest,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                    'secret_id': 'secretId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'secret_id': 'path',
                    'secret_edit_request': 'body',
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
        self.environment_environment_id_secret_secret_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret/{secretId}',
                'operation_id': 'environment_environment_id_secret_secret_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'environment_id',
                    'secret_id',
                ],
                'required': [
                    'environment_id',
                    'secret_id',
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
                    'secret_id':
                        (str,),
                },
                'attribute_map': {
                    'environment_id': 'environmentId',
                    'secret_id': 'secretId',
                },
                'location_map': {
                    'environment_id': 'path',
                    'secret_id': 'path',
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
        self.list_environment_secrets_endpoint = _Endpoint(
            settings={
                'response_type': (SecretResponseList,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/environment/{environmentId}/secret',
                'operation_id': 'list_environment_secrets',
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

    def create_environment_secret(
        self,
        environment_id,
        **kwargs
    ):
        """Add a secret to the environment  # noqa: E501

        - Add a secret to the environment.   - If the secret key already exists, then it will be replaced by the new one.   - If the secret value points toward an existing secret key, it will be considered as an alias.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_environment_secret(environment_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID

        Keyword Args:
            secret_request (SecretRequest): [optional]
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
            SecretResponse
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
        kwargs['environment_id'] = \
            environment_id
        return self.create_environment_secret_endpoint.call_with_http_info(**kwargs)

    def create_environment_secret_alias(
        self,
        environment_id,
        secret_id,
        **kwargs
    ):
        """Create a secret alias at the environment level  # noqa: E501

        - Allows you to add an alias at environment level on an existing secret having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new secret at environment level with the same value as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the aliased_secret will be exposed in the \"aliased_secret\" field of the newly created secret - Only 1 alias level is allowed. You can't create an alias on an alias   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_environment_secret_alias(environment_id, secret_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID
            secret_id (str): Secret ID

        Keyword Args:
            key (Key): [optional]
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
            SecretResponse
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
        kwargs['environment_id'] = \
            environment_id
        kwargs['secret_id'] = \
            secret_id
        return self.create_environment_secret_alias_endpoint.call_with_http_info(**kwargs)

    def create_environment_secret_override(
        self,
        environment_id,
        secret_id,
        **kwargs
    ):
        """Create a secret override at the environment level  # noqa: E501

        - Allows you to override at environment level a secret that has a higher scope. - You only have to specify a value in the request body - The system will create a new secret at environment level with the same key as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the overridden_secret will be exposed in the \"overridden_secret\" field of the newly created secret   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_environment_secret_override(environment_id, secret_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID
            secret_id (str): Secret ID

        Keyword Args:
            value (Value): [optional]
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
            SecretResponse
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
        kwargs['environment_id'] = \
            environment_id
        kwargs['secret_id'] = \
            secret_id
        return self.create_environment_secret_override_endpoint.call_with_http_info(**kwargs)

    def edit_environment_secret(
        self,
        environment_id,
        secret_id,
        secret_edit_request,
        **kwargs
    ):
        """Edit a secret belonging to the environment  # noqa: E501

        - You can't edit a BUILT_IN secret - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the secret it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_environment_secret(environment_id, secret_id, secret_edit_request, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID
            secret_id (str): Secret ID
            secret_edit_request (SecretEditRequest):

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
            SecretResponse
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
        kwargs['environment_id'] = \
            environment_id
        kwargs['secret_id'] = \
            secret_id
        kwargs['secret_edit_request'] = \
            secret_edit_request
        return self.edit_environment_secret_endpoint.call_with_http_info(**kwargs)

    def environment_environment_id_secret_secret_id_delete(
        self,
        environment_id,
        secret_id,
        **kwargs
    ):
        """Delete a secret from the environment  # noqa: E501

        - To delete a secret you must have the project user permission - You can't delete a BUILT_IN secret - If you delete a secret having override or alias, the associated override/alias will be deleted as well  operationId: deleteEnvironmentSecret   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.environment_environment_id_secret_secret_id_delete(environment_id, secret_id, async_req=True)
        >>> result = thread.get()

        Args:
            environment_id (str): Environment ID
            secret_id (str): Secret ID

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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['environment_id'] = \
            environment_id
        kwargs['secret_id'] = \
            secret_id
        return self.environment_environment_id_secret_secret_id_delete_endpoint.call_with_http_info(**kwargs)

    def list_environment_secrets(
        self,
        environment_id,
        **kwargs
    ):
        """List environment secrets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_environment_secrets(environment_id, async_req=True)
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SecretResponseList
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
        kwargs['environment_id'] = \
            environment_id
        return self.list_environment_secrets_endpoint.call_with_http_info(**kwargs)

