# Datalineage

Represents a datalineage record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upstream_id** | **str** |  | [optional] 
**downstream_id** | **str** |  | [optional] 
**transformation** | **str** |  | [optional] 
**metadata** | [**AnyOf**](AnyOf.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**downstream** | [**Dataobjects**](Dataobjects.md) |  | [optional] 
**upstream** | [**Dataobjects**](Dataobjects.md) |  | [optional] 

## Example

```python
from openapi_client.models.datalineage import Datalineage

# TODO update the JSON string below
json = "{}"
# create an instance of Datalineage from a JSON string
datalineage_instance = Datalineage.from_json(json)
# print the JSON string representation of the object
print(Datalineage.to_json())

# convert the object into a dict
datalineage_dict = datalineage_instance.to_dict()
# create an instance of Datalineage from a dict
datalineage_from_dict = Datalineage.from_dict(datalineage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


