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
from cloudcheckr_cmx.api.roles_api import RolesApi  # noqa: E501
from cloudcheckr_cmx.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = cloudcheckr_cmx.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role(self):
        """Test case for create_role

        Create a new role.  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete a role.  # noqa: E501
        """
        pass

    def test_get_all(self):
        """Test case for get_all

        Get all roles.  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get an individual role.  # noqa: E501
        """
        pass

    def test_list_clients_with_role_id(self):
        """Test case for list_clients_with_role_id

        Get all clients belonging to a role.  # noqa: E501
        """
        pass

    def test_list_users_with_role_id(self):
        """Test case for list_users_with_role_id

        Get all users belonging to a role.  # noqa: E501
        """
        pass

    def test_modify_client_roles(self):
        """Test case for modify_client_roles

        Add or remove a role from multiple clients.  # noqa: E501
        """
        pass

    def test_modify_user_roles(self):
        """Test case for modify_user_roles

        Add or remove a role from multiple users.  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update a role.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
