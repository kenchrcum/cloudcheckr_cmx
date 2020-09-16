# SamlProviderResponseDetailModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** | Metadata document for this identity provider. | [optional] 
**metadata_state** | **str** | The state of the metadata. | [optional] 
**id** | **str** | The SAML provider&#x27;s ID. | [optional] 
**name** | **str** | The SAML provider&#x27;s name. This property supports: filtering and sorting. | [optional] 
**default_role** | **str** | The SAML provider&#x27;s default role. This property supports: filtering and sorting. | [optional] 
**saml_issuer** | **str** | The SAML provider&#x27;s issuer. This property supports: filtering and sorting. | [optional] 
**permitted_child_customers** | [**list[PermittedChildCustomerModel]**](PermittedChildCustomerModel.md) | The L2 customers allowed to use this L1 SAML provider. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

