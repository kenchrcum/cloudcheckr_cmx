# cloudcheckr_cmx.PermissionSetsApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission_set**](PermissionSetsApi.md#create_permission_set) | **POST** /policy/v1/customers/{customerId}/permission-sets | Create a permission set.
[**delete_permission_set**](PermissionSetsApi.md#delete_permission_set) | **DELETE** /policy/v1/customers/{customerId}/permission-sets/{permissionSetId} | Delete a permission set.
[**get_all**](PermissionSetsApi.md#get_all) | **GET** /policy/v1/customers/{customerId}/permission-sets | Get all permission sets.
[**get_permission_set**](PermissionSetsApi.md#get_permission_set) | **GET** /policy/v1/customers/{customerId}/permission-sets/{permissionSetId} | Get an individual permission set.
[**update_permission_set**](PermissionSetsApi.md#update_permission_set) | **PUT** /policy/v1/customers/{customerId}/permission-sets/{permissionSetId} | Update a permission set.


# **create_permission_set**
> PermissionSetResponseModel create_permission_set(customer_id, request=request)

Create a permission set.

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
api_instance = cloudcheckr_cmx.PermissionSetsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
request = cloudcheckr_cmx.CreateRequestPermissionSetRequestModel() # CreateRequestPermissionSetRequestModel |  (optional)

try:
    # Create a permission set.
    api_response = api_instance.create_permission_set(customer_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionSetsApi->create_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **request** | [**CreateRequestPermissionSetRequestModel**](CreateRequestPermissionSetRequestModel.md)|  | [optional] 

### Return type

[**PermissionSetResponseModel**](PermissionSetResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_set**
> delete_permission_set(customer_id, permission_set_id)

Delete a permission set.

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
api_instance = cloudcheckr_cmx.PermissionSetsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
permission_set_id = 'permission_set_id_example' # str | 

try:
    # Delete a permission set.
    api_instance.delete_permission_set(customer_id, permission_set_id)
except ApiException as e:
    print("Exception when calling PermissionSetsApi->delete_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **permission_set_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> PaginationResponsePermissionSetResponseModel get_all(customer_id, search=search, owned_by=owned_by, action_type=action_type, order_by=order_by, page_size=page_size, pagination_key=pagination_key)

Get all permission sets.

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
api_instance = cloudcheckr_cmx.PermissionSetsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
search = 'search_example' # str | finds all resources that match the specified value (optional)
owned_by = 'owned_by_example' # str | finds all resources owned by the specified entity. (optional)
action_type = 'action_type_example' # str | determines which action is taken on a resource. (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)

try:
    # Get all permission sets.
    api_response = api_instance.get_all(customer_id, search=search, owned_by=owned_by, action_type=action_type, order_by=order_by, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionSetsApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **search** | **str**| finds all resources that match the specified value | [optional] 
 **owned_by** | **str**| finds all resources owned by the specified entity. | [optional] 
 **action_type** | **str**| determines which action is taken on a resource. | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 

### Return type

[**PaginationResponsePermissionSetResponseModel**](PaginationResponsePermissionSetResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_set**
> PermissionSetResponseModel get_permission_set(customer_id, permission_set_id)

Get an individual permission set.

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
api_instance = cloudcheckr_cmx.PermissionSetsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
permission_set_id = 'permission_set_id_example' # str | 

try:
    # Get an individual permission set.
    api_response = api_instance.get_permission_set(customer_id, permission_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionSetsApi->get_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **permission_set_id** | **str**|  | 

### Return type

[**PermissionSetResponseModel**](PermissionSetResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_set**
> PermissionSetResponseModel update_permission_set(customer_id, permission_set_id, request=request)

Update a permission set.

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
api_instance = cloudcheckr_cmx.PermissionSetsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
permission_set_id = 'permission_set_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestPermissionSetRequestModel() # UpdateRequestPermissionSetRequestModel |  (optional)

try:
    # Update a permission set.
    api_response = api_instance.update_permission_set(customer_id, permission_set_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionSetsApi->update_permission_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **permission_set_id** | **str**|  | 
 **request** | [**UpdateRequestPermissionSetRequestModel**](UpdateRequestPermissionSetRequestModel.md)|  | [optional] 

### Return type

[**PermissionSetResponseModel**](PermissionSetResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

