# openapi_client.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_endpoint_v1_tasks_post**](TasksApi.md#create_task_endpoint_v1_tasks_post) | **POST** /v1/tasks/ | Create Task Endpoint
[**delete_task_endpoint_v1_tasks_task_id_delete**](TasksApi.md#delete_task_endpoint_v1_tasks_task_id_delete) | **DELETE** /v1/tasks/{task_id} | Delete Task Endpoint
[**get_task_endpoint_v1_tasks_task_id_get**](TasksApi.md#get_task_endpoint_v1_tasks_task_id_get) | **GET** /v1/tasks/{task_id} | Get Task Endpoint
[**get_tasks_endpoint_v1_tasks_project_project_id_get**](TasksApi.md#get_tasks_endpoint_v1_tasks_project_project_id_get) | **GET** /v1/tasks/project/{project_id} | Get Tasks Endpoint
[**update_task_endpoint_v1_tasks_task_id_patch**](TasksApi.md#update_task_endpoint_v1_tasks_task_id_patch) | **PATCH** /v1/tasks/{task_id} | Update Task Endpoint


# **create_task_endpoint_v1_tasks_post**
> Tasks create_task_endpoint_v1_tasks_post(task_type=task_type, status=status, schedule=schedule, project_id=project_id)

Create Task Endpoint

### Example


```python
import openapi_client
from openapi_client.models.tasks import Tasks
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
    api_instance = openapi_client.TasksApi(api_client)
    task_type = 'task_type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    schedule = 'schedule_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)

    try:
        # Create Task Endpoint
        api_response = api_instance.create_task_endpoint_v1_tasks_post(task_type=task_type, status=status, schedule=schedule, project_id=project_id)
        print("The response of TasksApi->create_task_endpoint_v1_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_task_endpoint_v1_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **schedule** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 

### Return type

[**Tasks**](Tasks.md)

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

# **delete_task_endpoint_v1_tasks_task_id_delete**
> Tasks delete_task_endpoint_v1_tasks_task_id_delete(task_id)

Delete Task Endpoint

### Example


```python
import openapi_client
from openapi_client.models.tasks import Tasks
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Delete Task Endpoint
        api_response = api_instance.delete_task_endpoint_v1_tasks_task_id_delete(task_id)
        print("The response of TasksApi->delete_task_endpoint_v1_tasks_task_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task_endpoint_v1_tasks_task_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**Tasks**](Tasks.md)

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

# **get_task_endpoint_v1_tasks_task_id_get**
> Tasks get_task_endpoint_v1_tasks_task_id_get(task_id)

Get Task Endpoint

### Example


```python
import openapi_client
from openapi_client.models.tasks import Tasks
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Task Endpoint
        api_response = api_instance.get_task_endpoint_v1_tasks_task_id_get(task_id)
        print("The response of TasksApi->get_task_endpoint_v1_tasks_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_endpoint_v1_tasks_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**Tasks**](Tasks.md)

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

# **get_tasks_endpoint_v1_tasks_project_project_id_get**
> List[Tasks] get_tasks_endpoint_v1_tasks_project_project_id_get(project_id)

Get Tasks Endpoint

### Example


```python
import openapi_client
from openapi_client.models.tasks import Tasks
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
    api_instance = openapi_client.TasksApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Tasks Endpoint
        api_response = api_instance.get_tasks_endpoint_v1_tasks_project_project_id_get(project_id)
        print("The response of TasksApi->get_tasks_endpoint_v1_tasks_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_endpoint_v1_tasks_project_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[Tasks]**](Tasks.md)

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

# **update_task_endpoint_v1_tasks_task_id_patch**
> Tasks update_task_endpoint_v1_tasks_task_id_patch(task_id, task_type=task_type, status=status, schedule=schedule)

Update Task Endpoint

### Example


```python
import openapi_client
from openapi_client.models.tasks import Tasks
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
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    task_type = 'task_type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    schedule = 'schedule_example' # str |  (optional)

    try:
        # Update Task Endpoint
        api_response = api_instance.update_task_endpoint_v1_tasks_task_id_patch(task_id, task_type=task_type, status=status, schedule=schedule)
        print("The response of TasksApi->update_task_endpoint_v1_tasks_task_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task_endpoint_v1_tasks_task_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **task_type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **schedule** | **str**|  | [optional] 

### Return type

[**Tasks**](Tasks.md)

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

