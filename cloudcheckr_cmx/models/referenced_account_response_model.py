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


class ReferencedAccountResponseModel(object):
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
        'provider_identifier': 'str',
        'provider_sub_type': 'str',
        'provider_payment_type': 'str',
        'payer_identifier': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provider': 'provider',
        'provider_identifier': 'providerIdentifier',
        'provider_sub_type': 'providerSubType',
        'provider_payment_type': 'providerPaymentType',
        'payer_identifier': 'payerIdentifier',
        'id': 'id'
    }

    def __init__(self, name=None, provider=None, provider_identifier=None, provider_sub_type=None, provider_payment_type=None, payer_identifier=None, id=None):  # noqa: E501
        """ReferencedAccountResponseModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._provider = None
        self._provider_identifier = None
        self._provider_sub_type = None
        self._provider_payment_type = None
        self._payer_identifier = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if provider_identifier is not None:
            self.provider_identifier = provider_identifier
        if provider_sub_type is not None:
            self.provider_sub_type = provider_sub_type
        if provider_payment_type is not None:
            self.provider_payment_type = provider_payment_type
        if payer_identifier is not None:
            self.payer_identifier = payer_identifier
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ReferencedAccountResponseModel.  # noqa: E501

        The account's name. This property supports: sorting.  # noqa: E501

        :return: The name of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReferencedAccountResponseModel.

        The account's name. This property supports: sorting.  # noqa: E501

        :param name: The name of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this ReferencedAccountResponseModel.  # noqa: E501

        The account's cloud provider.  # noqa: E501

        :return: The provider of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ReferencedAccountResponseModel.

        The account's cloud provider.  # noqa: E501

        :param provider: The provider of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def provider_identifier(self):
        """Gets the provider_identifier of this ReferencedAccountResponseModel.  # noqa: E501

        The account's cloud provider identifier.  # noqa: E501

        :return: The provider_identifier of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_identifier

    @provider_identifier.setter
    def provider_identifier(self, provider_identifier):
        """Sets the provider_identifier of this ReferencedAccountResponseModel.

        The account's cloud provider identifier.  # noqa: E501

        :param provider_identifier: The provider_identifier of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_identifier = provider_identifier

    @property
    def provider_sub_type(self):
        """Gets the provider_sub_type of this ReferencedAccountResponseModel.  # noqa: E501

        The account's cloud provider sub-type.  # noqa: E501

        :return: The provider_sub_type of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_sub_type

    @provider_sub_type.setter
    def provider_sub_type(self, provider_sub_type):
        """Sets the provider_sub_type of this ReferencedAccountResponseModel.

        The account's cloud provider sub-type.  # noqa: E501

        :param provider_sub_type: The provider_sub_type of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_sub_type = provider_sub_type

    @property
    def provider_payment_type(self):
        """Gets the provider_payment_type of this ReferencedAccountResponseModel.  # noqa: E501

        The account's payment model.  # noqa: E501

        :return: The provider_payment_type of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_payment_type

    @provider_payment_type.setter
    def provider_payment_type(self, provider_payment_type):
        """Sets the provider_payment_type of this ReferencedAccountResponseModel.

        The account's payment model.  # noqa: E501

        :param provider_payment_type: The provider_payment_type of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Payer", "Payee"]  # noqa: E501
        if provider_payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `provider_payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(provider_payment_type, allowed_values)
            )

        self._provider_payment_type = provider_payment_type

    @property
    def payer_identifier(self):
        """Gets the payer_identifier of this ReferencedAccountResponseModel.  # noqa: E501

        The account's payer identifier.  # noqa: E501

        :return: The payer_identifier of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._payer_identifier

    @payer_identifier.setter
    def payer_identifier(self, payer_identifier):
        """Sets the payer_identifier of this ReferencedAccountResponseModel.

        The account's payer identifier.  # noqa: E501

        :param payer_identifier: The payer_identifier of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._payer_identifier = payer_identifier

    @property
    def id(self):
        """Gets the id of this ReferencedAccountResponseModel.  # noqa: E501

        The account's ID.  # noqa: E501

        :return: The id of this ReferencedAccountResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReferencedAccountResponseModel.

        The account's ID.  # noqa: E501

        :param id: The id of this ReferencedAccountResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(ReferencedAccountResponseModel, dict):
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
        if not isinstance(other, ReferencedAccountResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
