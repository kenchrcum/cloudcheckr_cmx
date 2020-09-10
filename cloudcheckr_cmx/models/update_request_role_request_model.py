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


class UpdateRequestRoleRequestModel(object):
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
        'item': 'RoleRequestModel',
        'reset_properties': 'list[str]'
    }

    attribute_map = {
        'item': 'item',
        'reset_properties': 'resetProperties'
    }

    def __init__(self, item=None, reset_properties=None):  # noqa: E501
        """UpdateRequestRoleRequestModel - a model defined in Swagger"""  # noqa: E501

        self._item = None
        self._reset_properties = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if reset_properties is not None:
            self.reset_properties = reset_properties

    @property
    def item(self):
        """Gets the item of this UpdateRequestRoleRequestModel.  # noqa: E501

        Item to update  # noqa: E501

        :return: The item of this UpdateRequestRoleRequestModel.  # noqa: E501
        :rtype: RoleRequestModel
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this UpdateRequestRoleRequestModel.

        Item to update  # noqa: E501

        :param item: The item of this UpdateRequestRoleRequestModel.  # noqa: E501
        :type: RoleRequestModel
        """

        self._item = item

    @property
    def reset_properties(self):
        """Gets the reset_properties of this UpdateRequestRoleRequestModel.  # noqa: E501

        If a property name is included in this list, then its value will be forced to its default value (default value may be null).  # noqa: E501

        :return: The reset_properties of this UpdateRequestRoleRequestModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._reset_properties

    @reset_properties.setter
    def reset_properties(self, reset_properties):
        """Sets the reset_properties of this UpdateRequestRoleRequestModel.

        If a property name is included in this list, then its value will be forced to its default value (default value may be null).  # noqa: E501

        :param reset_properties: The reset_properties of this UpdateRequestRoleRequestModel.  # noqa: E501
        :type: list[str]
        """

        self._reset_properties = reset_properties

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
        if issubclass(UpdateRequestRoleRequestModel, dict):
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
        if not isinstance(other, UpdateRequestRoleRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
