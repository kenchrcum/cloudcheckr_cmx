# cloudcheckr_cmx.ClientAccessKeysApi

All URIs are relative to *https://api-us.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_access_key**](ClientAccessKeysApi.md#create_client_access_key) | **POST** /auth/v1/customers/{customerId}/clients/{clientId}/access-keys | Create a new client access key.
[**delete_client_access_key**](ClientAccessKeysApi.md#delete_client_access_key) | **DELETE** /auth/v1/customers/{customerId}/clients/{clientId}/access-keys/{accessKeyId} | Delete a client access key.
[**list_client_access_keys**](ClientAccessKeysApi.md#list_client_access_keys) | **GET** /auth/v1/customers/{customerId}/clients/{clientId}/access-keys | Get all client access keys.


# **create_client_access_key**
> NewClientAccessInfo create_client_access_key(customer_id, client_id, request=request)

Create a new client access key.

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
api_instance = cloudcheckr_cmx.ClientAccessKeysApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 
request = cloudcheckr_cmx.CreateRequestClientAccessKeyRequestModel() # CreateRequestClientAccessKeyRequestModel | This includes the settings to create the new client Access Key. (optional)

try:
    # Create a new client access key.
    api_response = api_instance.create_client_access_key(customer_id, client_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAccessKeysApi->create_client_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 
 **request** | [**CreateRequestClientAccessKeyRequestModel**](CreateRequestClientAccessKeyRequestModel.md)| This includes the settings to create the new client Access Key. | [optional] 

### Return type

[**NewClientAccessInfo**](NewClientAccessInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_access_key**
> ClientAccessKeyResponseModel delete_client_access_key(customer_id, client_id, access_key_id)

Delete a client access key.

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
api_instance = cloudcheckr_cmx.ClientAccessKeysApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 
access_key_id = 'access_key_id_example' # str | 

try:
    # Delete a client access key.
    api_response = api_instance.delete_client_access_key(customer_id, client_id, access_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAccessKeysApi->delete_client_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 
 **access_key_id** | **str**|  | 

### Return type

[**ClientAccessKeyResponseModel**](ClientAccessKeyResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_access_keys**
> PaginationWithCountResponseClientAccessKeyResponseModel list_client_access_keys(customer_id, client_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter)

Get all client access keys.

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
api_instance = cloudcheckr_cmx.ClientAccessKeysApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)

try:
    # Get all client access keys.
    api_response = api_instance.list_client_access_keys(customer_id, client_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAccessKeysApi->list_client_access_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 

### Return type

[**PaginationWithCountResponseClientAccessKeyResponseModel**](PaginationWithCountResponseClientAccessKeyResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

