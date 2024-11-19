# Queryprograms

This model contains row level security and requires additional setup for migrations. Visit https://pris.ly/d/row-level-security for more info.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**dataline_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**dataobject_id** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**query_program** | **str** |  | [optional] 
**datalines** | [**Datalines**](Datalines.md) |  | [optional] 
**dataobjects** | [**Dataobjects**](Dataobjects.md) |  | [optional] 
**queryresponses** | [**List[Queryresponses]**](Queryresponses.md) |  | [optional] 

## Example

```python
from openapi_client.models.queryprograms import Queryprograms

# TODO update the JSON string below
json = "{}"
# create an instance of Queryprograms from a JSON string
queryprograms_instance = Queryprograms.from_json(json)
# print the JSON string representation of the object
print(Queryprograms.to_json())

# convert the object into a dict
queryprograms_dict = queryprograms_instance.to_dict()
# create an instance of Queryprograms from a dict
queryprograms_from_dict = Queryprograms.from_dict(queryprograms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


