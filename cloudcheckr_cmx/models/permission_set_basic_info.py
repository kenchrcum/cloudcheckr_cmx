# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PermissionSetBasicInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'name': 'str',
        'is_missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_missing': 'isMissing'
    }

    def __init__(self, id=None, name=None, is_missing=None):  # noqa: E501
        """PermissionSetBasicInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_missing = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_missing is not None:
            self.is_missing = is_missing

    @property
    def id(self):
        """Gets the id of this PermissionSetBasicInfo.  # noqa: E501

        The permission set's ID.  # noqa: E501

        :return: The id of this PermissionSetBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PermissionSetBasicInfo.

        The permission set's ID.  # noqa: E501

        :param id: The id of this PermissionSetBasicInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PermissionSetBasicInfo.  # noqa: E501

        The permission set's name.  # noqa: E501

        :return: The name of this PermissionSetBasicInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionSetBasicInfo.

        The permission set's name.  # noqa: E501

        :param name: The name of this PermissionSetBasicInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_missing(self):
        """Gets the is_missing of this PermissionSetBasicInfo.  # noqa: E501

        Determines if the permission set is missing.  # noqa: E501

        :return: The is_missing of this PermissionSetBasicInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_missing

    @is_missing.setter
    def is_missing(self, is_missing):
        """Sets the is_missing of this PermissionSetBasicInfo.

        Determines if the permission set is missing.  # noqa: E501

        :param is_missing: The is_missing of this PermissionSetBasicInfo.  # noqa: E501
        :type: bool
        """

        self._is_missing = is_missing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PermissionSetBasicInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PermissionSetBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
