# cloudcheckr_cmx.UsersApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /auth/v1/customers/{customerId}/users | Create a new user.
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /auth/v1/customers/{customerId}/users/{userId} | Delete a user.
[**get_user**](UsersApi.md#get_user) | **GET** /auth/v1/customers/{customerId}/users/{userId} | Get an individual user.
[**list_users**](UsersApi.md#list_users) | **GET** /auth/v1/customers/{customerId}/users | Get all users.
[**send_activation**](UsersApi.md#send_activation) | **POST** /auth/v1/customers/{customerId}/users/{userId}/send-activation | Send a user activation email.
[**update_user**](UsersApi.md#update_user) | **PUT** /auth/v1/customers/{customerId}/users/{userId} | Update a user.


# **create_user**
> UserResponseModel create_user(customer_id, request=request)

Create a new user.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
request = cloudcheckr_cmx.CreateRequestUserRequestModel() # CreateRequestUserRequestModel |  (optional)

try:
    # Create a new user.
    api_response = api_instance.create_user(customer_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **request** | [**CreateRequestUserRequestModel**](CreateRequestUserRequestModel.md)|  | [optional] 

### Return type

[**UserResponseModel**](UserResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(customer_id, user_id)

Delete a user.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Delete a user.
    api_instance.delete_user(customer_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponseModel get_user(customer_id, user_id)

Get an individual user.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Get an individual user.
    api_response = api_instance.get_user(customer_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserResponseModel**](UserResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> PaginationWithCountResponseUserResponseModel list_users(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter, search=search)

Get all users.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all users.
    api_response = api_instance.list_users(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseUserResponseModel**](PaginationWithCountResponseUserResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_activation**
> send_activation(customer_id, user_id)

Send a user activation email.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Send a user activation email.
    api_instance.send_activation(customer_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->send_activation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserResponseModel update_user(customer_id, user_id, request=request)

Update a user.

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
api_instance = cloudcheckr_cmx.UsersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
user_id = 'user_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestUserRequestModel() # UpdateRequestUserRequestModel |  (optional)

try:
    # Update a user.
    api_response = api_instance.update_user(customer_id, user_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **user_id** | **str**|  | 
 **request** | [**UpdateRequestUserRequestModel**](UpdateRequestUserRequestModel.md)|  | [optional] 

### Return type

[**UserResponseModel**](UserResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

