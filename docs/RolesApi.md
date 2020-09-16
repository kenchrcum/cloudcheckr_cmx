# cloudcheckr_cmx.RolesApi

All URIs are relative to *//api-eu.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /policy/v1/customers/{customerId}/roles | Create a new role.
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /policy/v1/customers/{customerId}/roles/{roleId} | Delete a role.
[**get_all**](RolesApi.md#get_all) | **GET** /policy/v1/customers/{customerId}/roles | Get all roles.
[**get_role**](RolesApi.md#get_role) | **GET** /policy/v1/customers/{customerId}/roles/{roleId} | Get an individual role.
[**list_clients_with_role_id**](RolesApi.md#list_clients_with_role_id) | **GET** /auth/v1/customers/{customerId}/roles/{roleId}/clients | Get all clients belonging to a role.
[**list_users_with_role_id**](RolesApi.md#list_users_with_role_id) | **GET** /auth/v1/customers/{customerId}/roles/{roleId}/users | Get all users belonging to a role.
[**modify_client_roles**](RolesApi.md#modify_client_roles) | **PUT** /auth/v1/customers/{customerId}/roles/{roleId}/clients | Add or remove a role from multiple clients.
[**modify_user_roles**](RolesApi.md#modify_user_roles) | **PUT** /auth/v1/customers/{customerId}/roles/{roleId}/users | Add or remove a role from multiple users.
[**update_role**](RolesApi.md#update_role) | **PUT** /policy/v1/customers/{customerId}/roles/{roleId} | Update a role.

# **create_role**
> RoleResponseModel create_role(customer_id, body=body)

Create a new role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.CreateRequestRoleRequestModel() # CreateRequestRoleRequestModel |  (optional)

try:
    # Create a new role.
    api_response = api_instance.create_role(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**CreateRequestRoleRequestModel**](CreateRequestRoleRequestModel.md)|  | [optional] 

### Return type

[**RoleResponseModel**](RoleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(customer_id, role_id)

Delete a role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    # Delete a role.
    api_instance.delete_role(customer_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> PaginationResponseRoleResponseModel get_all(customer_id, role_ids=role_ids, search=search, owned_by=owned_by, action_type=action_type, order_by=order_by, page_size=page_size, pagination_key=pagination_key)

Get all roles.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_ids = ['role_ids_example'] # list[str] |  (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)
owned_by = 'owned_by_example' # str | finds all resources owned by the specified entity. (optional)
action_type = 'action_type_example' # str | determines which action is taken on a resource. (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)

try:
    # Get all roles.
    api_response = api_instance.get_all(customer_id, role_ids=role_ids, search=search, owned_by=owned_by, action_type=action_type, order_by=order_by, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_ids** | [**list[str]**](str.md)|  | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 
 **owned_by** | **str**| finds all resources owned by the specified entity. | [optional] 
 **action_type** | **str**| determines which action is taken on a resource. | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 

### Return type

[**PaginationResponseRoleResponseModel**](PaginationResponseRoleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResponseModel get_role(customer_id, role_id)

Get an individual role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    # Get an individual role.
    api_response = api_instance.get_role(customer_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**RoleResponseModel**](RoleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients_with_role_id**
> PaginationWithCountResponseMinimalClientResponseModel list_clients_with_role_id(customer_id, role_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)

Get all clients belonging to a role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)

try:
    # Get all clients belonging to a role.
    api_response = api_instance.list_clients_with_role_id(customer_id, role_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_clients_with_role_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 

### Return type

[**PaginationWithCountResponseMinimalClientResponseModel**](PaginationWithCountResponseMinimalClientResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_with_role_id**
> PaginationWithCountResponseMinimalUserResponseModel list_users_with_role_id(customer_id, role_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)

Get all users belonging to a role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)

try:
    # Get all users belonging to a role.
    api_response = api_instance.list_users_with_role_id(customer_id, role_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list_users_with_role_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 

### Return type

[**PaginationWithCountResponseMinimalUserResponseModel**](PaginationWithCountResponseMinimalUserResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_client_roles**
> ListModificationResponseModel modify_client_roles(customer_id, role_id, body=body)

Add or remove a role from multiple clients.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
body = cloudcheckr_cmx.ListModificationRequestModel() # ListModificationRequestModel |  (optional)

try:
    # Add or remove a role from multiple clients.
    api_response = api_instance.modify_client_roles(customer_id, role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->modify_client_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **body** | [**ListModificationRequestModel**](ListModificationRequestModel.md)|  | [optional] 

### Return type

[**ListModificationResponseModel**](ListModificationResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_roles**
> ListModificationResponseModel modify_user_roles(customer_id, role_id, body=body)

Add or remove a role from multiple users.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
body = cloudcheckr_cmx.ListModificationRequestModel() # ListModificationRequestModel |  (optional)

try:
    # Add or remove a role from multiple users.
    api_response = api_instance.modify_user_roles(customer_id, role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->modify_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **body** | [**ListModificationRequestModel**](ListModificationRequestModel.md)|  | [optional] 

### Return type

[**ListModificationResponseModel**](ListModificationResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResponseModel update_role(customer_id, role_id, body=body)

Update a role.

### Example
```python
from __future__ import print_function
import time
import cloudcheckr_cmx
from cloudcheckr_cmx.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = cloudcheckr_cmx.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cloudcheckr_cmx.RolesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
role_id = 'role_id_example' # str | 
body = cloudcheckr_cmx.UpdateRequestRoleRequestModel() # UpdateRequestRoleRequestModel |  (optional)

try:
    # Update a role.
    api_response = api_instance.update_role(customer_id, role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **role_id** | **str**|  | 
 **body** | [**UpdateRequestRoleRequestModel**](UpdateRequestRoleRequestModel.md)|  | [optional] 

### Return type

[**RoleResponseModel**](RoleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

