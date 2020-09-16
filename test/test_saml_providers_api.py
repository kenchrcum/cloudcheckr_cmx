# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cloudcheckr_cmx
from cloudcheckr_cmx.api.saml_providers_api import SAMLProvidersApi  # noqa: E501
from cloudcheckr_cmx.rest import ApiException


class TestSAMLProvidersApi(unittest.TestCase):
    """SAMLProvidersApi unit test stubs"""

    def setUp(self):
        self.api = SAMLProvidersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_saml_provider(self):
        """Test case for create_saml_provider

        Creates a new SAML provider entry for this customer.  # noqa: E501
        """
        pass

    def test_delete_saml_provider(self):
        """Test case for delete_saml_provider

        Deletes an existing SAML provider entry for this customer.  # noqa: E501
        """
        pass

    def test_get_saml_provider(self):
        """Test case for get_saml_provider

        Get a single SAML provider by ID.  # noqa: E501
        """
        pass

    def test_list_saml_providers(self):
        """Test case for list_saml_providers

        Get all SAML providers.  # noqa: E501
        """
        pass

    def test_update_saml_provider(self):
        """Test case for update_saml_provider

        Updates an existing SAML provider entry for this customer.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
