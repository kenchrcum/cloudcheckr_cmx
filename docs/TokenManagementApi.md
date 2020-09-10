# cloudcheckr_cmx.TokenManagementApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_token_for_delegate_access_token**](TokenManagementApi.md#exchange_token_for_delegate_access_token) | **PUT** /auth/v1/token/exchange/{customerId} | Exchange a token for a different customer.
[**get_token_info**](TokenManagementApi.md#get_token_info) | **GET** /auth/v1/token/info | Get information about the current bearer token.


# **exchange_token_for_delegate_access_token**
> TokenResponse exchange_token_for_delegate_access_token(customer_id)

Exchange a token for a different customer.

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
api_instance = cloudcheckr_cmx.TokenManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    # Exchange a token for a different customer.
    api_response = api_instance.exchange_token_for_delegate_access_token(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenManagementApi->exchange_token_for_delegate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_info**
> TokenInfoResponse get_token_info()

Get information about the current bearer token.

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
api_instance = cloudcheckr_cmx.TokenManagementApi(cloudcheckr_cmx.ApiClient(configuration))

try:
    # Get information about the current bearer token.
    api_response = api_instance.get_token_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenManagementApi->get_token_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenInfoResponse**](TokenInfoResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

