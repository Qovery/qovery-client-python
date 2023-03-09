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



class ClusterAdvancedSettings(ModelNormal):
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
            'aws_cloudwatch_eks_logs_retention_days': (int,),  # noqa: E501
            'aws_vpc_enable_s3_flow_logs': (bool,),  # noqa: E501
            'aws_vpc_flow_logs_retention_days': (int,),  # noqa: E501
            'database_postgresql_deny_public_access': (bool,),  # noqa: E501
            'database_postgresql_allowed_cidrs': ([str],),  # noqa: E501
            'database_mysql_deny_public_access': (bool,),  # noqa: E501
            'database_mysql_allowed_cidrs': ([str],),  # noqa: E501
            'database_mongodb_deny_public_access': (bool,),  # noqa: E501
            'database_mongodb_allowed_cidrs': ([str],),  # noqa: E501
            'database_redis_deny_public_access': (bool,),  # noqa: E501
            'database_redis_allowed_cidrs': ([str],),  # noqa: E501
            'registry_image_retention_time': (int,),  # noqa: E501
            'loki_log_retention_in_week': (int,),  # noqa: E501
            'cloud_provider_container_registry_tags': ({str: (str,)},),  # noqa: E501
            'load_balancer_size': (str,),  # noqa: E501
            'pleco_resources_ttl': (int,),  # noqa: E501
            'aws_iam_admin_group': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'aws_cloudwatch_eks_logs_retention_days': 'aws.cloudwatch.eks_logs_retention_days',  # noqa: E501
        'aws_vpc_enable_s3_flow_logs': 'aws.vpc.enable_s3_flow_logs',  # noqa: E501
        'aws_vpc_flow_logs_retention_days': 'aws.vpc.flow_logs_retention_days',  # noqa: E501
        'database_postgresql_deny_public_access': 'database.postgresql.deny_public_access',  # noqa: E501
        'database_postgresql_allowed_cidrs': 'database.postgresql.allowed_cidrs',  # noqa: E501
        'database_mysql_deny_public_access': 'database.mysql.deny_public_access',  # noqa: E501
        'database_mysql_allowed_cidrs': 'database.mysql.allowed_cidrs',  # noqa: E501
        'database_mongodb_deny_public_access': 'database.mongodb.deny_public_access',  # noqa: E501
        'database_mongodb_allowed_cidrs': 'database.mongodb.allowed_cidrs',  # noqa: E501
        'database_redis_deny_public_access': 'database.redis.deny_public_access',  # noqa: E501
        'database_redis_allowed_cidrs': 'database.redis.allowed_cidrs',  # noqa: E501
        'registry_image_retention_time': 'registry.image_retention_time',  # noqa: E501
        'loki_log_retention_in_week': 'loki.log_retention_in_week',  # noqa: E501
        'cloud_provider_container_registry_tags': 'cloud_provider_container_registry_tags',  # noqa: E501
        'load_balancer_size': 'load_balancer.size',  # noqa: E501
        'pleco_resources_ttl': 'pleco.resources_ttl',  # noqa: E501
        'aws_iam_admin_group': 'aws.iam.admin_group',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ClusterAdvancedSettings - a model defined in OpenAPI

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
            aws_cloudwatch_eks_logs_retention_days (int): Set the number of retention days for EKS Cloudwatch logs. [optional] if omitted the server will use the default value of 90  # noqa: E501
            aws_vpc_enable_s3_flow_logs (bool): Enable flow logs for on the VPC and store them in an S3 bucket. [optional] if omitted the server will use the default value of False  # noqa: E501
            aws_vpc_flow_logs_retention_days (int): Set the number of retention days for flow logs. Disable with value \"0\". [optional] if omitted the server will use the default value of 365  # noqa: E501
            database_postgresql_deny_public_access (bool): Deny public access to any PostgreSQL database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_postgresql_allowed_cidrs ([str]): List of CIDRs allowed to access the PostgreSQL database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_mysql_deny_public_access (bool): Deny public access to any MySql database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_mysql_allowed_cidrs ([str]): List of CIDRs allowed to access the MySql database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_mongodb_deny_public_access (bool): Deny public access to any MongoDB/DocumentDB database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_mongodb_allowed_cidrs ([str]): List of CIDRs allowed to access the MongoDB/DocumentDB database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_redis_deny_public_access (bool): Deny public access to any Redis database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_redis_allowed_cidrs ([str]): List of CIDRs allowed to access the Redis database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            registry_image_retention_time (int): Configure the number of seconds before cleaning images in the registry. [optional] if omitted the server will use the default value of 31536000  # noqa: E501
            loki_log_retention_in_week (int): For how long in week loki is going to keep logs of your applications. [optional] if omitted the server will use the default value of 12  # noqa: E501
            cloud_provider_container_registry_tags ({str: (str,)}): Add additional tags on the cluster dedicated registry. [optional]  # noqa: E501
            load_balancer_size (str): Select the size of the main load_balancer (only effective for Scaleway). [optional] if omitted the server will use the default value of "lb-s"  # noqa: E501
            pleco_resources_ttl (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            aws_iam_admin_group (str): AWS IAM group name with cluster access. [optional] if omitted the server will use the default value of "Admins"  # noqa: E501
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
        """ClusterAdvancedSettings - a model defined in OpenAPI

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
            aws_cloudwatch_eks_logs_retention_days (int): Set the number of retention days for EKS Cloudwatch logs. [optional] if omitted the server will use the default value of 90  # noqa: E501
            aws_vpc_enable_s3_flow_logs (bool): Enable flow logs for on the VPC and store them in an S3 bucket. [optional] if omitted the server will use the default value of False  # noqa: E501
            aws_vpc_flow_logs_retention_days (int): Set the number of retention days for flow logs. Disable with value \"0\". [optional] if omitted the server will use the default value of 365  # noqa: E501
            database_postgresql_deny_public_access (bool): Deny public access to any PostgreSQL database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_postgresql_allowed_cidrs ([str]): List of CIDRs allowed to access the PostgreSQL database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_mysql_deny_public_access (bool): Deny public access to any MySql database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_mysql_allowed_cidrs ([str]): List of CIDRs allowed to access the MySql database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_mongodb_deny_public_access (bool): Deny public access to any MongoDB/DocumentDB database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_mongodb_allowed_cidrs ([str]): List of CIDRs allowed to access the MongoDB/DocumentDB database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            database_redis_deny_public_access (bool): Deny public access to any Redis database. [optional] if omitted the server will use the default value of False  # noqa: E501
            database_redis_allowed_cidrs ([str]): List of CIDRs allowed to access the Redis database. [optional] if omitted the server will use the default value of ["0.0.0.0/0"]  # noqa: E501
            registry_image_retention_time (int): Configure the number of seconds before cleaning images in the registry. [optional] if omitted the server will use the default value of 31536000  # noqa: E501
            loki_log_retention_in_week (int): For how long in week loki is going to keep logs of your applications. [optional] if omitted the server will use the default value of 12  # noqa: E501
            cloud_provider_container_registry_tags ({str: (str,)}): Add additional tags on the cluster dedicated registry. [optional]  # noqa: E501
            load_balancer_size (str): Select the size of the main load_balancer (only effective for Scaleway). [optional] if omitted the server will use the default value of "lb-s"  # noqa: E501
            pleco_resources_ttl (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            aws_iam_admin_group (str): AWS IAM group name with cluster access. [optional] if omitted the server will use the default value of "Admins"  # noqa: E501
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
