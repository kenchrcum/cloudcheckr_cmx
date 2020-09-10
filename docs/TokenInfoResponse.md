# TokenInfoResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of authentication (authentication_entity). | [optional] 
**client_id** | **str** | The client ID from the token (client_id). | [optional] 
**user_id** | **str** | The user ID from the token (sub) | [optional] 
**roles** | **list[str]** | The roles associated with this token. | [optional] 
**version1_roles** | **list[str]** | The legacy roles associated with this token. | [optional] 
**customer_id** | **str** | The current customer ID (authz_customer_id). | [optional] 
**expiration** | **datetime** | The expiration date and time (exp). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


