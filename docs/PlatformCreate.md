# PlatformCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.platform_create import PlatformCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformCreate from a JSON string
platform_create_instance = PlatformCreate.from_json(json)
# print the JSON string representation of the object
print(PlatformCreate.to_json())

# convert the object into a dict
platform_create_dict = platform_create_instance.to_dict()
# create an instance of PlatformCreate from a dict
platform_create_from_dict = PlatformCreate.from_dict(platform_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


