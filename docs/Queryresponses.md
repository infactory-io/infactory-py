# Queryresponses

Represents a queryresponses record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**queryprogram_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**queryprograms** | [**Queryprograms**](Queryprograms.md) |  | [optional] 

## Example

```python
from openapi_client.models.queryresponses import Queryresponses

# TODO update the JSON string below
json = "{}"
# create an instance of Queryresponses from a JSON string
queryresponses_instance = Queryresponses.from_json(json)
# print the JSON string representation of the object
print(Queryresponses.to_json())

# convert the object into a dict
queryresponses_dict = queryresponses_instance.to_dict()
# create an instance of Queryresponses from a dict
queryresponses_from_dict = Queryresponses.from_dict(queryresponses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


