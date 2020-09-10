# AccountGroupSearchResponseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_account_id** | **str** | The legacy account&#39;s ID. | [optional] 
**provider_identifier** | **str** | The account&#39;s cloud provider identifier. | [optional] 
**provider_sub_type** | **str** | The account&#39;s cloud provider sub-type. | [optional] 
**provider_payment_type** | **str** | The account&#39;s payment model. | [optional] 
**payer_identifier** | **str** | The account&#39;s payer identifier. | [optional] 
**parent** | [**BaseAccountInfo**](BaseAccountInfo.md) | The account group&#39;s parent. | [optional] 
**grandparent** | [**BaseAccountInfo**](BaseAccountInfo.md) | The account group&#39;s grandparent. | [optional] 
**include_all_accounts** | **bool** | True if all accounts are included. Only applicable to MAVs. | [optional] 
**associated_account_attributes** | [**list[AccountAttributeBasicInfo]**](AccountAttributeBasicInfo.md) | List of associated account attributes. | [optional] 
**has_children** | **bool** | Determines if the account group has children. | [optional] 
**type** | **str** | The account group&#39;s type. Valid types are General, Group, and MAV. This property supports: sorting. | [optional] 
**provider** | **str** | The account&#39;s cloud provider. | [optional] 
**has_pending_change** | **bool** | True if the account has a pending change. | [optional] 
**id** | **str** | The account&#39;s ID. | [optional] 
**name** | **str** | The account&#39;s name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


