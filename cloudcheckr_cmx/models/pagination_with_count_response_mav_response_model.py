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


class PaginationWithCountResponseMavResponseModel(object):
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
        'total_count': 'int',
        'items': 'list[MavResponseModel]',
        'pagination': 'PaginationInfo'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'items': 'items',
        'pagination': 'pagination'
    }

    def __init__(self, total_count=None, items=None, pagination=None):  # noqa: E501
        """PaginationWithCountResponseMavResponseModel - a model defined in Swagger"""  # noqa: E501

        self._total_count = None
        self._items = None
        self._pagination = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if items is not None:
            self.items = items
        if pagination is not None:
            self.pagination = pagination

    @property
    def total_count(self):
        """Gets the total_count of this PaginationWithCountResponseMavResponseModel.  # noqa: E501

        The total amount of results before pagination has occurred.  # noqa: E501

        :return: The total_count of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginationWithCountResponseMavResponseModel.

        The total amount of results before pagination has occurred.  # noqa: E501

        :param total_count: The total_count of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def items(self):
        """Gets the items of this PaginationWithCountResponseMavResponseModel.  # noqa: E501

        Items for this page.  # noqa: E501

        :return: The items of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :rtype: list[MavResponseModel]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PaginationWithCountResponseMavResponseModel.

        Items for this page.  # noqa: E501

        :param items: The items of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :type: list[MavResponseModel]
        """

        self._items = items

    @property
    def pagination(self):
        """Gets the pagination of this PaginationWithCountResponseMavResponseModel.  # noqa: E501

        Key information required to request other pages of data.  Will be null / absent if there is only one page.  # noqa: E501

        :return: The pagination of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :rtype: PaginationInfo
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PaginationWithCountResponseMavResponseModel.

        Key information required to request other pages of data.  Will be null / absent if there is only one page.  # noqa: E501

        :param pagination: The pagination of this PaginationWithCountResponseMavResponseModel.  # noqa: E501
        :type: PaginationInfo
        """

        self._pagination = pagination

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
        if issubclass(PaginationWithCountResponseMavResponseModel, dict):
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
        if not isinstance(other, PaginationWithCountResponseMavResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
