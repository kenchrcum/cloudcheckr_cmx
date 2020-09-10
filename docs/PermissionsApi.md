# cloudcheckr_cmx.PermissionsApi

All URIs are relative to *https://api-us.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all**](PermissionsApi.md#get_all) | **GET** /policy/v1/customers/{customerId}/permissions | Get all permissions.


# **get_all**
> PaginationWithCountResponsePermissionResponseModel get_all(customer_id, order_by=order_by, filter=filter, search=search)

Get all permissions.

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
api_instance = cloudcheckr_cmx.PermissionsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
order_by = 'order_by_example' # str | orders a given property (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all permissions.
    api_response = api_instance.get_all(customer_id, order_by=order_by, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **order_by** | **str**| orders a given property | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponsePermissionResponseModel**](PaginationWithCountResponsePermissionResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

