# UserCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_create_input import UserCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateInput from a JSON string
user_create_input_instance = UserCreateInput.from_json(json)
# print the JSON string representation of the object
print(UserCreateInput.to_json())

# convert the object into a dict
user_create_input_dict = user_create_input_instance.to_dict()
# create an instance of UserCreateInput from a dict
user_create_input_from_dict = UserCreateInput.from_dict(user_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


