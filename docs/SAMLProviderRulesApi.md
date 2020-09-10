# cloudcheckr_cmx.SAMLProviderRulesApi

All URIs are relative to *https://api-us.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_provider_rule**](SAMLProviderRulesApi.md#create_saml_provider_rule) | **POST** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId}/rules | Creates a new SAML provider rule for the specified SAML provider.
[**delete_saml_provider_rule**](SAMLProviderRulesApi.md#delete_saml_provider_rule) | **DELETE** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId}/rules/{ruleId} | Deletes a SAML provider rule.
[**list_saml_provider_rules**](SAMLProviderRulesApi.md#list_saml_provider_rules) | **GET** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId}/rules | Get all SAML provider rules assigned to a SAML provider.
[**update_saml_provider_rule**](SAMLProviderRulesApi.md#update_saml_provider_rule) | **PUT** /auth/v1/customers/{customerId}/saml-providers/{samlProviderId}/rules/{ruleId} | Updates a SAML provider rule.


# **create_saml_provider_rule**
> SamlProviderRuleResponseModel create_saml_provider_rule(customer_id, saml_provider_id, request=request)

Creates a new SAML provider rule for the specified SAML provider.

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
api_instance = cloudcheckr_cmx.SAMLProviderRulesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 
request = cloudcheckr_cmx.CreateRequestSamlProviderRuleRequestModel() # CreateRequestSamlProviderRuleRequestModel |  (optional)

try:
    # Creates a new SAML provider rule for the specified SAML provider.
    api_response = api_instance.create_saml_provider_rule(customer_id, saml_provider_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProviderRulesApi->create_saml_provider_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 
 **request** | [**CreateRequestSamlProviderRuleRequestModel**](CreateRequestSamlProviderRuleRequestModel.md)|  | [optional] 

### Return type

[**SamlProviderRuleResponseModel**](SamlProviderRuleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_provider_rule**
> delete_saml_provider_rule(customer_id, saml_provider_id, rule_id)

Deletes a SAML provider rule.

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
api_instance = cloudcheckr_cmx.SAMLProviderRulesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 
rule_id = 'rule_id_example' # str | 

try:
    # Deletes a SAML provider rule.
    api_instance.delete_saml_provider_rule(customer_id, saml_provider_id, rule_id)
except ApiException as e:
    print("Exception when calling SAMLProviderRulesApi->delete_saml_provider_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saml_provider_rules**
> PaginationWithCountResponseSamlProviderRuleResponseModel list_saml_provider_rules(customer_id, saml_provider_id, page_size=page_size, pagination_key=pagination_key)

Get all SAML provider rules assigned to a SAML provider.

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
api_instance = cloudcheckr_cmx.SAMLProviderRulesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)

try:
    # Get all SAML provider rules assigned to a SAML provider.
    api_response = api_instance.list_saml_provider_rules(customer_id, saml_provider_id, page_size=page_size, pagination_key=pagination_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProviderRulesApi->list_saml_provider_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 

### Return type

[**PaginationWithCountResponseSamlProviderRuleResponseModel**](PaginationWithCountResponseSamlProviderRuleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_provider_rule**
> SamlProviderRuleResponseModel update_saml_provider_rule(customer_id, saml_provider_id, rule_id, request=request)

Updates a SAML provider rule.

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
api_instance = cloudcheckr_cmx.SAMLProviderRulesApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
saml_provider_id = 'saml_provider_id_example' # str | 
rule_id = 'rule_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestSamlProviderRuleRequestModel() # UpdateRequestSamlProviderRuleRequestModel |  (optional)

try:
    # Updates a SAML provider rule.
    api_response = api_instance.update_saml_provider_rule(customer_id, saml_provider_id, rule_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLProviderRulesApi->update_saml_provider_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **saml_provider_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **request** | [**UpdateRequestSamlProviderRuleRequestModel**](UpdateRequestSamlProviderRuleRequestModel.md)|  | [optional] 

### Return type

[**SamlProviderRuleResponseModel**](SamlProviderRuleResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

