# Datasources

This model contains row level security and requires additional setup for migrations. Visit https://pris.ly/d/row-level-security for more info.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**credentials** | [**List[Credentials]**](Credentials.md) |  | [optional] 
**dataobjects** | [**List[Dataobjects]**](Dataobjects.md) |  | [optional] 
**projects** | [**Projects**](Projects.md) |  | [optional] 

## Example

```python
from openapi_client.models.datasources import Datasources

# TODO update the JSON string below
json = "{}"
# create an instance of Datasources from a JSON string
datasources_instance = Datasources.from_json(json)
# print the JSON string representation of the object
print(Datasources.to_json())

# convert the object into a dict
datasources_dict = datasources_instance.to_dict()
# create an instance of Datasources from a dict
datasources_from_dict = Datasources.from_dict(datasources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


