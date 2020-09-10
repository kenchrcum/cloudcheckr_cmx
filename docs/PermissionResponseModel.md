# PermissionResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The permission&#39;s ID. This property supports: filtering. | [optional] 
**name** | **str** | The permission&#39;s name. This property supports: sorting and filtering. | [optional] 
**description** | **str** | The permission&#39;s description. This property supports: sorting and filtering. | [optional] 
**display_grouping** | [**PermissionGroupModel**](PermissionGroupModel.md) | The full path of the the permission&#39;s grouping. Example: /Administration/User Management. This property supports: sorting and filtering. | [optional] 
**related_permissions** | [**list[RelatedPermissionModel]**](RelatedPermissionModel.md) | The related permissions that are included or excluded by this permission. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


