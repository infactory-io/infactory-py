# AskDatalineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_name** | **str** |  | 
**dataset_name** | **str** |  | 
**query** | **str** |  | 

## Example

```python
from openapi_client.models.ask_dataline_request import AskDatalineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskDatalineRequest from a JSON string
ask_dataline_request_instance = AskDatalineRequest.from_json(json)
# print the JSON string representation of the object
print(AskDatalineRequest.to_json())

# convert the object into a dict
ask_dataline_request_dict = ask_dataline_request_instance.to_dict()
# create an instance of AskDatalineRequest from a dict
ask_dataline_request_from_dict = AskDatalineRequest.from_dict(ask_dataline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


