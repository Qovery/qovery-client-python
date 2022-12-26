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


def lazy_import():
    from qovery.model.reference_object import ReferenceObject
    from qovery.model.service_port_response_list import ServicePortResponseList
    globals()['ReferenceObject'] = ReferenceObject
    globals()['ServicePortResponseList'] = ServicePortResponseList


class ContainerResponseAllOf(ModelNormal):
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
    }

    validations = {
        ('min_running_instances',): {
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'environment': (ReferenceObject,),  # noqa: E501
            'registry': (ReferenceObject,),  # noqa: E501
            'maximum_cpu': (int,),  # noqa: E501
            'maximum_memory': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'image_name': (str,),  # noqa: E501
            'tag': (str,),  # noqa: E501
            'cpu': (int,),  # noqa: E501
            'memory': (int,),  # noqa: E501
            'min_running_instances': (int,),  # noqa: E501
            'max_running_instances': (int,),  # noqa: E501
            'auto_preview': (bool,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'arguments': ([str],),  # noqa: E501
            'entrypoint': (str,),  # noqa: E501
            'ports': (ServicePortResponseList,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'environment': 'environment',  # noqa: E501
        'registry': 'registry',  # noqa: E501
        'maximum_cpu': 'maximum_cpu',  # noqa: E501
        'maximum_memory': 'maximum_memory',  # noqa: E501
        'name': 'name',  # noqa: E501
        'image_name': 'image_name',  # noqa: E501
        'tag': 'tag',  # noqa: E501
        'cpu': 'cpu',  # noqa: E501
        'memory': 'memory',  # noqa: E501
        'min_running_instances': 'min_running_instances',  # noqa: E501
        'max_running_instances': 'max_running_instances',  # noqa: E501
        'auto_preview': 'auto_preview',  # noqa: E501
        'description': 'description',  # noqa: E501
        'arguments': 'arguments',  # noqa: E501
        'entrypoint': 'entrypoint',  # noqa: E501
        'ports': 'ports',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, environment, registry, maximum_cpu, maximum_memory, name, image_name, tag, cpu, memory, auto_preview, *args, **kwargs):  # noqa: E501
        """ContainerResponseAllOf - a model defined in OpenAPI

        Args:
            environment (ReferenceObject):
            registry (ReferenceObject):
            maximum_cpu (int): Maximum cpu that can be allocated to the container based on organization cluster configuration. unit is millicores (m). 1000m = 1 cpu
            maximum_memory (int): Maximum memory that can be allocated to the container based on organization cluster configuration. unit is MB. 1024 MB = 1GB
            name (str): name is case insensitive
            image_name (str): name of the image container
            tag (str): tag of the image container
            cpu (int): unit is millicores (m). 1000m = 1 cpu
            memory (int): unit is MB. 1024 MB = 1GB
            auto_preview (bool): Indicates if the 'environment preview option' is enabled for this container.   If enabled, a preview environment will be automatically cloned when `/preview` endpoint is called.   If not specified, it takes the value of the `auto_preview` property from the associated environment. 

        Keyword Args:
            min_running_instances (int): Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running. . defaults to 1  # noqa: E501
            max_running_instances (int): Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit. . defaults to 1  # noqa: E501
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
            description (str): give a description to this container. [optional]  # noqa: E501
            arguments ([str]): [optional]  # noqa: E501
            entrypoint (str): optional entrypoint when launching container. [optional]  # noqa: E501
            ports (ServicePortResponseList): [optional]  # noqa: E501
        """

        min_running_instances = kwargs.get('min_running_instances', 1)
        max_running_instances = kwargs.get('max_running_instances', 1)
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

        self.environment = environment
        self.registry = registry
        self.maximum_cpu = maximum_cpu
        self.maximum_memory = maximum_memory
        self.name = name
        self.image_name = image_name
        self.tag = tag
        self.cpu = cpu
        self.memory = memory
        self.min_running_instances = min_running_instances
        self.max_running_instances = max_running_instances
        self.auto_preview = auto_preview
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
    def __init__(self, environment, registry, maximum_cpu, maximum_memory, name, image_name, tag, cpu, memory, auto_preview, *args, **kwargs):  # noqa: E501
        """ContainerResponseAllOf - a model defined in OpenAPI

        Args:
            environment (ReferenceObject):
            registry (ReferenceObject):
            maximum_cpu (int): Maximum cpu that can be allocated to the container based on organization cluster configuration. unit is millicores (m). 1000m = 1 cpu
            maximum_memory (int): Maximum memory that can be allocated to the container based on organization cluster configuration. unit is MB. 1024 MB = 1GB
            name (str): name is case insensitive
            image_name (str): name of the image container
            tag (str): tag of the image container
            cpu (int): unit is millicores (m). 1000m = 1 cpu
            memory (int): unit is MB. 1024 MB = 1GB
            auto_preview (bool): Indicates if the 'environment preview option' is enabled for this container.   If enabled, a preview environment will be automatically cloned when `/preview` endpoint is called.   If not specified, it takes the value of the `auto_preview` property from the associated environment. 

        Keyword Args:
            min_running_instances (int): Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running. . defaults to 1  # noqa: E501
            max_running_instances (int): Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit. . defaults to 1  # noqa: E501
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
            description (str): give a description to this container. [optional]  # noqa: E501
            arguments ([str]): [optional]  # noqa: E501
            entrypoint (str): optional entrypoint when launching container. [optional]  # noqa: E501
            ports (ServicePortResponseList): [optional]  # noqa: E501
        """

        min_running_instances = kwargs.get('min_running_instances', 1)
        max_running_instances = kwargs.get('max_running_instances', 1)
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

        self.environment = environment
        self.registry = registry
        self.maximum_cpu = maximum_cpu
        self.maximum_memory = maximum_memory
        self.name = name
        self.image_name = image_name
        self.tag = tag
        self.cpu = cpu
        self.memory = memory
        self.min_running_instances = min_running_instances
        self.max_running_instances = max_running_instances
        self.auto_preview = auto_preview
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
