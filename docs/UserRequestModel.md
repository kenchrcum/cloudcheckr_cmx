# UserRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#x27;s email address. | 
**saml_provider** | [**UserSamlProviderRequestModel**](UserSamlProviderRequestModel.md) |  | [optional] 
**allowed_auth_types** | **list[str]** | The user&#x27;s allowed authorization types. | 
**organization_note** | **str** | The user&#x27;s organizational, shared note. | [optional] 
**personal_note** | **str** | The user&#x27;s personal note. | [optional] 
**roles** | [**list[BasicRequestListModification]**](BasicRequestListModification.md) | List of role ids to assign to the user. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

