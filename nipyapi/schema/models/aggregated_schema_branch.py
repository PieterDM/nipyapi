# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AggregatedSchemaBranch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'schema_branch': 'SchemaBranch',
        'root_schema_version': 'int',
        'schema_version_infos': 'list[SchemaVersionInfo]'
    }

    attribute_map = {
        'schema_branch': 'schemaBranch',
        'root_schema_version': 'rootSchemaVersion',
        'schema_version_infos': 'schemaVersionInfos'
    }

    def __init__(self, schema_branch=None, root_schema_version=None, schema_version_infos=None):
        """
        AggregatedSchemaBranch - a model defined in Swagger
        """

        self._schema_branch = None
        self._root_schema_version = None
        self._schema_version_infos = None

        if schema_branch is not None:
          self.schema_branch = schema_branch
        if root_schema_version is not None:
          self.root_schema_version = root_schema_version
        if schema_version_infos is not None:
          self.schema_version_infos = schema_version_infos

    @property
    def schema_branch(self):
        """
        Gets the schema_branch of this AggregatedSchemaBranch.

        :return: The schema_branch of this AggregatedSchemaBranch.
        :rtype: SchemaBranch
        """
        return self._schema_branch

    @schema_branch.setter
    def schema_branch(self, schema_branch):
        """
        Sets the schema_branch of this AggregatedSchemaBranch.

        :param schema_branch: The schema_branch of this AggregatedSchemaBranch.
        :type: SchemaBranch
        """

        self._schema_branch = schema_branch

    @property
    def root_schema_version(self):
        """
        Gets the root_schema_version of this AggregatedSchemaBranch.

        :return: The root_schema_version of this AggregatedSchemaBranch.
        :rtype: int
        """
        return self._root_schema_version

    @root_schema_version.setter
    def root_schema_version(self, root_schema_version):
        """
        Sets the root_schema_version of this AggregatedSchemaBranch.

        :param root_schema_version: The root_schema_version of this AggregatedSchemaBranch.
        :type: int
        """

        self._root_schema_version = root_schema_version

    @property
    def schema_version_infos(self):
        """
        Gets the schema_version_infos of this AggregatedSchemaBranch.

        :return: The schema_version_infos of this AggregatedSchemaBranch.
        :rtype: list[SchemaVersionInfo]
        """
        return self._schema_version_infos

    @schema_version_infos.setter
    def schema_version_infos(self, schema_version_infos):
        """
        Sets the schema_version_infos of this AggregatedSchemaBranch.

        :param schema_version_infos: The schema_version_infos of this AggregatedSchemaBranch.
        :type: list[SchemaVersionInfo]
        """

        self._schema_version_infos = schema_version_infos

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AggregatedSchemaBranch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
