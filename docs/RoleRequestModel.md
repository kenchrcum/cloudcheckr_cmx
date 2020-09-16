# RoleRequestModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The role&#x27;s name. | 
**description** | **str** | The role&#x27;s description. This property supports: resetting. | [optional] 
**permission_sets** | [**list[BasicRequestListModification]**](BasicRequestListModification.md) | The role&#x27;s permission sets. This property supports: resetting. | [optional] 
**customer_account_access_rule** | **str** | The role&#x27;s access rule. This controls how customer and account access is determined. | [optional] 
**customer_accounts** | [**list[CustomerAccountModification]**](CustomerAccountModification.md) | The customers and/or accounts to which the role grants access. This property supports: resetting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

