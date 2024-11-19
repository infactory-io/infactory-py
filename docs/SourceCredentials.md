# SourceCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_key_id** | **str** |  | 
**aws_secret_access_key** | **str** |  | 

## Example

```python
from openapi_client.models.source_credentials import SourceCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCredentials from a JSON string
source_credentials_instance = SourceCredentials.from_json(json)
# print the JSON string representation of the object
print(SourceCredentials.to_json())

# convert the object into a dict
source_credentials_dict = source_credentials_instance.to_dict()
# create an instance of SourceCredentials from a dict
source_credentials_from_dict = SourceCredentials.from_dict(source_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


