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
    from qovery.model.application_edit_request_all_of import ApplicationEditRequestAllOf
    from qovery.model.application_git_repository_request import ApplicationGitRepositoryRequest
    from qovery.model.build_mode_enum import BuildModeEnum
    from qovery.model.build_pack_language_enum import BuildPackLanguageEnum
    from qovery.model.healthcheck import Healthcheck
    from qovery.model.service_port_response_list import ServicePortResponseList
    from qovery.model.service_storage_request import ServiceStorageRequest
    from qovery.model.service_storage_request_storage_inner import ServiceStorageRequestStorageInner
    globals()['ApplicationEditRequestAllOf'] = ApplicationEditRequestAllOf
    globals()['ApplicationGitRepositoryRequest'] = ApplicationGitRepositoryRequest
    globals()['BuildModeEnum'] = BuildModeEnum
    globals()['BuildPackLanguageEnum'] = BuildPackLanguageEnum
    globals()['Healthcheck'] = Healthcheck
    globals()['ServicePortResponseList'] = ServicePortResponseList
    globals()['ServiceStorageRequest'] = ServiceStorageRequest
    globals()['ServiceStorageRequestStorageInner'] = ServiceStorageRequestStorageInner


class ApplicationEditRequest(ModelComposed):
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
            'storage': ([ServiceStorageRequestStorageInner],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'git_repository': (ApplicationGitRepositoryRequest,),  # noqa: E501
            'build_mode': (BuildModeEnum,),  # noqa: E501
            'dockerfile_path': (str,),  # noqa: E501
            'buildpack_language': (BuildPackLanguageEnum,),  # noqa: E501
            'cpu': (int,),  # noqa: E501
            'memory': (int,),  # noqa: E501
            'min_running_instances': (int,),  # noqa: E501
            'max_running_instances': (int,),  # noqa: E501
            'healthchecks': (Healthcheck,),  # noqa: E501
            'auto_preview': (bool,),  # noqa: E501
            'ports': (ServicePortResponseList,),  # noqa: E501
            'arguments': ([str],),  # noqa: E501
            'entrypoint': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'storage': 'storage',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'git_repository': 'git_repository',  # noqa: E501
        'build_mode': 'build_mode',  # noqa: E501
        'dockerfile_path': 'dockerfile_path',  # noqa: E501
        'buildpack_language': 'buildpack_language',  # noqa: E501
        'cpu': 'cpu',  # noqa: E501
        'memory': 'memory',  # noqa: E501
        'min_running_instances': 'min_running_instances',  # noqa: E501
        'max_running_instances': 'max_running_instances',  # noqa: E501
        'healthchecks': 'healthchecks',  # noqa: E501
        'auto_preview': 'auto_preview',  # noqa: E501
        'ports': 'ports',  # noqa: E501
        'arguments': 'arguments',  # noqa: E501
        'entrypoint': 'entrypoint',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ApplicationEditRequest - a model defined in OpenAPI

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
            storage ([ServiceStorageRequestStorageInner]): [optional]  # noqa: E501
            name (str): name is case insensitive. [optional]  # noqa: E501
            description (str): give a description to this application. [optional]  # noqa: E501
            git_repository (ApplicationGitRepositoryRequest): [optional]  # noqa: E501
            build_mode (BuildModeEnum): [optional]  # noqa: E501
            dockerfile_path (str): The path of the associated Dockerfile. [optional]  # noqa: E501
            buildpack_language (BuildPackLanguageEnum): [optional]  # noqa: E501
            cpu (int): unit is millicores (m). 1000m = 1 cpu. [optional] if omitted the server will use the default value of 500  # noqa: E501
            memory (int): unit is MB. 1024 MB = 1GB. [optional] if omitted the server will use the default value of 512  # noqa: E501
            min_running_instances (int): Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running. . [optional] if omitted the server will use the default value of 1  # noqa: E501
            max_running_instances (int): Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit. . [optional] if omitted the server will use the default value of 1  # noqa: E501
            healthchecks (Healthcheck): [optional]  # noqa: E501
            auto_preview (bool): Specify if the environment preview option is activated or not for this application.   If activated, a preview environment will be automatically cloned at each pull request.   If not specified, it takes the value of the `auto_preview` property from the associated environment. . [optional] if omitted the server will use the default value of True  # noqa: E501
            ports (ServicePortResponseList): [optional]  # noqa: E501
            arguments ([str]): [optional]  # noqa: E501
            entrypoint (str): optional entrypoint when launching container. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ApplicationEditRequest - a model defined in OpenAPI

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
            storage ([ServiceStorageRequestStorageInner]): [optional]  # noqa: E501
            name (str): name is case insensitive. [optional]  # noqa: E501
            description (str): give a description to this application. [optional]  # noqa: E501
            git_repository (ApplicationGitRepositoryRequest): [optional]  # noqa: E501
            build_mode (BuildModeEnum): [optional]  # noqa: E501
            dockerfile_path (str): The path of the associated Dockerfile. [optional]  # noqa: E501
            buildpack_language (BuildPackLanguageEnum): [optional]  # noqa: E501
            cpu (int): unit is millicores (m). 1000m = 1 cpu. [optional] if omitted the server will use the default value of 500  # noqa: E501
            memory (int): unit is MB. 1024 MB = 1GB. [optional] if omitted the server will use the default value of 512  # noqa: E501
            min_running_instances (int): Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running. . [optional] if omitted the server will use the default value of 1  # noqa: E501
            max_running_instances (int): Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit. . [optional] if omitted the server will use the default value of 1  # noqa: E501
            healthchecks (Healthcheck): [optional]  # noqa: E501
            auto_preview (bool): Specify if the environment preview option is activated or not for this application.   If activated, a preview environment will be automatically cloned at each pull request.   If not specified, it takes the value of the `auto_preview` property from the associated environment. . [optional] if omitted the server will use the default value of True  # noqa: E501
            ports (ServicePortResponseList): [optional]  # noqa: E501
            arguments ([str]): [optional]  # noqa: E501
            entrypoint (str): optional entrypoint when launching container. [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              ApplicationEditRequestAllOf,
              ServiceStorageRequest,
          ],
          'oneOf': [
          ],
        }
