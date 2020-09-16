# cloudcheckr_cmx.CustomersApi

All URIs are relative to *//api-eu.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer**](CustomersApi.md#get_customer) | **GET** /customer/v1/customers/{customerId} | Get an individual customer.
[**list_customers**](CustomersApi.md#list_customers) | **GET** /customer/v1/customers | Get all customers.

# **get_customer**
> CustomerResponseModel get_customer(customer_id)

Get an individual customer.

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
api_instance = cloudcheckr_cmx.CustomersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 

try:
    # Get an individual customer.
    api_response = api_instance.get_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

### Return type

[**CustomerResponseModel**](CustomerResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> PaginationWithCountResponseCustomerResponseModel list_customers(page_size=page_size, pagination_key=pagination_key, search=search, filter=filter, order_by=order_by)

Get all customers.

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
api_instance = cloudcheckr_cmx.CustomersApi(cloudcheckr_cmx.ApiClient(configuration))
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)
order_by = 'order_by_example' # str | orders a given property (optional)

try:
    # Get all customers.
    api_response = api_instance.list_customers(page_size=page_size, pagination_key=pagination_key, search=search, filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 
 **order_by** | **str**| orders a given property | [optional] 

### Return type

[**PaginationWithCountResponseCustomerResponseModel**](PaginationWithCountResponseCustomerResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

