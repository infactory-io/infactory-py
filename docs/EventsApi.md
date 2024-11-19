# openapi_client.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_endpoint_v1_events_post**](EventsApi.md#create_event_endpoint_v1_events_post) | **POST** /v1/events/ | Create Event Endpoint
[**delete_event_endpoint_v1_events_event_id_delete**](EventsApi.md#delete_event_endpoint_v1_events_event_id_delete) | **DELETE** /v1/events/{event_id} | Delete Event Endpoint
[**get_event_endpoint_v1_events_event_id_get**](EventsApi.md#get_event_endpoint_v1_events_event_id_get) | **GET** /v1/events/{event_id} | Get Event Endpoint
[**get_events_endpoint_v1_events_project_project_id_get**](EventsApi.md#get_events_endpoint_v1_events_project_project_id_get) | **GET** /v1/events/project/{project_id} | Get Events Endpoint
[**update_event_endpoint_v1_events_event_id_patch**](EventsApi.md#update_event_endpoint_v1_events_event_id_patch) | **PATCH** /v1/events/{event_id} | Update Event Endpoint


# **create_event_endpoint_v1_events_post**
> Events create_event_endpoint_v1_events_post(event_type=event_type, description=description, timestamp=timestamp, project_id=project_id)

Create Event Endpoint

### Example


```python
import openapi_client
from openapi_client.models.events import Events
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    event_type = 'event_type_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    timestamp = 'timestamp_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)

    try:
        # Create Event Endpoint
        api_response = api_instance.create_event_endpoint_v1_events_post(event_type=event_type, description=description, timestamp=timestamp, project_id=project_id)
        print("The response of EventsApi->create_event_endpoint_v1_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_event_endpoint_v1_events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_endpoint_v1_events_event_id_delete**
> Events delete_event_endpoint_v1_events_event_id_delete(event_id)

Delete Event Endpoint

### Example


```python
import openapi_client
from openapi_client.models.events import Events
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Delete Event Endpoint
        api_response = api_instance.delete_event_endpoint_v1_events_event_id_delete(event_id)
        print("The response of EventsApi->delete_event_endpoint_v1_events_event_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_event_endpoint_v1_events_event_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_endpoint_v1_events_event_id_get**
> Events get_event_endpoint_v1_events_event_id_get(event_id)

Get Event Endpoint

### Example


```python
import openapi_client
from openapi_client.models.events import Events
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Event Endpoint
        api_response = api_instance.get_event_endpoint_v1_events_event_id_get(event_id)
        print("The response of EventsApi->get_event_endpoint_v1_events_event_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_endpoint_v1_events_event_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_endpoint_v1_events_project_project_id_get**
> List[Events] get_events_endpoint_v1_events_project_project_id_get(project_id)

Get Events Endpoint

### Example


```python
import openapi_client
from openapi_client.models.events import Events
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Events Endpoint
        api_response = api_instance.get_events_endpoint_v1_events_project_project_id_get(project_id)
        print("The response of EventsApi->get_events_endpoint_v1_events_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events_endpoint_v1_events_project_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[Events]**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_endpoint_v1_events_event_id_patch**
> Events update_event_endpoint_v1_events_event_id_patch(event_id, event_type=event_type, description=description, timestamp=timestamp)

Update Event Endpoint

### Example


```python
import openapi_client
from openapi_client.models.events import Events
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    event_id = 'event_id_example' # str | 
    event_type = 'event_type_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    timestamp = 'timestamp_example' # str |  (optional)

    try:
        # Update Event Endpoint
        api_response = api_instance.update_event_endpoint_v1_events_event_id_patch(event_id, event_type=event_type, description=description, timestamp=timestamp)
        print("The response of EventsApi->update_event_endpoint_v1_events_event_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->update_event_endpoint_v1_events_event_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **event_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

