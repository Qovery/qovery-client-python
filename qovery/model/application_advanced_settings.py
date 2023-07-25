"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from qovery.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from qovery.exceptions import ApiAttributeError



class ApplicationAdvancedSettings(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('deployment_update_strategy_type',): {
            'ROLLINGUPDATE': "RollingUpdate",
            'RECREATE': "Recreate",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'deployment_delay_start_time_sec': (int,),  # noqa: E501
            'deployment_custom_domain_check_enabled': (bool,),  # noqa: E501
            'deployment_termination_grace_period_seconds': (int,),  # noqa: E501
            'deployment_update_strategy_type': (str,),  # noqa: E501
            'deployment_update_strategy_rolling_update_max_unavailable_percent': (int,),  # noqa: E501
            'deployment_update_strategy_rolling_update_max_surge_percent': (int,),  # noqa: E501
            'build_timeout_max_sec': (int,),  # noqa: E501
            'build_cpu_max_in_milli': (int,),  # noqa: E501
            'build_ram_max_in_gib': (int,),  # noqa: E501
            'network_ingress_proxy_body_size_mb': (int,),  # noqa: E501
            'network_ingress_enable_cors': (bool,),  # noqa: E501
            'network_ingress_cors_allow_origin': (str,),  # noqa: E501
            'network_ingress_cors_allow_methods': (str,),  # noqa: E501
            'network_ingress_cors_allow_headers': (str,),  # noqa: E501
            'network_ingress_proxy_buffer_size_kb': (int,),  # noqa: E501
            'network_ingress_keepalive_time_seconds': (int,),  # noqa: E501
            'network_ingress_keepalive_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_send_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_proxy_connect_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_proxy_send_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_proxy_read_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_whitelist_source_range': (str,),  # noqa: E501
            'network_ingress_denylist_source_range': (str,),  # noqa: E501
            'network_ingress_basic_auth_env_var': (str,),  # noqa: E501
            'network_ingress_enable_sticky_session': (bool,),  # noqa: E501
            'network_ingress_grpc_send_timeout_seconds': (int,),  # noqa: E501
            'network_ingress_grpc_read_timeout_seconds': (int,),  # noqa: E501
            'hpa_cpu_average_utilization_percent': (int,),  # noqa: E501
            'security_service_account_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'deployment_delay_start_time_sec': 'deployment.delay_start_time_sec',  # noqa: E501
        'deployment_custom_domain_check_enabled': 'deployment.custom_domain_check_enabled',  # noqa: E501
        'deployment_termination_grace_period_seconds': 'deployment.termination_grace_period_seconds',  # noqa: E501
        'deployment_update_strategy_type': 'deployment.update_strategy.type',  # noqa: E501
        'deployment_update_strategy_rolling_update_max_unavailable_percent': 'deployment.update_strategy.rolling_update.max_unavailable_percent',  # noqa: E501
        'deployment_update_strategy_rolling_update_max_surge_percent': 'deployment.update_strategy.rolling_update.max_surge_percent',  # noqa: E501
        'build_timeout_max_sec': 'build.timeout_max_sec',  # noqa: E501
        'build_cpu_max_in_milli': 'build.cpu_max_in_milli',  # noqa: E501
        'build_ram_max_in_gib': 'build.ram_max_in_gib',  # noqa: E501
        'network_ingress_proxy_body_size_mb': 'network.ingress.proxy_body_size_mb',  # noqa: E501
        'network_ingress_enable_cors': 'network.ingress.enable_cors',  # noqa: E501
        'network_ingress_cors_allow_origin': 'network.ingress.cors_allow_origin',  # noqa: E501
        'network_ingress_cors_allow_methods': 'network.ingress.cors_allow_methods',  # noqa: E501
        'network_ingress_cors_allow_headers': 'network.ingress.cors_allow_headers',  # noqa: E501
        'network_ingress_proxy_buffer_size_kb': 'network.ingress.proxy_buffer_size_kb',  # noqa: E501
        'network_ingress_keepalive_time_seconds': 'network.ingress.keepalive_time_seconds',  # noqa: E501
        'network_ingress_keepalive_timeout_seconds': 'network.ingress.keepalive_timeout_seconds',  # noqa: E501
        'network_ingress_send_timeout_seconds': 'network.ingress.send_timeout_seconds',  # noqa: E501
        'network_ingress_proxy_connect_timeout_seconds': 'network.ingress.proxy_connect_timeout_seconds',  # noqa: E501
        'network_ingress_proxy_send_timeout_seconds': 'network.ingress.proxy_send_timeout_seconds',  # noqa: E501
        'network_ingress_proxy_read_timeout_seconds': 'network.ingress.proxy_read_timeout_seconds',  # noqa: E501
        'network_ingress_whitelist_source_range': 'network.ingress.whitelist_source_range',  # noqa: E501
        'network_ingress_denylist_source_range': 'network.ingress.denylist_source_range',  # noqa: E501
        'network_ingress_basic_auth_env_var': 'network.ingress.basic_auth_env_var',  # noqa: E501
        'network_ingress_enable_sticky_session': 'network.ingress.enable_sticky_session',  # noqa: E501
        'network_ingress_grpc_send_timeout_seconds': 'network.ingress.grpc_send_timeout_seconds',  # noqa: E501
        'network_ingress_grpc_read_timeout_seconds': 'network.ingress.grpc_read_timeout_seconds',  # noqa: E501
        'hpa_cpu_average_utilization_percent': 'hpa.cpu.average_utilization_percent',  # noqa: E501
        'security_service_account_name': 'security.service_account_name',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ApplicationAdvancedSettings - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            deployment_delay_start_time_sec (int): please use `readiness_probe.initial_delay_seconds` and `liveness_probe.initial_delay_seconds` instead. [optional] if omitted the server will use the default value of 30  # noqa: E501
            deployment_custom_domain_check_enabled (bool): disable custom domain check when deploying an application. [optional] if omitted the server will use the default value of True  # noqa: E501
            deployment_termination_grace_period_seconds (int): define how long in seconds an application is supposed to be stopped gracefully. [optional] if omitted the server will use the default value of 60  # noqa: E501
            deployment_update_strategy_type (str): * `RollingUpdate` gracefully rollout new versions, and automatically rollback if the new version fails to start * `Recreate` stop all current versions and create new ones once all old ones have been shutdown . [optional] if omitted the server will use the default value of "RollingUpdate"  # noqa: E501
            deployment_update_strategy_rolling_update_max_unavailable_percent (int): Define the percentage of a maximum number of pods that can be unavailable during the update process. [optional] if omitted the server will use the default value of 25  # noqa: E501
            deployment_update_strategy_rolling_update_max_surge_percent (int): Define the percentage of the maximum number of pods that can be created over the desired number of pods. [optional] if omitted the server will use the default value of 25  # noqa: E501
            build_timeout_max_sec (int): [optional] if omitted the server will use the default value of 1800  # noqa: E501
            build_cpu_max_in_milli (int): define the max cpu resources (in milli). [optional] if omitted the server will use the default value of 4000  # noqa: E501
            build_ram_max_in_gib (int): define the max ram resources (in gib). [optional] if omitted the server will use the default value of 8  # noqa: E501
            network_ingress_proxy_body_size_mb (int): [optional] if omitted the server will use the default value of 100  # noqa: E501
            network_ingress_enable_cors (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            network_ingress_cors_allow_origin (str): [optional] if omitted the server will use the default value of "*"  # noqa: E501
            network_ingress_cors_allow_methods (str): [optional] if omitted the server will use the default value of "GET, PUT, POST, DELETE, PATCH, OPTIONS"  # noqa: E501
            network_ingress_cors_allow_headers (str): [optional] if omitted the server will use the default value of "DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization"  # noqa: E501
            network_ingress_proxy_buffer_size_kb (int): header buffer size used while reading response header from upstream. [optional] if omitted the server will use the default value of 4  # noqa: E501
            network_ingress_keepalive_time_seconds (int): Limits the maximum time (in seconds) during which requests can be processed through one keepalive connection. [optional] if omitted the server will use the default value of 3600  # noqa: E501
            network_ingress_keepalive_timeout_seconds (int): Sets a timeout (in seconds) during which an idle keepalive connection to an upstream server will stay open.. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a response to the client. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_connect_timeout_seconds (int): Sets a timeout (in seconds) for establishing a connection to a proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_read_timeout_seconds (int): Sets a timeout (in seconds) for reading a response from the proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_whitelist_source_range (str): list of source ranges to allow access to ingress proxy.  This property can be used to whitelist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 To allow all source ranges, set 0.0.0.0/0. . [optional] if omitted the server will use the default value of "0.0.0.0/0"  # noqa: E501
            network_ingress_denylist_source_range (str): list of source ranges to deny access to ingress proxy.  This property can be used to blacklist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 . [optional] if omitted the server will use the default value of ""  # noqa: E501
            network_ingress_basic_auth_env_var (str): Set the name of an environment variable to use as a basic authentication (`login:crypted_password`) from `htpasswd` command. . [optional] if omitted the server will use the default value of ""  # noqa: E501
            network_ingress_enable_sticky_session (bool): Enable the load balancer to bind a user's session to a specific target. This ensures that all requests from the user during the session are sent to the same target . [optional] if omitted the server will use the default value of False  # noqa: E501
            network_ingress_grpc_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the grpc server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_grpc_read_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the grpc server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            hpa_cpu_average_utilization_percent (int): Percentage value of cpu usage at which point pods should scale up.. [optional] if omitted the server will use the default value of 60  # noqa: E501
            security_service_account_name (str): Allows you to set an existing Kubernetes service account name . [optional] if omitted the server will use the default value of ""  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ApplicationAdvancedSettings - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            deployment_delay_start_time_sec (int): please use `readiness_probe.initial_delay_seconds` and `liveness_probe.initial_delay_seconds` instead. [optional] if omitted the server will use the default value of 30  # noqa: E501
            deployment_custom_domain_check_enabled (bool): disable custom domain check when deploying an application. [optional] if omitted the server will use the default value of True  # noqa: E501
            deployment_termination_grace_period_seconds (int): define how long in seconds an application is supposed to be stopped gracefully. [optional] if omitted the server will use the default value of 60  # noqa: E501
            deployment_update_strategy_type (str): * `RollingUpdate` gracefully rollout new versions, and automatically rollback if the new version fails to start * `Recreate` stop all current versions and create new ones once all old ones have been shutdown . [optional] if omitted the server will use the default value of "RollingUpdate"  # noqa: E501
            deployment_update_strategy_rolling_update_max_unavailable_percent (int): Define the percentage of a maximum number of pods that can be unavailable during the update process. [optional] if omitted the server will use the default value of 25  # noqa: E501
            deployment_update_strategy_rolling_update_max_surge_percent (int): Define the percentage of the maximum number of pods that can be created over the desired number of pods. [optional] if omitted the server will use the default value of 25  # noqa: E501
            build_timeout_max_sec (int): [optional] if omitted the server will use the default value of 1800  # noqa: E501
            build_cpu_max_in_milli (int): define the max cpu resources (in milli). [optional] if omitted the server will use the default value of 4000  # noqa: E501
            build_ram_max_in_gib (int): define the max ram resources (in gib). [optional] if omitted the server will use the default value of 8  # noqa: E501
            network_ingress_proxy_body_size_mb (int): [optional] if omitted the server will use the default value of 100  # noqa: E501
            network_ingress_enable_cors (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            network_ingress_cors_allow_origin (str): [optional] if omitted the server will use the default value of "*"  # noqa: E501
            network_ingress_cors_allow_methods (str): [optional] if omitted the server will use the default value of "GET, PUT, POST, DELETE, PATCH, OPTIONS"  # noqa: E501
            network_ingress_cors_allow_headers (str): [optional] if omitted the server will use the default value of "DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization"  # noqa: E501
            network_ingress_proxy_buffer_size_kb (int): header buffer size used while reading response header from upstream. [optional] if omitted the server will use the default value of 4  # noqa: E501
            network_ingress_keepalive_time_seconds (int): Limits the maximum time (in seconds) during which requests can be processed through one keepalive connection. [optional] if omitted the server will use the default value of 3600  # noqa: E501
            network_ingress_keepalive_timeout_seconds (int): Sets a timeout (in seconds) during which an idle keepalive connection to an upstream server will stay open.. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a response to the client. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_connect_timeout_seconds (int): Sets a timeout (in seconds) for establishing a connection to a proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_proxy_read_timeout_seconds (int): Sets a timeout (in seconds) for reading a response from the proxied server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_whitelist_source_range (str): list of source ranges to allow access to ingress proxy.  This property can be used to whitelist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 To allow all source ranges, set 0.0.0.0/0. . [optional] if omitted the server will use the default value of "0.0.0.0/0"  # noqa: E501
            network_ingress_denylist_source_range (str): list of source ranges to deny access to ingress proxy.  This property can be used to blacklist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 . [optional] if omitted the server will use the default value of ""  # noqa: E501
            network_ingress_basic_auth_env_var (str): Set the name of an environment variable to use as a basic authentication (`login:crypted_password`) from `htpasswd` command. . [optional] if omitted the server will use the default value of ""  # noqa: E501
            network_ingress_enable_sticky_session (bool): Enable the load balancer to bind a user's session to a specific target. This ensures that all requests from the user during the session are sent to the same target . [optional] if omitted the server will use the default value of False  # noqa: E501
            network_ingress_grpc_send_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the grpc server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            network_ingress_grpc_read_timeout_seconds (int): Sets a timeout (in seconds) for transmitting a request to the grpc server. [optional] if omitted the server will use the default value of 60  # noqa: E501
            hpa_cpu_average_utilization_percent (int): Percentage value of cpu usage at which point pods should scale up.. [optional] if omitted the server will use the default value of 60  # noqa: E501
            security_service_account_name (str): Allows you to set an existing Kubernetes service account name . [optional] if omitted the server will use the default value of ""  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
