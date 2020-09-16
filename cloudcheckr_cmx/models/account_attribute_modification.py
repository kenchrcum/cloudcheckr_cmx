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

class AccountAttributeModification(object):
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
        'name': 'str',
        'value': 'str',
        'action': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'action': 'action'
    }

    def __init__(self, name=None, value=None, action=None):  # noqa: E501
        """AccountAttributeModification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self._action = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if action is not None:
            self.action = action

    @property
    def name(self):
        """Gets the name of this AccountAttributeModification.  # noqa: E501

        Attribute's name.  # noqa: E501

        :return: The name of this AccountAttributeModification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountAttributeModification.

        Attribute's name.  # noqa: E501

        :param name: The name of this AccountAttributeModification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this AccountAttributeModification.  # noqa: E501

        Attribute's value.  # noqa: E501

        :return: The value of this AccountAttributeModification.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AccountAttributeModification.

        Attribute's value.  # noqa: E501

        :param value: The value of this AccountAttributeModification.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def action(self):
        """Gets the action of this AccountAttributeModification.  # noqa: E501

        Request list modification (e.g. add to the list).  # noqa: E501

        :return: The action of this AccountAttributeModification.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AccountAttributeModification.

        Request list modification (e.g. add to the list).  # noqa: E501

        :param action: The action of this AccountAttributeModification.  # noqa: E501
        :type: str
        """
        allowed_values = ["Add", "Remove"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

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
        if issubclass(AccountAttributeModification, dict):
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
        if not isinstance(other, AccountAttributeModification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
