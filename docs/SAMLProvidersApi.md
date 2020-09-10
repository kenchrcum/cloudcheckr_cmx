# cloudcheckr_cmx.SAMLProvidersApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_provider**](SAMLProvidersApi.md#create_saml_provider) | **POST** /auth/v1/customers/{customerId}/saml-providers | Creates a new SAML provider entry for this customer.
[**delete_saml_provider**](SAMLProvidersApi.md#delete_saml_provider) | **DELETE** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId} | Deletes an existing SAML provider entry for this customer.
[**get_saml_provider**](SAMLProvidersApi.md#get_saml_provider) | **GET** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId} | Get a single SAML provider by ID.
[**list_saml_providers**](SAMLProvidersApi.md#list_saml_providers) | **GET** /auth/v1/customers/{customerId}/saml-providers | Get all SAML providers.
[**update_saml_provider**](SAMLProvidersApi.md#update_saml_provider) | **PUT** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId} | Updates an existing SAML provider entry for this customer.


# **create_saml_provider**
> SamlProviderResponseDetailModel create_saml_provider(customer_id, request=request)

Creates a new SAML provider entry for this customer.

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
api_instance = cloudcheckr_cmx.SAMLProvidersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
request = cloudcheckr_cmx.CreateRequestSamlProviderRequestModel() # CreateRequestSamlProviderRequestModel |  (optional)

try:
    # Creates a new SAML provider entry for this customer.
    api_response = api_instance.create_saml_provider(customer_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProvidersApi->create_saml_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **request** | [**CreateRequestSamlProviderRequestModel**](CreateRequestSamlProviderRequestModel.md)|  | [optional] 

### Return type

[**SamlProviderResponseDetailModel**](SamlProviderResponseDetailModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_provider**
> delete_saml_provider(customer_id, saml_provider_id)

Deletes an existing SAML provider entry for this customer.

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
api_instance = cloudcheckr_cmx.SAMLProvidersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 

try:
    # Deletes an existing SAML provider entry for this customer.
    api_instance.delete_saml_provider(customer_id, saml_provider_id)
except ApiException as e:
    print("Exception when calling SAMLProvidersApi->delete_saml_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_provider**
> SamlProviderResponseDetailModel get_saml_provider(customer_id, saml_provider_id)

Get a single SAML provider by ID.

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
api_instance = cloudcheckr_cmx.SAMLProvidersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 

try:
    # Get a single SAML provider by ID.
    api_response = api_instance.get_saml_provider(customer_id, saml_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProvidersApi->get_saml_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 

### Return type

[**SamlProviderResponseDetailModel**](SamlProviderResponseDetailModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saml_providers**
> PaginationWithCountResponseSamlProviderResponseModel list_saml_providers(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter)

Get all SAML providers.

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
api_instance = cloudcheckr_cmx.SAMLProvidersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)
filter = 'filter_example' # str | filters the result by the conditions (optional)

try:
    # Get all SAML providers.
    api_response = api_instance.list_saml_providers(customer_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProvidersApi->list_saml_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 
 **filter** | **str**| filters the result by the conditions | [optional] 

### Return type

[**PaginationWithCountResponseSamlProviderResponseModel**](PaginationWithCountResponseSamlProviderResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_provider**
> SamlProviderResponseDetailModel update_saml_provider(customer_id, saml_provider_id, request=request)

Updates an existing SAML provider entry for this customer.

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
api_instance = cloudcheckr_cmx.SAMLProvidersApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestSamlProviderRequestModel() # UpdateRequestSamlProviderRequestModel |  (optional)

try:
    # Updates an existing SAML provider entry for this customer.
    api_response = api_instance.update_saml_provider(customer_id, saml_provider_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProvidersApi->update_saml_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 
 **request** | [**UpdateRequestSamlProviderRequestModel**](UpdateRequestSamlProviderRequestModel.md)|  | [optional] 

### Return type

[**SamlProviderResponseDetailModel**](SamlProviderResponseDetailModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

