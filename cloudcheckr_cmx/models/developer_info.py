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


class DeveloperInfo(object):
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
        'exception_type': 'str',
        'exception_message': 'str',
        'exception_full_stack': 'str'
    }

    attribute_map = {
        'exception_type': 'exceptionType',
        'exception_message': 'exceptionMessage',
        'exception_full_stack': 'exceptionFullStack'
    }

    def __init__(self, exception_type=None, exception_message=None, exception_full_stack=None):  # noqa: E501
        """DeveloperInfo - a model defined in Swagger"""  # noqa: E501

        self._exception_type = None
        self._exception_message = None
        self._exception_full_stack = None
        self.discriminator = None

        if exception_type is not None:
            self.exception_type = exception_type
        if exception_message is not None:
            self.exception_message = exception_message
        if exception_full_stack is not None:
            self.exception_full_stack = exception_full_stack

    @property
    def exception_type(self):
        """Gets the exception_type of this DeveloperInfo.  # noqa: E501


        :return: The exception_type of this DeveloperInfo.  # noqa: E501
        :rtype: str
        """
        return self._exception_type

    @exception_type.setter
    def exception_type(self, exception_type):
        """Sets the exception_type of this DeveloperInfo.


        :param exception_type: The exception_type of this DeveloperInfo.  # noqa: E501
        :type: str
        """

        self._exception_type = exception_type

    @property
    def exception_message(self):
        """Gets the exception_message of this DeveloperInfo.  # noqa: E501


        :return: The exception_message of this DeveloperInfo.  # noqa: E501
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """Sets the exception_message of this DeveloperInfo.


        :param exception_message: The exception_message of this DeveloperInfo.  # noqa: E501
        :type: str
        """

        self._exception_message = exception_message

    @property
    def exception_full_stack(self):
        """Gets the exception_full_stack of this DeveloperInfo.  # noqa: E501


        :return: The exception_full_stack of this DeveloperInfo.  # noqa: E501
        :rtype: str
        """
        return self._exception_full_stack

    @exception_full_stack.setter
    def exception_full_stack(self, exception_full_stack):
        """Sets the exception_full_stack of this DeveloperInfo.


        :param exception_full_stack: The exception_full_stack of this DeveloperInfo.  # noqa: E501
        :type: str
        """

        self._exception_full_stack = exception_full_stack

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
        if issubclass(DeveloperInfo, dict):
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
        if not isinstance(other, DeveloperInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
