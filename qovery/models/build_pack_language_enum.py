# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class BuildPackLanguageEnum(str, Enum):
    """
    Development language of the application
    """

    """
    allowed enum values
    """
    CLOJURE = 'CLOJURE'
    GO = 'GO'
    GRADLE = 'GRADLE'
    GRAILS = 'GRAILS'
    JAVA = 'JAVA'
    JVM = 'JVM'
    NODE_JS = 'NODE_JS'
    PHP = 'PHP'
    PLAY = 'PLAY'
    PYTHON = 'PYTHON'
    SCALA = 'SCALA'

    @classmethod
    def from_json(cls, json_str: str) -> BuildPackLanguageEnum:
        """Create an instance of BuildPackLanguageEnum from a JSON string"""
        return BuildPackLanguageEnum(json.loads(json_str))


