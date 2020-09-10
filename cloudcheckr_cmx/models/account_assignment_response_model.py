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


class AccountAssignmentResponseModel(object):
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
        'new_parent_assignment': 'ParentAssignment',
        'id': 'str',
        'error': 'Error'
    }

    attribute_map = {
        'new_parent_assignment': 'newParentAssignment',
        'id': 'id',
        'error': 'error'
    }

    def __init__(self, new_parent_assignment=None, id=None, error=None):  # noqa: E501
        """AccountAssignmentResponseModel - a model defined in Swagger"""  # noqa: E501

        self._new_parent_assignment = None
        self._id = None
        self._error = None
        self.discriminator = None

        if new_parent_assignment is not None:
            self.new_parent_assignment = new_parent_assignment
        if id is not None:
            self.id = id
        if error is not None:
            self.error = error

    @property
    def new_parent_assignment(self):
        """Gets the new_parent_assignment of this AccountAssignmentResponseModel.  # noqa: E501

        The account's parent assignment.  # noqa: E501

        :return: The new_parent_assignment of this AccountAssignmentResponseModel.  # noqa: E501
        :rtype: ParentAssignment
        """
        return self._new_parent_assignment

    @new_parent_assignment.setter
    def new_parent_assignment(self, new_parent_assignment):
        """Sets the new_parent_assignment of this AccountAssignmentResponseModel.

        The account's parent assignment.  # noqa: E501

        :param new_parent_assignment: The new_parent_assignment of this AccountAssignmentResponseModel.  # noqa: E501
        :type: ParentAssignment
        """

        self._new_parent_assignment = new_parent_assignment

    @property
    def id(self):
        """Gets the id of this AccountAssignmentResponseModel.  # noqa: E501

        Assigned Id.  # noqa: E501

        :return: The id of this AccountAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountAssignmentResponseModel.

        Assigned Id.  # noqa: E501

        :param id: The id of this AccountAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def error(self):
        """Gets the error of this AccountAssignmentResponseModel.  # noqa: E501

        The errors that occurred during account assignment.  # noqa: E501

        :return: The error of this AccountAssignmentResponseModel.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AccountAssignmentResponseModel.

        The errors that occurred during account assignment.  # noqa: E501

        :param error: The error of this AccountAssignmentResponseModel.  # noqa: E501
        :type: Error
        """

        self._error = error

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
        if issubclass(AccountAssignmentResponseModel, dict):
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
        if not isinstance(other, AccountAssignmentResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
