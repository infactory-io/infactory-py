# openapi_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_endpoint_v1_projects_team_id_post**](ProjectsApi.md#create_project_endpoint_v1_projects_team_id_post) | **POST** /v1/projects/{team_id} | Create Project Endpoint
[**delete_project_endpoint_v1_projects_team_id_project_id_delete**](ProjectsApi.md#delete_project_endpoint_v1_projects_team_id_project_id_delete) | **DELETE** /v1/projects/{team_id}/{project_id} | Delete Project Endpoint
[**get_project_endpoint_v1_projects_team_id_project_id_get**](ProjectsApi.md#get_project_endpoint_v1_projects_team_id_project_id_get) | **GET** /v1/projects/{team_id}/{project_id} | Get Project Endpoint
[**get_projects_endpoint_v1_projects_team_id_get**](ProjectsApi.md#get_projects_endpoint_v1_projects_team_id_get) | **GET** /v1/projects/{team_id} | Get Projects Endpoint
[**move_project_endpoint_v1_projects_team_id_project_id_move_post**](ProjectsApi.md#move_project_endpoint_v1_projects_team_id_project_id_move_post) | **POST** /v1/projects/{team_id}/{project_id}/move | Move Project Endpoint
[**update_project_endpoint_v1_projects_team_id_project_id_patch**](ProjectsApi.md#update_project_endpoint_v1_projects_team_id_project_id_patch) | **PATCH** /v1/projects/{team_id}/{project_id} | Update Project Endpoint


# **create_project_endpoint_v1_projects_team_id_post**
> Projects create_project_endpoint_v1_projects_team_id_post(team_id, name=name, description=description)

Create Project Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    team_id = 'team_id_example' # str | 
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)

    try:
        # Create Project Endpoint
        api_response = api_instance.create_project_endpoint_v1_projects_team_id_post(team_id, name=name, description=description)
        print("The response of ProjectsApi->create_project_endpoint_v1_projects_team_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_endpoint_v1_projects_team_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**Projects**](Projects.md)

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

# **delete_project_endpoint_v1_projects_team_id_project_id_delete**
> Projects delete_project_endpoint_v1_projects_team_id_project_id_delete(project_id, permanent=permanent)

Delete Project Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    permanent = False # bool |  (optional) (default to False)

    try:
        # Delete Project Endpoint
        api_response = api_instance.delete_project_endpoint_v1_projects_team_id_project_id_delete(project_id, permanent=permanent)
        print("The response of ProjectsApi->delete_project_endpoint_v1_projects_team_id_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_endpoint_v1_projects_team_id_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **permanent** | **bool**|  | [optional] [default to False]

### Return type

[**Projects**](Projects.md)

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

# **get_project_endpoint_v1_projects_team_id_project_id_get**
> Projects get_project_endpoint_v1_projects_team_id_project_id_get(project_id, team_id)

Get Project Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    team_id = 'team_id_example' # str | 

    try:
        # Get Project Endpoint
        api_response = api_instance.get_project_endpoint_v1_projects_team_id_project_id_get(project_id, team_id)
        print("The response of ProjectsApi->get_project_endpoint_v1_projects_team_id_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_endpoint_v1_projects_team_id_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **team_id** | **str**|  | 

### Return type

[**Projects**](Projects.md)

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

# **get_projects_endpoint_v1_projects_team_id_get**
> List[Projects] get_projects_endpoint_v1_projects_team_id_get(team_id, include_deleted=include_deleted)

Get Projects Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    team_id = 'team_id_example' # str | 
    include_deleted = False # bool |  (optional) (default to False)

    try:
        # Get Projects Endpoint
        api_response = api_instance.get_projects_endpoint_v1_projects_team_id_get(team_id, include_deleted=include_deleted)
        print("The response of ProjectsApi->get_projects_endpoint_v1_projects_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_endpoint_v1_projects_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to False]

### Return type

[**List[Projects]**](Projects.md)

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

# **move_project_endpoint_v1_projects_team_id_project_id_move_post**
> Projects move_project_endpoint_v1_projects_team_id_project_id_move_post(project_id, new_team_id)

Move Project Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    new_team_id = 'new_team_id_example' # str | 

    try:
        # Move Project Endpoint
        api_response = api_instance.move_project_endpoint_v1_projects_team_id_project_id_move_post(project_id, new_team_id)
        print("The response of ProjectsApi->move_project_endpoint_v1_projects_team_id_project_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->move_project_endpoint_v1_projects_team_id_project_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **new_team_id** | **str**|  | 

### Return type

[**Projects**](Projects.md)

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

# **update_project_endpoint_v1_projects_team_id_project_id_patch**
> Projects update_project_endpoint_v1_projects_team_id_project_id_patch(team_id, project_id, name=name, description=description, deleted_at=deleted_at)

Update Project Endpoint

### Example


```python
import openapi_client
from openapi_client.models.projects import Projects
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
    api_instance = openapi_client.ProjectsApi(api_client)
    team_id = 'team_id_example' # str | 
    project_id = 'project_id_example' # str | 
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    deleted_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Update Project Endpoint
        api_response = api_instance.update_project_endpoint_v1_projects_team_id_project_id_patch(team_id, project_id, name=name, description=description, deleted_at=deleted_at)
        print("The response of ProjectsApi->update_project_endpoint_v1_projects_team_id_project_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_endpoint_v1_projects_team_id_project_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **project_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **deleted_at** | **datetime**|  | [optional] 

### Return type

[**Projects**](Projects.md)

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

