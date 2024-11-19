# Dataobjects

Represents a dataobjects record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**bucket** | **str** |  | 
**key** | **str** |  | 
**file_type** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**etag** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**metadata** | [**AnyOf**](AnyOf.md) |  | [optional] 
**datasource_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**downstream_lineage** | [**List[Datalineage]**](Datalineage.md) |  | [optional] 
**upstream_lineage** | [**List[Datalineage]**](Datalineage.md) |  | [optional] 
**datalines** | [**List[Datalines]**](Datalines.md) |  | [optional] 
**datasources** | [**Datasources**](Datasources.md) |  | [optional] 
**queryprograms** | [**List[Queryprograms]**](Queryprograms.md) |  | [optional] 

## Example

```python
from openapi_client.models.dataobjects import Dataobjects

# TODO update the JSON string below
json = "{}"
# create an instance of Dataobjects from a JSON string
dataobjects_instance = Dataobjects.from_json(json)
# print the JSON string representation of the object
print(Dataobjects.to_json())

# convert the object into a dict
dataobjects_dict = dataobjects_instance.to_dict()
# create an instance of Dataobjects from a dict
dataobjects_from_dict = Dataobjects.from_dict(dataobjects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


