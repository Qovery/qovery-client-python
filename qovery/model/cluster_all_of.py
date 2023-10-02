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
    from qovery.model.cloud_provider_enum import CloudProviderEnum
    from qovery.model.cluster_deployment_status_enum import ClusterDeploymentStatusEnum
    from qovery.model.cluster_feature import ClusterFeature
    from qovery.model.cluster_state_enum import ClusterStateEnum
    from qovery.model.kubernetes_enum import KubernetesEnum
    globals()['CloudProviderEnum'] = CloudProviderEnum
    globals()['ClusterDeploymentStatusEnum'] = ClusterDeploymentStatusEnum
    globals()['ClusterFeature'] = ClusterFeature
    globals()['ClusterStateEnum'] = ClusterStateEnum
    globals()['KubernetesEnum'] = KubernetesEnum


class ClusterAllOf(ModelNormal):
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
            'name': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'cloud_provider': (CloudProviderEnum,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'min_running_nodes': (int,),  # noqa: E501
            'max_running_nodes': (int,),  # noqa: E501
            'disk_size': (int,),  # noqa: E501
            'instance_type': (str,),  # noqa: E501
            'kubernetes': (KubernetesEnum,),  # noqa: E501
            'cpu': (int,),  # noqa: E501
            'memory': (int,),  # noqa: E501
            'estimated_cloud_provider_cost': (int,),  # noqa: E501
            'status': (ClusterStateEnum,),  # noqa: E501
            'has_access': (bool,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'is_default': (bool,),  # noqa: E501
            'production': (bool,),  # noqa: E501
            'ssh_keys': ([str],),  # noqa: E501
            'features': ([ClusterFeature],),  # noqa: E501
            'deployment_status': (ClusterDeploymentStatusEnum,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'region': 'region',  # noqa: E501
        'cloud_provider': 'cloud_provider',  # noqa: E501
        'description': 'description',  # noqa: E501
        'min_running_nodes': 'min_running_nodes',  # noqa: E501
        'max_running_nodes': 'max_running_nodes',  # noqa: E501
        'disk_size': 'disk_size',  # noqa: E501
        'instance_type': 'instance_type',  # noqa: E501
        'kubernetes': 'kubernetes',  # noqa: E501
        'cpu': 'cpu',  # noqa: E501
        'memory': 'memory',  # noqa: E501
        'estimated_cloud_provider_cost': 'estimated_cloud_provider_cost',  # noqa: E501
        'status': 'status',  # noqa: E501
        'has_access': 'has_access',  # noqa: E501
        'version': 'version',  # noqa: E501
        'is_default': 'is_default',  # noqa: E501
        'production': 'production',  # noqa: E501
        'ssh_keys': 'ssh_keys',  # noqa: E501
        'features': 'features',  # noqa: E501
        'deployment_status': 'deployment_status',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, region, cloud_provider, *args, **kwargs):  # noqa: E501
        """ClusterAllOf - a model defined in OpenAPI

        Args:
            name (str): name is case-insensitive
            region (str):
            cloud_provider (CloudProviderEnum):

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
            description (str): [optional]  # noqa: E501
            min_running_nodes (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            max_running_nodes (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            disk_size (int): Unit is in GB. The disk size to be used for the node configuration. [optional] if omitted the server will use the default value of 20  # noqa: E501
            instance_type (str): the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType. [optional]  # noqa: E501
            kubernetes (KubernetesEnum): [optional]  # noqa: E501
            cpu (int): unit is millicores (m). 1000m = 1 cpu. [optional]  # noqa: E501
            memory (int): unit is MB. 1024 MB = 1GB. [optional]  # noqa: E501
            estimated_cloud_provider_cost (int): This is an estimation of the cost this cluster will represent on your cloud proider bill, based on your current configuration. [optional]  # noqa: E501
            status (ClusterStateEnum): [optional]  # noqa: E501
            has_access (bool): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            is_default (bool): [optional]  # noqa: E501
            production (bool): specific flag to indicate that this cluster is a production one. [optional]  # noqa: E501
            ssh_keys ([str]): Indicate your public ssh_key to remotely connect to your EC2 instance.. [optional]  # noqa: E501
            features ([ClusterFeature]): [optional]  # noqa: E501
            deployment_status (ClusterDeploymentStatusEnum): [optional]  # noqa: E501
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

        self.name = name
        self.region = region
        self.cloud_provider = cloud_provider
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
    def __init__(self, name, region, cloud_provider, *args, **kwargs):  # noqa: E501
        """ClusterAllOf - a model defined in OpenAPI

        Args:
            name (str): name is case-insensitive
            region (str):
            cloud_provider (CloudProviderEnum):

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
            description (str): [optional]  # noqa: E501
            min_running_nodes (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            max_running_nodes (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            disk_size (int): Unit is in GB. The disk size to be used for the node configuration. [optional] if omitted the server will use the default value of 20  # noqa: E501
            instance_type (str): the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType. [optional]  # noqa: E501
            kubernetes (KubernetesEnum): [optional]  # noqa: E501
            cpu (int): unit is millicores (m). 1000m = 1 cpu. [optional]  # noqa: E501
            memory (int): unit is MB. 1024 MB = 1GB. [optional]  # noqa: E501
            estimated_cloud_provider_cost (int): This is an estimation of the cost this cluster will represent on your cloud proider bill, based on your current configuration. [optional]  # noqa: E501
            status (ClusterStateEnum): [optional]  # noqa: E501
            has_access (bool): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            is_default (bool): [optional]  # noqa: E501
            production (bool): specific flag to indicate that this cluster is a production one. [optional]  # noqa: E501
            ssh_keys ([str]): Indicate your public ssh_key to remotely connect to your EC2 instance.. [optional]  # noqa: E501
            features ([ClusterFeature]): [optional]  # noqa: E501
            deployment_status (ClusterDeploymentStatusEnum): [optional]  # noqa: E501
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

        self.name = name
        self.region = region
        self.cloud_provider = cloud_provider
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
