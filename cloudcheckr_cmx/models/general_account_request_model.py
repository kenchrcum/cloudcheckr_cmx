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


class GeneralAccountRequestModel(object):
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
        'provider': 'str',
        'parent_id': 'str',
        'associated_account_attributes': 'list[AccountAttributeModification]'
    }

    attribute_map = {
        'name': 'name',
        'provider': 'provider',
        'parent_id': 'parentId',
        'associated_account_attributes': 'associatedAccountAttributes'
    }

    def __init__(self, name=None, provider=None, parent_id=None, associated_account_attributes=None):  # noqa: E501
        """GeneralAccountRequestModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._provider = None
        self._parent_id = None
        self._associated_account_attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if parent_id is not None:
            self.parent_id = parent_id
        if associated_account_attributes is not None:
            self.associated_account_attributes = associated_account_attributes

    @property
    def name(self):
        """Gets the name of this GeneralAccountRequestModel.  # noqa: E501

        The account's name.  # noqa: E501

        :return: The name of this GeneralAccountRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GeneralAccountRequestModel.

        The account's name.  # noqa: E501

        :param name: The name of this GeneralAccountRequestModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this GeneralAccountRequestModel.  # noqa: E501

        The cloud provider associated with the cloud account.  This property cannot be updated.  # noqa: E501

        :return: The provider of this GeneralAccountRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this GeneralAccountRequestModel.

        The cloud provider associated with the cloud account.  This property cannot be updated.  # noqa: E501

        :param provider: The provider of this GeneralAccountRequestModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotApplicable", "AWS", "Azure", "Google", "VMware", "Oracle"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def parent_id(self):
        """Gets the parent_id of this GeneralAccountRequestModel.  # noqa: E501

        The account's parent. This property supports: resetting.  # noqa: E501

        :return: The parent_id of this GeneralAccountRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this GeneralAccountRequestModel.

        The account's parent. This property supports: resetting.  # noqa: E501

        :param parent_id: The parent_id of this GeneralAccountRequestModel.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def associated_account_attributes(self):
        """Gets the associated_account_attributes of this GeneralAccountRequestModel.  # noqa: E501

        Associated account attributes. This property supports: resetting.  # noqa: E501

        :return: The associated_account_attributes of this GeneralAccountRequestModel.  # noqa: E501
        :rtype: list[AccountAttributeModification]
        """
        return self._associated_account_attributes

    @associated_account_attributes.setter
    def associated_account_attributes(self, associated_account_attributes):
        """Sets the associated_account_attributes of this GeneralAccountRequestModel.

        Associated account attributes. This property supports: resetting.  # noqa: E501

        :param associated_account_attributes: The associated_account_attributes of this GeneralAccountRequestModel.  # noqa: E501
        :type: list[AccountAttributeModification]
        """

        self._associated_account_attributes = associated_account_attributes

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
        if issubclass(GeneralAccountRequestModel, dict):
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
        if not isinstance(other, GeneralAccountRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
