# Secrets

Represents a secrets record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**credentials_id** | **str** |  | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**teams** | [**Teams**](Teams.md) |  | [optional] 

## Example

```python
from openapi_client.models.secrets import Secrets

# TODO update the JSON string below
json = "{}"
# create an instance of Secrets from a JSON string
secrets_instance = Secrets.from_json(json)
# print the JSON string representation of the object
print(Secrets.to_json())

# convert the object into a dict
secrets_dict = secrets_instance.to_dict()
# create an instance of Secrets from a dict
secrets_from_dict = Secrets.from_dict(secrets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


