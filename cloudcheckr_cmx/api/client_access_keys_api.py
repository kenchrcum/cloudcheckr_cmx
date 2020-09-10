# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudcheckr_cmx.api_client import ApiClient


class ClientAccessKeysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_client_access_key(self, customer_id, client_id, **kwargs):  # noqa: E501
        """Create a new client access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_access_key(customer_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param CreateRequestClientAccessKeyRequestModel request: This includes the settings to create the new client Access Key.
        :return: NewClientAccessInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_client_access_key_with_http_info(customer_id, client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_client_access_key_with_http_info(customer_id, client_id, **kwargs)  # noqa: E501
            return data

    def create_client_access_key_with_http_info(self, customer_id, client_id, **kwargs):  # noqa: E501
        """Create a new client access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_client_access_key_with_http_info(customer_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param CreateRequestClientAccessKeyRequestModel request: This includes the settings to create the new client Access Key.
        :return: NewClientAccessInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'client_id', 'request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client_access_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `create_client_access_key`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `create_client_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/customers/{customerId}/clients/{clientId}/access-keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewClientAccessInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_client_access_key(self, customer_id, client_id, access_key_id, **kwargs):  # noqa: E501
        """Delete a client access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client_access_key(customer_id, client_id, access_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param str access_key_id:  (required)
        :return: ClientAccessKeyResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_client_access_key_with_http_info(customer_id, client_id, access_key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_client_access_key_with_http_info(customer_id, client_id, access_key_id, **kwargs)  # noqa: E501
            return data

    def delete_client_access_key_with_http_info(self, customer_id, client_id, access_key_id, **kwargs):  # noqa: E501
        """Delete a client access key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_client_access_key_with_http_info(customer_id, client_id, access_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param str access_key_id:  (required)
        :return: ClientAccessKeyResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'client_id', 'access_key_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_client_access_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `delete_client_access_key`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `delete_client_access_key`")  # noqa: E501
        # verify the required parameter 'access_key_id' is set
        if ('access_key_id' not in params or
                params['access_key_id'] is None):
            raise ValueError("Missing the required parameter `access_key_id` when calling `delete_client_access_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501
        if 'access_key_id' in params:
            path_params['accessKeyId'] = params['access_key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/customers/{customerId}/clients/{clientId}/access-keys/{accessKeyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientAccessKeyResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_client_access_keys(self, customer_id, client_id, **kwargs):  # noqa: E501
        """Get all client access keys.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_client_access_keys(customer_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param int page_size: number of items to include in the response
        :param str pagination_key: key used to fetch the next page of items
        :param str order_by: orders a given property
        :param str filter: filters the result by the conditions
        :return: PaginationWithCountResponseClientAccessKeyResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_client_access_keys_with_http_info(customer_id, client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_client_access_keys_with_http_info(customer_id, client_id, **kwargs)  # noqa: E501
            return data

    def list_client_access_keys_with_http_info(self, customer_id, client_id, **kwargs):  # noqa: E501
        """Get all client access keys.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_client_access_keys_with_http_info(customer_id, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id:  (required)
        :param str client_id:  (required)
        :param int page_size: number of items to include in the response
        :param str pagination_key: key used to fetch the next page of items
        :param str order_by: orders a given property
        :param str filter: filters the result by the conditions
        :return: PaginationWithCountResponseClientAccessKeyResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'client_id', 'page_size', 'pagination_key', 'order_by', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_client_access_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `list_client_access_keys`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `list_client_access_keys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501
        if 'client_id' in params:
            path_params['clientId'] = params['client_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('$pageSize', params['page_size']))  # noqa: E501
        if 'pagination_key' in params:
            query_params.append(('$paginationKey', params['pagination_key']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('$orderBy', params['order_by']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/customers/{customerId}/clients/{clientId}/access-keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginationWithCountResponseClientAccessKeyResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
