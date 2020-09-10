# ParentAssignmentResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The parent assignment&#39;s ID. | [optional] 
**state** | **str** | The parent assignment&#39;s state. | [optional] 
**new_parent** | **str** | The new parent&#39;s ID. Excluded if there is no parent. | [optional] 
**date_started** | **datetime** | The date in which the parent assignment was started. | [optional] 
**date_requested** | **datetime** | The date in which the parent assignment was requested. | [optional] 
**date_last_activity** | **datetime** | The date in which the parent assignment was last updated. | [optional] 
**date_completed** | **datetime** | The date in which the parent assignment completed. | [optional] 
**error_message** | **str** | The error message if parent movement was unsuccessful. | [optional] 
**correlation_id** | **str** | The request&#39;s correlation ID. | [optional] 
**target_account_group_id** | **str** | The parent assignment&#39;s target account group. | [optional] 
**target_expected_parent** | **str** | The expected parent ID when the assignment is completed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


