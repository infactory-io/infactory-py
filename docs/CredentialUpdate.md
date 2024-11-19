# CredentialUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.credential_update import CredentialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialUpdate from a JSON string
credential_update_instance = CredentialUpdate.from_json(json)
# print the JSON string representation of the object
print(CredentialUpdate.to_json())

# convert the object into a dict
credential_update_dict = credential_update_instance.to_dict()
# create an instance of CredentialUpdate from a dict
credential_update_from_dict = CredentialUpdate.from_dict(credential_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


