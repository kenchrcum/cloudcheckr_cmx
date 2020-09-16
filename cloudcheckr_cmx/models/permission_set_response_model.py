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

class PermissionSetResponseModel(object):
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
        'friendly_name': 'str',
        'owned_by': 'str',
        'description': 'str',
        'permissions': 'list[PermissionSetPermissionModel]',
        'created_date': 'datetime',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'friendly_name': 'friendlyName',
        'owned_by': 'ownedBy',
        'description': 'description',
        'permissions': 'permissions',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate'
    }

    def __init__(self, id=None, name=None, friendly_name=None, owned_by=None, description=None, permissions=None, created_date=None, updated_date=None):  # noqa: E501
        """PermissionSetResponseModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._friendly_name = None
        self._owned_by = None
        self._description = None
        self._permissions = None
        self._created_date = None
        self._updated_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if owned_by is not None:
            self.owned_by = owned_by
        if description is not None:
            self.description = description
        if permissions is not None:
            self.permissions = permissions
        if created_date is not None:
            self.created_date = created_date
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def id(self):
        """Gets the id of this PermissionSetResponseModel.  # noqa: E501

        The permission set's ID.  # noqa: E501

        :return: The id of this PermissionSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PermissionSetResponseModel.

        The permission set's ID.  # noqa: E501

        :param id: The id of this PermissionSetResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PermissionSetResponseModel.  # noqa: E501

        The permission set's name. This property supports: sorting.  # noqa: E501

        :return: The name of this PermissionSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionSetResponseModel.

        The permission set's name. This property supports: sorting.  # noqa: E501

        :param name: The name of this PermissionSetResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def friendly_name(self):
        """Gets the friendly_name of this PermissionSetResponseModel.  # noqa: E501

        The permission set's friendly name (obsolete).  # noqa: E501

        :return: The friendly_name of this PermissionSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this PermissionSetResponseModel.

        The permission set's friendly name (obsolete).  # noqa: E501

        :param friendly_name: The friendly_name of this PermissionSetResponseModel.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def owned_by(self):
        """Gets the owned_by of this PermissionSetResponseModel.  # noqa: E501

        The owner of the permission set.  # noqa: E501

        :return: The owned_by of this PermissionSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this PermissionSetResponseModel.

        The owner of the permission set.  # noqa: E501

        :param owned_by: The owned_by of this PermissionSetResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["All", "System", "Customer"]  # noqa: E501
        if owned_by not in allowed_values:
            raise ValueError(
                "Invalid value for `owned_by` ({0}), must be one of {1}"  # noqa: E501
                .format(owned_by, allowed_values)
            )

        self._owned_by = owned_by

    @property
    def description(self):
        """Gets the description of this PermissionSetResponseModel.  # noqa: E501

        The permission set's description.  # noqa: E501

        :return: The description of this PermissionSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionSetResponseModel.

        The permission set's description.  # noqa: E501

        :param description: The description of this PermissionSetResponseModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """Gets the permissions of this PermissionSetResponseModel.  # noqa: E501

        The permission set's permissions.  # noqa: E501

        :return: The permissions of this PermissionSetResponseModel.  # noqa: E501
        :rtype: list[PermissionSetPermissionModel]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this PermissionSetResponseModel.

        The permission set's permissions.  # noqa: E501

        :param permissions: The permissions of this PermissionSetResponseModel.  # noqa: E501
        :type: list[PermissionSetPermissionModel]
        """

        self._permissions = permissions

    @property
    def created_date(self):
        """Gets the created_date of this PermissionSetResponseModel.  # noqa: E501

        The permission set's creation date.  # noqa: E501

        :return: The created_date of this PermissionSetResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this PermissionSetResponseModel.

        The permission set's creation date.  # noqa: E501

        :param created_date: The created_date of this PermissionSetResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this PermissionSetResponseModel.  # noqa: E501

        The permission set's last updated date.  # noqa: E501

        :return: The updated_date of this PermissionSetResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this PermissionSetResponseModel.

        The permission set's last updated date.  # noqa: E501

        :param updated_date: The updated_date of this PermissionSetResponseModel.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(PermissionSetResponseModel, dict):
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
        if not isinstance(other, PermissionSetResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
