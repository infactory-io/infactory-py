# Teams

Represents a teams record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**credentials** | [**List[Credentials]**](Credentials.md) |  | [optional] 
**projects** | [**List[Projects]**](Projects.md) |  | [optional] 
**rbac** | [**List[Rbac]**](Rbac.md) |  | [optional] 
**secrets** | [**List[Secrets]**](Secrets.md) |  | [optional] 
**organizations** | [**Organizations**](Organizations.md) |  | [optional] 
**user_teams** | [**List[UserTeams]**](UserTeams.md) |  | [optional] 

## Example

```python
from openapi_client.models.teams import Teams

# TODO update the JSON string below
json = "{}"
# create an instance of Teams from a JSON string
teams_instance = Teams.from_json(json)
# print the JSON string representation of the object
print(Teams.to_json())

# convert the object into a dict
teams_dict = teams_instance.to_dict()
# create an instance of Teams from a dict
teams_from_dict = Teams.from_dict(teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


