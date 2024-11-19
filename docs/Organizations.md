# Organizations

Represents a organizations record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**platform_id** | **str** |  | [optional] 
**credentials** | [**List[Credentials]**](Credentials.md) |  | [optional] 
**infrastructure** | [**List[Infrastructure]**](Infrastructure.md) |  | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**teams** | [**List[Teams]**](Teams.md) |  | [optional] 
**users** | [**List[Users]**](Users.md) |  | [optional] 
**clerk_org_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.organizations import Organizations

# TODO update the JSON string below
json = "{}"
# create an instance of Organizations from a JSON string
organizations_instance = Organizations.from_json(json)
# print the JSON string representation of the object
print(Organizations.to_json())

# convert the object into a dict
organizations_dict = organizations_instance.to_dict()
# create an instance of Organizations from a dict
organizations_from_dict = Organizations.from_dict(organizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


