# SamlProviderRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the SAML provider. | [optional] 
**idp_metadata** | **str** | The IdpMetadata for the given provider. | [optional] 
**permitted_child_customers** | [**list[BasicRequestListModification]**](BasicRequestListModification.md) | A list of the customers which will be permitted to use this SAML provider to authenticate. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

