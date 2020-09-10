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


class RoleResponseModel(object):
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
        'description': 'str',
        'customer_account_access_rule': 'str',
        'permission_sets': 'list[PermissionSetBasicInfo]',
        'customer_accounts': 'list[CustomerAccountBasicInfo]',
        'created_date': 'datetime',
        'updated_date': 'datetime',
        'owned_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'customer_account_access_rule': 'customerAccountAccessRule',
        'permission_sets': 'permissionSets',
        'customer_accounts': 'customerAccounts',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate',
        'owned_by': 'ownedBy'
    }

    def __init__(self, id=None, name=None, description=None, customer_account_access_rule=None, permission_sets=None, customer_accounts=None, created_date=None, updated_date=None, owned_by=None):  # noqa: E501
        """RoleResponseModel - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._customer_account_access_rule = None
        self._permission_sets = None
        self._customer_accounts = None
        self._created_date = None
        self._updated_date = None
        self._owned_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if customer_account_access_rule is not None:
            self.customer_account_access_rule = customer_account_access_rule
        if permission_sets is not None:
            self.permission_sets = permission_sets
        if customer_accounts is not None:
            self.customer_accounts = customer_accounts
        if created_date is not None:
            self.created_date = created_date
        if updated_date is not None:
            self.updated_date = updated_date
        if owned_by is not None:
            self.owned_by = owned_by

    @property
    def id(self):
        """Gets the id of this RoleResponseModel.  # noqa: E501

        The role's ID.  # noqa: E501

        :return: The id of this RoleResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleResponseModel.

        The role's ID.  # noqa: E501

        :param id: The id of this RoleResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RoleResponseModel.  # noqa: E501

        The role's name. This property supports: sorting.  # noqa: E501

        :return: The name of this RoleResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleResponseModel.

        The role's name. This property supports: sorting.  # noqa: E501

        :param name: The name of this RoleResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleResponseModel.  # noqa: E501

        The role's description.  # noqa: E501

        :return: The description of this RoleResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleResponseModel.

        The role's description.  # noqa: E501

        :param description: The description of this RoleResponseModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer_account_access_rule(self):
        """Gets the customer_account_access_rule of this RoleResponseModel.  # noqa: E501

        The role's access rule. This controls how customer and account access is determined.  # noqa: E501

        :return: The customer_account_access_rule of this RoleResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._customer_account_access_rule

    @customer_account_access_rule.setter
    def customer_account_access_rule(self, customer_account_access_rule):
        """Sets the customer_account_access_rule of this RoleResponseModel.

        The role's access rule. This controls how customer and account access is determined.  # noqa: E501

        :param customer_account_access_rule: The customer_account_access_rule of this RoleResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["SpecifiedCustomersAndAccountsOnly", "OwnCustomerAndAllAccounts"]  # noqa: E501
        if customer_account_access_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `customer_account_access_rule` ({0}), must be one of {1}"  # noqa: E501
                .format(customer_account_access_rule, allowed_values)
            )

        self._customer_account_access_rule = customer_account_access_rule

    @property
    def permission_sets(self):
        """Gets the permission_sets of this RoleResponseModel.  # noqa: E501

        The role's permission sets.  # noqa: E501

        :return: The permission_sets of this RoleResponseModel.  # noqa: E501
        :rtype: list[PermissionSetBasicInfo]
        """
        return self._permission_sets

    @permission_sets.setter
    def permission_sets(self, permission_sets):
        """Sets the permission_sets of this RoleResponseModel.

        The role's permission sets.  # noqa: E501

        :param permission_sets: The permission_sets of this RoleResponseModel.  # noqa: E501
        :type: list[PermissionSetBasicInfo]
        """

        self._permission_sets = permission_sets

    @property
    def customer_accounts(self):
        """Gets the customer_accounts of this RoleResponseModel.  # noqa: E501

        The customers and/or accounts to which the role grants access.  # noqa: E501

        :return: The customer_accounts of this RoleResponseModel.  # noqa: E501
        :rtype: list[CustomerAccountBasicInfo]
        """
        return self._customer_accounts

    @customer_accounts.setter
    def customer_accounts(self, customer_accounts):
        """Sets the customer_accounts of this RoleResponseModel.

        The customers and/or accounts to which the role grants access.  # noqa: E501

        :param customer_accounts: The customer_accounts of this RoleResponseModel.  # noqa: E501
        :type: list[CustomerAccountBasicInfo]
        """

        self._customer_accounts = customer_accounts

    @property
    def created_date(self):
        """Gets the created_date of this RoleResponseModel.  # noqa: E501

        The role's creation date.  # noqa: E501

        :return: The created_date of this RoleResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RoleResponseModel.

        The role's creation date.  # noqa: E501

        :param created_date: The created_date of this RoleResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this RoleResponseModel.  # noqa: E501

        The role's last updated date.  # noqa: E501

        :return: The updated_date of this RoleResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this RoleResponseModel.

        The role's last updated date.  # noqa: E501

        :param updated_date: The updated_date of this RoleResponseModel.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def owned_by(self):
        """Gets the owned_by of this RoleResponseModel.  # noqa: E501

        The role's owner.  # noqa: E501

        :return: The owned_by of this RoleResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._owned_by

    @owned_by.setter
    def owned_by(self, owned_by):
        """Sets the owned_by of this RoleResponseModel.

        The role's owner.  # noqa: E501

        :param owned_by: The owned_by of this RoleResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["All", "System", "Customer"]  # noqa: E501
        if owned_by not in allowed_values:
            raise ValueError(
                "Invalid value for `owned_by` ({0}), must be one of {1}"  # noqa: E501
                .format(owned_by, allowed_values)
            )

        self._owned_by = owned_by

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
        if issubclass(RoleResponseModel, dict):
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
        if not isinstance(other, RoleResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
