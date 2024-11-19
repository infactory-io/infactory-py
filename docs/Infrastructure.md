# Infrastructure

Represents a infrastructure record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization_id** | **str** |  | [optional] 
**resources_allocated** | [**AnyOf**](AnyOf.md) |  | [optional] 
**limits** | [**AnyOf**](AnyOf.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**credentials** | [**List[Credentials]**](Credentials.md) |  | [optional] 
**organizations** | [**Organizations**](Organizations.md) |  | [optional] 

## Example

```python
from openapi_client.models.infrastructure import Infrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of Infrastructure from a JSON string
infrastructure_instance = Infrastructure.from_json(json)
# print the JSON string representation of the object
print(Infrastructure.to_json())

# convert the object into a dict
infrastructure_dict = infrastructure_instance.to_dict()
# create an instance of Infrastructure from a dict
infrastructure_from_dict = Infrastructure.from_dict(infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


