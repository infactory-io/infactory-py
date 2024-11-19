# Rbac

Represents a rbac record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role_name** | **str** |  | [optional] 
**permissions** | [**AnyOf**](AnyOf.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**teams** | [**Teams**](Teams.md) |  | [optional] 
**users** | [**Users**](Users.md) |  | [optional] 

## Example

```python
from openapi_client.models.rbac import Rbac

# TODO update the JSON string below
json = "{}"
# create an instance of Rbac from a JSON string
rbac_instance = Rbac.from_json(json)
# print the JSON string representation of the object
print(Rbac.to_json())

# convert the object into a dict
rbac_dict = rbac_instance.to_dict()
# create an instance of Rbac from a dict
rbac_from_dict = Rbac.from_dict(rbac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


