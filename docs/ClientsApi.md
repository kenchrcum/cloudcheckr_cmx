# cloudcheckr_cmx.ClientsApi

All URIs are relative to *//api-eu.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientsApi.md#create_client) | **POST** /auth/v1/customers/{customerId}/clients | Create a new client.
[**delete_client**](ClientsApi.md#delete_client) | **DELETE** /auth/v1/customers/{customerId}/clients/{clientId} | Delete a client.
[**get_client**](ClientsApi.md#get_client) | **GET** /auth/v1/customers/{customerId}/clients/{clientId} | Get an individual client.
[**list_clients**](ClientsApi.md#list_clients) | **GET** /auth/v1/customers/{customerId}/clients | Get all clients.
[**update_client**](ClientsApi.md#update_client) | **PUT** /auth/v1/customers/{customerId}/clients/{clientId} | Update a client.

# **create_client**
> ClientResponseModel create_client(customer_id, body=body)

Create a new client.

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
api_instance = cloudcheckr_cmx.ClientsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.CreateRequestClientCreateRequestModel() # CreateRequestClientCreateRequestModel | This includes the settings to create the new client. (optional)

try:
    # Create a new client.
    api_response = api_instance.create_client(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**CreateRequestClientCreateRequestModel**](CreateRequestClientCreateRequestModel.md)| This includes the settings to create the new client. | [optional] 

### Return type

[**ClientResponseModel**](ClientResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(customer_id, client_id)

Delete a client.

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
api_instance = cloudcheckr_cmx.ClientsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 

try:
    # Delete a client.
    api_instance.delete_client(customer_id, client_id)
except ApiException as e:
    print("Exception when calling ClientsApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> ClientResponseModel get_client(customer_id, client_id)

Get an individual client.

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
api_instance = cloudcheckr_cmx.ClientsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 

try:
    # Get an individual client.
    api_response = api_instance.get_client(customer_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 

### Return type

[**ClientResponseModel**](ClientResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> PaginationWithCountResponseClientResponseModel list_clients(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, search=search, filter=filter)

Get all clients.

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
api_instance = cloudcheckr_cmx.ClientsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)

try:
    # Get all clients.
    api_response = api_instance.list_clients(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, search=search, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 

### Return type

[**PaginationWithCountResponseClientResponseModel**](PaginationWithCountResponseClientResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> ClientResponseModel update_client(customer_id, client_id, body=body)

Update a client.

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
api_instance = cloudcheckr_cmx.ClientsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
client_id = 'client_id_example' # str | 
body = cloudcheckr_cmx.UpdateRequestClientRequestModel() # UpdateRequestClientRequestModel |  (optional)

try:
    # Update a client.
    api_response = api_instance.update_client(customer_id, client_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **client_id** | **str**|  | 
 **body** | [**UpdateRequestClientRequestModel**](UpdateRequestClientRequestModel.md)|  | [optional] 

### Return type

[**ClientResponseModel**](ClientResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

