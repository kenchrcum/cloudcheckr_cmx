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


class SamlProviderRuleRequestModel(object):
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
        'saml_claim': 'SamlClaimModel',
        'mapped_role_id': 'str'
    }

    attribute_map = {
        'saml_claim': 'samlClaim',
        'mapped_role_id': 'mappedRoleId'
    }

    def __init__(self, saml_claim=None, mapped_role_id=None):  # noqa: E501
        """SamlProviderRuleRequestModel - a model defined in Swagger"""  # noqa: E501

        self._saml_claim = None
        self._mapped_role_id = None
        self.discriminator = None

        if saml_claim is not None:
            self.saml_claim = saml_claim
        if mapped_role_id is not None:
            self.mapped_role_id = mapped_role_id

    @property
    def saml_claim(self):
        """Gets the saml_claim of this SamlProviderRuleRequestModel.  # noqa: E501

        SAML attribute info used for matching.  # noqa: E501

        :return: The saml_claim of this SamlProviderRuleRequestModel.  # noqa: E501
        :rtype: SamlClaimModel
        """
        return self._saml_claim

    @saml_claim.setter
    def saml_claim(self, saml_claim):
        """Sets the saml_claim of this SamlProviderRuleRequestModel.

        SAML attribute info used for matching.  # noqa: E501

        :param saml_claim: The saml_claim of this SamlProviderRuleRequestModel.  # noqa: E501
        :type: SamlClaimModel
        """

        self._saml_claim = saml_claim

    @property
    def mapped_role_id(self):
        """Gets the mapped_role_id of this SamlProviderRuleRequestModel.  # noqa: E501

        Mapped role ID. This property supports: resetting.  # noqa: E501

        :return: The mapped_role_id of this SamlProviderRuleRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._mapped_role_id

    @mapped_role_id.setter
    def mapped_role_id(self, mapped_role_id):
        """Sets the mapped_role_id of this SamlProviderRuleRequestModel.

        Mapped role ID. This property supports: resetting.  # noqa: E501

        :param mapped_role_id: The mapped_role_id of this SamlProviderRuleRequestModel.  # noqa: E501
        :type: str
        """

        self._mapped_role_id = mapped_role_id

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
        if issubclass(SamlProviderRuleRequestModel, dict):
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
        if not isinstance(other, SamlProviderRuleRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
