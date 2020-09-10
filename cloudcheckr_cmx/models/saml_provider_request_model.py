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


class SamlProviderRequestModel(object):
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
        'idp_metadata': 'str',
        'permitted_child_customers': 'list[BasicRequestListModification]'
    }

    attribute_map = {
        'name': 'name',
        'idp_metadata': 'idpMetadata',
        'permitted_child_customers': 'permittedChildCustomers'
    }

    def __init__(self, name=None, idp_metadata=None, permitted_child_customers=None):  # noqa: E501
        """SamlProviderRequestModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._idp_metadata = None
        self._permitted_child_customers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if idp_metadata is not None:
            self.idp_metadata = idp_metadata
        if permitted_child_customers is not None:
            self.permitted_child_customers = permitted_child_customers

    @property
    def name(self):
        """Gets the name of this SamlProviderRequestModel.  # noqa: E501

        The unique name of the SAML provider.  # noqa: E501

        :return: The name of this SamlProviderRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SamlProviderRequestModel.

        The unique name of the SAML provider.  # noqa: E501

        :param name: The name of this SamlProviderRequestModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def idp_metadata(self):
        """Gets the idp_metadata of this SamlProviderRequestModel.  # noqa: E501

        The IdpMetadata for the given provider.  # noqa: E501

        :return: The idp_metadata of this SamlProviderRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._idp_metadata

    @idp_metadata.setter
    def idp_metadata(self, idp_metadata):
        """Sets the idp_metadata of this SamlProviderRequestModel.

        The IdpMetadata for the given provider.  # noqa: E501

        :param idp_metadata: The idp_metadata of this SamlProviderRequestModel.  # noqa: E501
        :type: str
        """

        self._idp_metadata = idp_metadata

    @property
    def permitted_child_customers(self):
        """Gets the permitted_child_customers of this SamlProviderRequestModel.  # noqa: E501

        A list of the customers which will be permitted to use this SAML provider to authenticate. This property supports: resetting.  # noqa: E501

        :return: The permitted_child_customers of this SamlProviderRequestModel.  # noqa: E501
        :rtype: list[BasicRequestListModification]
        """
        return self._permitted_child_customers

    @permitted_child_customers.setter
    def permitted_child_customers(self, permitted_child_customers):
        """Sets the permitted_child_customers of this SamlProviderRequestModel.

        A list of the customers which will be permitted to use this SAML provider to authenticate. This property supports: resetting.  # noqa: E501

        :param permitted_child_customers: The permitted_child_customers of this SamlProviderRequestModel.  # noqa: E501
        :type: list[BasicRequestListModification]
        """

        self._permitted_child_customers = permitted_child_customers

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
        if issubclass(SamlProviderRequestModel, dict):
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
        if not isinstance(other, SamlProviderRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other