# Credentials

Represents a credentials record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | [**AnyOf**](AnyOf.md) |  | [optional] 
**datasource_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**datasources** | [**Datasources**](Datasources.md) |  | [optional] 
**infrastructure** | [**Infrastructure**](Infrastructure.md) |  | [optional] 
**organizations** | [**Organizations**](Organizations.md) |  | [optional] 
**teams** | [**Teams**](Teams.md) |  | [optional] 
**secrets** | [**List[Secrets]**](Secrets.md) |  | [optional] 

## Example

```python
from openapi_client.models.credentials import Credentials

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials from a JSON string
credentials_instance = Credentials.from_json(json)
# print the JSON string representation of the object
print(Credentials.to_json())

# convert the object into a dict
credentials_dict = credentials_instance.to_dict()
# create an instance of Credentials from a dict
credentials_from_dict = Credentials.from_dict(credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


