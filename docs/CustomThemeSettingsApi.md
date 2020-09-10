# cloudcheckr_cmx.CustomThemeSettingsApi

All URIs are relative to *https://api-eu.cloudcheckr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_theme_settings**](CustomThemeSettingsApi.md#get_theme_settings) | **GET** /customer/v1/customers/theme | Retrieves the customer&#39;s theme settings.
[**update_custom_theme_settings**](CustomThemeSettingsApi.md#update_custom_theme_settings) | **PUT** /customer/v1/customers/{customerId}/theme | Update the custom theme settings such as logo, colors, etc.


# **get_theme_settings**
> CustomThemeResponseModel get_theme_settings()

Retrieves the customer's theme settings.

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
api_instance = cloudcheckr_cmx.CustomThemeSettingsApi(cloudcheckr_cmx.ApiClient(configuration))

try:
    # Retrieves the customer's theme settings.
    api_response = api_instance.get_theme_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomThemeSettingsApi->get_theme_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomThemeResponseModel**](CustomThemeResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_theme_settings**
> CustomThemeResponseModel update_custom_theme_settings(customer_id, request=request)

Update the custom theme settings such as logo, colors, etc.

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
api_instance = cloudcheckr_cmx.CustomThemeSettingsApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
request = cloudcheckr_cmx.UpdateRequestCustomThemeRequestModel() # UpdateRequestCustomThemeRequestModel |  (optional)

try:
    # Update the custom theme settings such as logo, colors, etc.
    api_response = api_instance.update_custom_theme_settings(customer_id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomThemeSettingsApi->update_custom_theme_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **request** | [**UpdateRequestCustomThemeRequestModel**](UpdateRequestCustomThemeRequestModel.md)|  | [optional] 

### Return type

[**CustomThemeResponseModel**](CustomThemeResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

