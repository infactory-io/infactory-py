# UserTeams

Represents a user_teams record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**team_id** | **str** |  | 
**role** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 
**team** | [**Teams**](Teams.md) |  | [optional] 
**user** | [**Users**](Users.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_teams import UserTeams

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeams from a JSON string
user_teams_instance = UserTeams.from_json(json)
# print the JSON string representation of the object
print(UserTeams.to_json())

# convert the object into a dict
user_teams_dict = user_teams_instance.to_dict()
# create an instance of UserTeams from a dict
user_teams_from_dict = UserTeams.from_dict(user_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


