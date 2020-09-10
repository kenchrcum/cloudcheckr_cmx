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


class AncestorsResponseModel(object):
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
        'ancestors': 'list[AncestorModel]'
    }

    attribute_map = {
        'ancestors': 'ancestors'
    }

    def __init__(self, ancestors=None):  # noqa: E501
        """AncestorsResponseModel - a model defined in Swagger"""  # noqa: E501

        self._ancestors = None
        self.discriminator = None

        if ancestors is not None:
            self.ancestors = ancestors

    @property
    def ancestors(self):
        """Gets the ancestors of this AncestorsResponseModel.  # noqa: E501

        The account's ancestors (in order, with immediate parent first).  # noqa: E501

        :return: The ancestors of this AncestorsResponseModel.  # noqa: E501
        :rtype: list[AncestorModel]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """Sets the ancestors of this AncestorsResponseModel.

        The account's ancestors (in order, with immediate parent first).  # noqa: E501

        :param ancestors: The ancestors of this AncestorsResponseModel.  # noqa: E501
        :type: list[AncestorModel]
        """

        self._ancestors = ancestors

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
        if issubclass(AncestorsResponseModel, dict):
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
        if not isinstance(other, AncestorsResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
