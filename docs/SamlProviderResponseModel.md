# SamlProviderResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The SAML provider&#39;s ID. | [optional] 
**name** | **str** | The SAML provider&#39;s name. This property supports: filtering and sorting. | [optional] 
**default_role** | **str** | The SAML provider&#39;s default role. This property supports: filtering and sorting. | [optional] 
**saml_issuer** | **str** | The SAML provider&#39;s issuer. This property supports: filtering and sorting. | [optional] 
**permitted_child_customers** | [**list[PermittedChildCustomerModel]**](PermittedChildCustomerModel.md) | The L2 customers allowed to use this L1 SAML provider. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


