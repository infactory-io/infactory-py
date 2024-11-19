# CredentialCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**datasource_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.credential_create import CredentialCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreate from a JSON string
credential_create_instance = CredentialCreate.from_json(json)
# print the JSON string representation of the object
print(CredentialCreate.to_json())

# convert the object into a dict
credential_create_dict = credential_create_instance.to_dict()
# create an instance of CredentialCreate from a dict
credential_create_from_dict = CredentialCreate.from_dict(credential_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


