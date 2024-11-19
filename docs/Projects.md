# Projects

This model contains row level security and requires additional setup for migrations. Visit https://pris.ly/d/row-level-security for more info.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**datasources** | [**List[Datasources]**](Datasources.md) |  | [optional] 
**events** | [**List[Events]**](Events.md) |  | [optional] 
**teams** | [**Teams**](Teams.md) |  | [optional] 
**tasks** | [**List[Tasks]**](Tasks.md) |  | [optional] 
**datalines** | [**List[Datalines]**](Datalines.md) |  | [optional] 

## Example

```python
from openapi_client.models.projects import Projects

# TODO update the JSON string below
json = "{}"
# create an instance of Projects from a JSON string
projects_instance = Projects.from_json(json)
# print the JSON string representation of the object
print(Projects.to_json())

# convert the object into a dict
projects_dict = projects_instance.to_dict()
# create an instance of Projects from a dict
projects_from_dict = Projects.from_dict(projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


