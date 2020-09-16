# cloudcheckr_cmx.AccountManagementApi

All URIs are relative to *//api-eu.cloudcheckr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_account_groups**](AccountManagementApi.md#attach_account_groups) | **PUT** /customer/v1/customers/{customerId}/account-management/account-groups/{groupId}/attach | Bulk move account groups into a parent account group.
[**attach_account_groups_to_root**](AccountManagementApi.md#attach_account_groups_to_root) | **PUT** /customer/v1/customers/{customerId}/account-management/account-groups/root/attach | Bulk move account groups into the root path.
[**create_account**](AccountManagementApi.md#create_account) | **POST** /customer/v1/customers/{customerId}/account-management/accounts | Create a General Account.
[**create_account_group**](AccountManagementApi.md#create_account_group) | **POST** /customer/v1/customers/{customerId}/account-management/account-groups | Create a new account group.
[**create_mav**](AccountManagementApi.md#create_mav) | **POST** /customer/v1/customers/{customerId}/account-management/mavs | Create a MAV.
[**delete_account**](AccountManagementApi.md#delete_account) | **DELETE** /customer/v1/customers/{customerId}/account-management/accounts/{accountId} | Delete a general account.
[**delete_account_group**](AccountManagementApi.md#delete_account_group) | **DELETE** /customer/v1/customers/{customerId}/account-management/account-groups/{accountId} | Delete an account group
[**delete_mav**](AccountManagementApi.md#delete_mav) | **DELETE** /customer/v1/customers/{customerId}/account-management/mavs/{accountId} | Delete a MAV.
[**get_account**](AccountManagementApi.md#get_account) | **GET** /customer/v1/customers/{customerId}/account-management/accounts/{accountId} | Get an individual general account.
[**get_account_group_parent_assignment**](AccountManagementApi.md#get_account_group_parent_assignment) | **GET** /customer/v1/customers/{customerId}/account-management/parent-assignments/{parentAssignmentId} | Get an individual account group parent assignment.
[**get_account_group_parent_assignments**](AccountManagementApi.md#get_account_group_parent_assignments) | **GET** /customer/v1/customers/{customerId}/account-management/parent-assignments | Get all account group parent assignments.
[**get_general_accounts**](AccountManagementApi.md#get_general_accounts) | **GET** /customer/v1/customers/{customerId}/account-management/accounts | Get all general accounts.
[**get_group**](AccountManagementApi.md#get_group) | **GET** /customer/v1/customers/{customerId}/account-management/account-groups/{groupId} | Get an individual account group.
[**get_group_children**](AccountManagementApi.md#get_group_children) | **GET** /customer/v1/customers/{customerId}/account-management/account-groups/{groupId}/children | Get all children of an account group.
[**get_groups**](AccountManagementApi.md#get_groups) | **GET** /customer/v1/customers/{customerId}/account-management/account-groups | Get all account groups.
[**get_mav**](AccountManagementApi.md#get_mav) | **GET** /customer/v1/customers/{customerId}/account-management/mavs/{accountId} | Get an individual MAV.
[**get_mav_accounts**](AccountManagementApi.md#get_mav_accounts) | **GET** /customer/v1/customers/{customerId}/account-management/mavs | Get all MAVs.
[**get_mav_referenced_accounts**](AccountManagementApi.md#get_mav_referenced_accounts) | **GET** /customer/v1/customers/{customerId}/account-management/mavs/{accountId}/referenced-accounts | Get accounts associated with a MAV.
[**get_root_children**](AccountManagementApi.md#get_root_children) | **GET** /customer/v1/customers/{customerId}/account-management/account-groups/root/children | Get the root of the account hierarchy.
[**update_account**](AccountManagementApi.md#update_account) | **PUT** /customer/v1/customers/{customerId}/account-management/accounts/{accountId} | Update a General Account.
[**update_account_group**](AccountManagementApi.md#update_account_group) | **PUT** /customer/v1/customers/{customerId}/account-management/account-groups/{accountId} | Update an account group.
[**update_mav**](AccountManagementApi.md#update_mav) | **PUT** /customer/v1/customers/{customerId}/account-management/mavs/{accountId} | Update a MAV.

# **attach_account_groups**
> BulkAccountAssignmentResponseModelAccountAssignmentResponseModel attach_account_groups(customer_id, group_id, body=body)

Bulk move account groups into a parent account group.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
group_id = 'group_id_example' # str | 
body = cloudcheckr_cmx.BulkAccountAssignmentRequestModel() # BulkAccountAssignmentRequestModel |  (optional)

try:
    # Bulk move account groups into a parent account group.
    api_response = api_instance.attach_account_groups(customer_id, group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->attach_account_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **group_id** | **str**|  | 
 **body** | [**BulkAccountAssignmentRequestModel**](BulkAccountAssignmentRequestModel.md)|  | [optional] 

### Return type

[**BulkAccountAssignmentResponseModelAccountAssignmentResponseModel**](BulkAccountAssignmentResponseModelAccountAssignmentResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_account_groups_to_root**
> BulkAccountAssignmentResponseModelAccountAssignmentResponseModel attach_account_groups_to_root(customer_id, body=body)

Bulk move account groups into the root path.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.BulkAccountAssignmentRequestModel() # BulkAccountAssignmentRequestModel |  (optional)

try:
    # Bulk move account groups into the root path.
    api_response = api_instance.attach_account_groups_to_root(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->attach_account_groups_to_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**BulkAccountAssignmentRequestModel**](BulkAccountAssignmentRequestModel.md)|  | [optional] 

### Return type

[**BulkAccountAssignmentResponseModelAccountAssignmentResponseModel**](BulkAccountAssignmentResponseModelAccountAssignmentResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> GeneralAccountResponseModel create_account(customer_id, body=body)

Create a General Account.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.CreateRequestGeneralAccountRequestModel() # CreateRequestGeneralAccountRequestModel |  (optional)

try:
    # Create a General Account.
    api_response = api_instance.create_account(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**CreateRequestGeneralAccountRequestModel**](CreateRequestGeneralAccountRequestModel.md)|  | [optional] 

### Return type

[**GeneralAccountResponseModel**](GeneralAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_group**
> AccountGroupResponseModel create_account_group(customer_id, body=body)

Create a new account group.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.CreateRequestAccountGroupRequestModel() # CreateRequestAccountGroupRequestModel |  (optional)

try:
    # Create a new account group.
    api_response = api_instance.create_account_group(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->create_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**CreateRequestAccountGroupRequestModel**](CreateRequestAccountGroupRequestModel.md)|  | [optional] 

### Return type

[**AccountGroupResponseModel**](AccountGroupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mav**
> MavResponseModel create_mav(customer_id, body=body)

Create a MAV.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
body = cloudcheckr_cmx.CreateRequestMavRequestModel() # CreateRequestMavRequestModel |  (optional)

try:
    # Create a MAV.
    api_response = api_instance.create_mav(customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->create_mav: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **body** | [**CreateRequestMavRequestModel**](CreateRequestMavRequestModel.md)|  | [optional] 

### Return type

[**MavResponseModel**](MavResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> delete_account(customer_id, account_id)

Delete a general account.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Delete a general account.
    api_instance.delete_account(customer_id, account_id)
except ApiException as e:
    print("Exception when calling AccountManagementApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_group**
> delete_account_group(customer_id, account_id)

Delete an account group

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Delete an account group
    api_instance.delete_account_group(customer_id, account_id)
except ApiException as e:
    print("Exception when calling AccountManagementApi->delete_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mav**
> delete_mav(customer_id, account_id)

Delete a MAV.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Delete a MAV.
    api_instance.delete_mav(customer_id, account_id)
except ApiException as e:
    print("Exception when calling AccountManagementApi->delete_mav: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> GeneralAccountResponseModel get_account(customer_id, account_id)

Get an individual general account.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Get an individual general account.
    api_response = api_instance.get_account(customer_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**GeneralAccountResponseModel**](GeneralAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_group_parent_assignment**
> ParentAssignmentResponseModel get_account_group_parent_assignment(customer_id, parent_assignment_id)

Get an individual account group parent assignment.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
parent_assignment_id = 'parent_assignment_id_example' # str | 

try:
    # Get an individual account group parent assignment.
    api_response = api_instance.get_account_group_parent_assignment(customer_id, parent_assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_account_group_parent_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **parent_assignment_id** | **str**|  | 

### Return type

[**ParentAssignmentResponseModel**](ParentAssignmentResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_group_parent_assignments**
> PaginationWithCountResponseParentAssignmentResponseModel get_account_group_parent_assignments(customer_id, parent_assignment_ids=parent_assignment_ids)

Get all account group parent assignments.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
parent_assignment_ids = ['parent_assignment_ids_example'] # list[str] |  (optional)

try:
    # Get all account group parent assignments.
    api_response = api_instance.get_account_group_parent_assignments(customer_id, parent_assignment_ids=parent_assignment_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_account_group_parent_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **parent_assignment_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**PaginationWithCountResponseParentAssignmentResponseModel**](PaginationWithCountResponseParentAssignmentResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_accounts**
> PaginationWithCountResponseGeneralAccountResponseModel get_general_accounts(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)

Get all general accounts.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all general accounts.
    api_response = api_instance.get_general_accounts(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_general_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseGeneralAccountResponseModel**](PaginationWithCountResponseGeneralAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> AccountGroupResponseModel get_group(customer_id, group_id)

Get an individual account group.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
group_id = 'group_id_example' # str | 

try:
    # Get an individual account group.
    api_response = api_instance.get_group(customer_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

[**AccountGroupResponseModel**](AccountGroupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_children**
> PaginationWithCountResponseAccountGroupHierarchyResponseModel get_group_children(customer_id, group_id, page_size=page_size, pagination_key=pagination_key, search=search)

Get all children of an account group.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
group_id = 'group_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all children of an account group.
    api_response = api_instance.get_group_children(customer_id, group_id, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_group_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **group_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseAccountGroupHierarchyResponseModel**](PaginationWithCountResponseAccountGroupHierarchyResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> PaginationWithCountResponseAccountGroupResponseModel get_groups(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)

Get all account groups.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all account groups.
    api_response = api_instance.get_groups(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseAccountGroupResponseModel**](PaginationWithCountResponseAccountGroupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mav**
> MavResponseModel get_mav(customer_id, account_id)

Get an individual MAV.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    # Get an individual MAV.
    api_response = api_instance.get_mav(customer_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_mav: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**MavResponseModel**](MavResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mav_accounts**
> PaginationWithCountResponseMavResponseModel get_mav_accounts(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)

Get all MAVs.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get all MAVs.
    api_response = api_instance.get_mav_accounts(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_mav_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseMavResponseModel**](PaginationWithCountResponseMavResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mav_referenced_accounts**
> PaginationWithCountResponseReferencedAccountResponseModel get_mav_referenced_accounts(customer_id, account_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)

Get accounts associated with a MAV.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
order_by = 'order_by_example' # str | orders a given property (optional)

try:
    # Get accounts associated with a MAV.
    api_response = api_instance.get_mav_referenced_accounts(customer_id, account_id, page_size=page_size, pagination_key=pagination_key, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_mav_referenced_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **order_by** | **str**| orders a given property | [optional] 

### Return type

[**PaginationWithCountResponseReferencedAccountResponseModel**](PaginationWithCountResponseReferencedAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_children**
> PaginationWithCountResponseAccountGroupHierarchyResponseModel get_root_children(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)

Get the root of the account hierarchy.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
page_size = 56 # int | number of items to include in the response (optional)
pagination_key = 'pagination_key_example' # str | key used to fetch the next page of items (optional)
search = 'search_example' # str | finds all resources that match the specified value (optional)

try:
    # Get the root of the account hierarchy.
    api_response = api_instance.get_root_children(customer_id, page_size=page_size, pagination_key=pagination_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->get_root_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **page_size** | **int**| number of items to include in the response | [optional] 
 **pagination_key** | **str**| key used to fetch the next page of items | [optional] 
 **search** | **str**| finds all resources that match the specified value | [optional] 

### Return type

[**PaginationWithCountResponseAccountGroupHierarchyResponseModel**](PaginationWithCountResponseAccountGroupHierarchyResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> GeneralAccountResponseModel update_account(customer_id, account_id, body=body)

Update a General Account.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx.UpdateRequestGeneralAccountRequestModel() # UpdateRequestGeneralAccountRequestModel |  (optional)

try:
    # Update a General Account.
    api_response = api_instance.update_account(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestGeneralAccountRequestModel**](UpdateRequestGeneralAccountRequestModel.md)|  | [optional] 

### Return type

[**GeneralAccountResponseModel**](GeneralAccountResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_group**
> AccountGroupResponseModel update_account_group(customer_id, account_id, body=body)

Update an account group.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx.UpdateRequestAccountGroupRequestModel() # UpdateRequestAccountGroupRequestModel |  (optional)

try:
    # Update an account group.
    api_response = api_instance.update_account_group(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->update_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestAccountGroupRequestModel**](UpdateRequestAccountGroupRequestModel.md)|  | [optional] 

### Return type

[**AccountGroupResponseModel**](AccountGroupResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mav**
> MavResponseModel update_mav(customer_id, account_id, body=body)

Update a MAV.

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
api_instance = cloudcheckr_cmx.AccountManagementApi(cloudcheckr_cmx.ApiClient(configuration))
customer_id = 'customer_id_example' # str | 
account_id = 'account_id_example' # str | 
body = cloudcheckr_cmx.UpdateRequestMavRequestModel() # UpdateRequestMavRequestModel |  (optional)

try:
    # Update a MAV.
    api_response = api_instance.update_mav(customer_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountManagementApi->update_mav: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**UpdateRequestMavRequestModel**](UpdateRequestMavRequestModel.md)|  | [optional] 

### Return type

[**MavResponseModel**](MavResponseModel.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

