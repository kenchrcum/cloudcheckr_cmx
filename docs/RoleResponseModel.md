# RoleResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The role&#39;s ID. | [optional] 
**name** | **str** | The role&#39;s name. This property supports: sorting. | [optional] 
**description** | **str** | The role&#39;s description. | [optional] 
**customer_account_access_rule** | **str** | The role&#39;s access rule. This controls how customer and account access is determined. | [optional] 
**permission_sets** | [**list[PermissionSetBasicInfo]**](PermissionSetBasicInfo.md) | The role&#39;s permission sets. | [optional] 
**customer_accounts** | [**list[CustomerAccountBasicInfo]**](CustomerAccountBasicInfo.md) | The customers and/or accounts to which the role grants access. | [optional] 
**created_date** | **datetime** | The role&#39;s creation date. | [optional] 
**updated_date** | **datetime** | The role&#39;s last updated date. | [optional] 
**owned_by** | **str** | The role&#39;s owner. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


