# ClientCreateRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_access_key** | **bool** | Controls whether or not to create an access key for the client. | [optional] 
**access_key_name** | **str** | The name that the access key will be assigned. | [optional] 
**access_key_valid_days** | **int** | The number of days until the access key will expire. | [optional] 
**name** | **str** | The client&#x27;s name. | 
**description** | **str** | The client&#x27;s description. This property supports: resetting. | [optional] 
**type** | **str** | The type of client. | 
**roles** | [**list[BasicRequestListModification]**](BasicRequestListModification.md) | List of role ids to assign to the user. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

