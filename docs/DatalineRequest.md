# DatalineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_name** | **str** |  | 
**dataset_name** | **str** |  | 

## Example

```python
from openapi_client.models.dataline_request import DatalineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatalineRequest from a JSON string
dataline_request_instance = DatalineRequest.from_json(json)
# print the JSON string representation of the object
print(DatalineRequest.to_json())

# convert the object into a dict
dataline_request_dict = dataline_request_instance.to_dict()
# create an instance of DatalineRequest from a dict
dataline_request_from_dict = DatalineRequest.from_dict(dataline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


