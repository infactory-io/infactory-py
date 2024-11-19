# Datalines

This model contains row level security and requires additional setup for migrations. Visit https://pris.ly/d/row-level-security for more info.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**dataobject_id** | **str** |  | [optional] 
**schema_code** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**dataobjects** | [**Dataobjects**](Dataobjects.md) |  | [optional] 
**projects** | [**Projects**](Projects.md) |  | [optional] 
**queryprograms** | [**List[Queryprograms]**](Queryprograms.md) |  | [optional] 

## Example

```python
from openapi_client.models.datalines import Datalines

# TODO update the JSON string below
json = "{}"
# create an instance of Datalines from a JSON string
datalines_instance = Datalines.from_json(json)
# print the JSON string representation of the object
print(Datalines.to_json())

# convert the object into a dict
datalines_dict = datalines_instance.to_dict()
# create an instance of Datalines from a dict
datalines_from_dict = Datalines.from_dict(datalines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


