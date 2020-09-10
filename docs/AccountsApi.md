# cloudcheckr_cmx.AccountsApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /customer/v1/customers/{customerId}/accounts/{accountId} | Get an individual account, account group, or MAV.
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /customer/v1/customers/{customerId}/accounts | Get all accounts, account groups, and MAVs.
[**get_ancestors**](AccountsApi.md#get_ancestors) | **GET** /customer/v1/customers/{customerId}/accounts/{accountId}/ancestors | Get all ancestors of an account.


# **get_account**
> AccountGroupResponseModel get_account(customer_id, account_id)

Get an individual account, account group, or MAV.

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
api_instance = cloudcheckr_cmx.AccountsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Get an individual account, account group, or MAV.
    api_response = api_instance.get_account(customer_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**AccountGroupResponseModel**](AccountGroupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> PaginationWithCountResponseAccountGroupSearchResponseModel get_accounts(customer_id, account_types=account_types, account_ids=account_ids, account_attributes=account_attributes, page_size=page_size, pagination_key=pagination_key, search=search)

Get all accounts, account groups, and MAVs.

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
api_instance = cloudcheckr_cmx.AccountsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_types = ['account_types_example'] # list[str] |  (optional)
account_ids = ['account_ids_example'] # list[str] | Specific account IDs to return. (optional)
account_attributes = ['account_attributes_example'] # list[str] | Account attributes to be searched. This will attempt to match name or name:value combinations.               Matching is not case-sensitive. (optional)
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all accounts, account groups, and MAVs.
    api_response = api_instance.get_accounts(customer_id, account_types=account_types, account_ids=account_ids, account_attributes=account_attributes, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_types** | [**list[str]**](str.md)|  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Specific account IDs to return. | [optional] 
 **account_attributes** | [**list[str]**](str.md)| Account attributes to be searched. This will attempt to match name or name:value combinations.               Matching is not case-sensitive. | [optional] 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseAccountGroupSearchResponseModel**](PaginationWithCountResponseAccountGroupSearchResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors**
> AncestorsResponseModel get_ancestors(customer_id, account_id)

Get all ancestors of an account.

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
api_instance = cloudcheckr_cmx.AccountsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Get all ancestors of an account.
    api_response = api_instance.get_ancestors(customer_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**AncestorsResponseModel**](AncestorsResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

