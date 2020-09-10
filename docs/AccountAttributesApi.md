# cloudcheckr_cmx.AccountAttributesApi

All URIs are relative to *https://api-us.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_account_attribute**](AccountAttributesApi.md#attach_account_attribute) | **PUT** /customer/v1/customers/{customerId}/account-attributes/{attributeName}/values/{value}/assign | Bulk associate account attribute name-value to list of general accounts.
[**delete_account_attribute**](AccountAttributesApi.md#delete_account_attribute) | **DELETE** /customer/v1/customers/{customerId}/account-attributes/{attributeName} | Delete an account attribute.
[**get_account_attribute**](AccountAttributesApi.md#get_account_attribute) | **GET** /customer/v1/customers/{customerId}/account-attributes/{attributeName} | Get an individual account attribute.
[**list_account_attributes**](AccountAttributesApi.md#list_account_attributes) | **GET** /customer/v1/customers/{customerId}/account-attributes | Get all account attributes.
[**update_account_attribute**](AccountAttributesApi.md#update_account_attribute) | **PUT** /customer/v1/customers/{customerId}/account-attributes | Create/Update an account attribute.


# **attach_account_attribute**
> BulkAccountAssignmentResponseModelAccountAttributeAssignmentResponseModel attach_account_attribute(customer_id, attribute_name, value, request=request)

Bulk associate account attribute name-value to list of general accounts.

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
api_instance = cloudcheckr_cmx.AccountAttributesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 
value = 'value_example' # str | 
request = cloudcheckr_cmx.BulkAccountAttributeAssignmentRequestModel() # BulkAccountAttributeAssignmentRequestModel |  (optional)

try:
    # Bulk associate account attribute name-value to list of general accounts.
    api_response = api_instance.attach_account_attribute(customer_id, attribute_name, value, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAttributesApi->attach_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **attribute_name** | **str**|  | 
 **value** | **str**|  | 
 **request** | [**BulkAccountAttributeAssignmentRequestModel**](BulkAccountAttributeAssignmentRequestModel.md)|  | [optional] 

### Return type

[**BulkAccountAssignmentResponseModelAccountAttributeAssignmentResponseModel**](BulkAccountAssignmentResponseModelAccountAttributeAssignmentResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_attribute**
> delete_account_attribute(customer_id, attribute_name)

Delete an account attribute.

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
api_instance = cloudcheckr_cmx.AccountAttributesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 

try:
    # Delete an account attribute.
    api_instance.delete_account_attribute(customer_id, attribute_name)
except ApiException as e:
    print("Exception when calling AccountAttributesApi->delete_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **attribute_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attribute**
> AccountAttributeResponseModel get_account_attribute(customer_id, attribute_name)

Get an individual account attribute.

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
api_instance = cloudcheckr_cmx.AccountAttributesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
attribute_name = 'attribute_name_example' # str | 

try:
    # Get an individual account attribute.
    api_response = api_instance.get_account_attribute(customer_id, attribute_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAttributesApi->get_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **attribute_name** | **str**|  | 

### Return type

[**AccountAttributeResponseModel**](AccountAttributeResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_attributes**
> PaginationResponseAccountAttributeResponseModel list_account_attributes(customer_id, include_values=include_values, search=search, page_size=page_size, pagination_key=pagination_key, order_by=order_by)

Get all account attributes.

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
api_instance = cloudcheckr_cmx.AccountAttributesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
include_values = false # bool |  (optional) (default to false)
search = 'search_example' # str | finds all resources that match the specified value (optional)
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)

try:
    # Get all account attributes.
    api_response = api_instance.list_account_attributes(customer_id, include_values=include_values, search=search, page_size=page_size, pagination_key=pagination_key, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAttributesApi->list_account_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **include_values** | **bool**|  | [optional] [default to false]
 **search** | **str**| finds all resources that match the specified value | [optional] 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 

### Return type

[**PaginationResponseAccountAttributeResponseModel**](PaginationResponseAccountAttributeResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_attribute**
> AccountAttributeResponseModel update_account_attribute(customer_id, request=request)

Create/Update an account attribute.

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
api_instance = cloudcheckr_cmx.AccountAttributesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestAccountAttributeRequestModel() # UpdateRequestAccountAttributeRequestModel |  (optional)

try:
    # Create/Update an account attribute.
    api_response = api_instance.update_account_attribute(customer_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAttributesApi->update_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **request** | [**UpdateRequestAccountAttributeRequestModel**](UpdateRequestAccountAttributeRequestModel.md)|  | [optional] 

### Return type

[**AccountAttributeResponseModel**](AccountAttributeResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

