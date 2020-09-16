# UserResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#x27;s unique ID. | [optional] 
**customer_id** | **str** | The ID of the customer that manages the user. | [optional] 
**roles** | [**list[MappedRoleResponseModel]**](MappedRoleResponseModel.md) | The roles that are assigned to the user. | [optional] 
**email** | **str** | The user&#x27;s email address. This property supports: sorting and filtering. | [optional] 
**saml_provider** | [**UserSamlProviderResponseModel**](UserSamlProviderResponseModel.md) |  | [optional] 
**allowed_auth_types** | **list[str]** | The user&#x27;s allowed authorization types. | [optional] 
**created_date** | **datetime** | The user&#x27;s creation date. This property supports: sorting and filtering. | [optional] 
**last_login_date** | **datetime** | The user&#x27;s last login date. This property supports: sorting and filtering. | [optional] 
**is_activated** | **bool** | The user&#x27;s activation status. Some actions may be limited if the user is inactive. This property supports: filtering. | [optional] 
**organization_note** | **str** | The user&#x27;s organizational, shared note. | [optional] 
**personal_note** | **str** | The user&#x27;s personal note. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

