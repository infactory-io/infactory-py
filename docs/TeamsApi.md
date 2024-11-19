# openapi_client.TeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_endpoint_v1_teams_post**](TeamsApi.md#create_team_endpoint_v1_teams_post) | **POST** /v1/teams/ | Create Team Endpoint
[**delete_team_endpoint_v1_teams_team_id_delete**](TeamsApi.md#delete_team_endpoint_v1_teams_team_id_delete) | **DELETE** /v1/teams/{team_id} | Delete Team Endpoint
[**get_team_endpoint_v1_teams_team_id_get**](TeamsApi.md#get_team_endpoint_v1_teams_team_id_get) | **GET** /v1/teams/{team_id} | Get Team Endpoint
[**get_teams_endpoint_v1_teams_get**](TeamsApi.md#get_teams_endpoint_v1_teams_get) | **GET** /v1/teams/ | Get Teams Endpoint
[**move_team_endpoint_v1_teams_team_id_move_post**](TeamsApi.md#move_team_endpoint_v1_teams_team_id_move_post) | **POST** /v1/teams/{team_id}/move | Move Team Endpoint
[**update_team_endpoint_v1_teams_team_id_patch**](TeamsApi.md#update_team_endpoint_v1_teams_team_id_patch) | **PATCH** /v1/teams/{team_id} | Update Team Endpoint


# **create_team_endpoint_v1_teams_post**
> Teams create_team_endpoint_v1_teams_post(name=name, organization_id=organization_id)

Create Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    name = 'name_example' # str |  (optional)
    organization_id = 'organization_id_example' # str |  (optional)

    try:
        # Create Team Endpoint
        api_response = api_instance.create_team_endpoint_v1_teams_post(name=name, organization_id=organization_id)
        print("The response of TeamsApi->create_team_endpoint_v1_teams_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->create_team_endpoint_v1_teams_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **organization_id** | **str**|  | [optional] 

### Return type

[**Teams**](Teams.md)

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

# **delete_team_endpoint_v1_teams_team_id_delete**
> Teams delete_team_endpoint_v1_teams_team_id_delete(team_id)

Delete Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Delete Team Endpoint
        api_response = api_instance.delete_team_endpoint_v1_teams_team_id_delete(team_id)
        print("The response of TeamsApi->delete_team_endpoint_v1_teams_team_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->delete_team_endpoint_v1_teams_team_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**Teams**](Teams.md)

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

# **get_team_endpoint_v1_teams_team_id_get**
> Teams get_team_endpoint_v1_teams_team_id_get(team_id)

Get Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Get Team Endpoint
        api_response = api_instance.get_team_endpoint_v1_teams_team_id_get(team_id)
        print("The response of TeamsApi->get_team_endpoint_v1_teams_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_endpoint_v1_teams_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**Teams**](Teams.md)

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

# **get_teams_endpoint_v1_teams_get**
> List[Teams] get_teams_endpoint_v1_teams_get(organization_id)

Get Teams Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Teams Endpoint
        api_response = api_instance.get_teams_endpoint_v1_teams_get(organization_id)
        print("The response of TeamsApi->get_teams_endpoint_v1_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams_endpoint_v1_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[Teams]**](Teams.md)

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

# **move_team_endpoint_v1_teams_team_id_move_post**
> Teams move_team_endpoint_v1_teams_team_id_move_post(team_id, new_organization_id)

Move Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 
    new_organization_id = 'new_organization_id_example' # str | 

    try:
        # Move Team Endpoint
        api_response = api_instance.move_team_endpoint_v1_teams_team_id_move_post(team_id, new_organization_id)
        print("The response of TeamsApi->move_team_endpoint_v1_teams_team_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->move_team_endpoint_v1_teams_team_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **new_organization_id** | **str**|  | 

### Return type

[**Teams**](Teams.md)

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

# **update_team_endpoint_v1_teams_team_id_patch**
> Teams update_team_endpoint_v1_teams_team_id_patch(team_id, name=name)

Update Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 
    name = 'name_example' # str |  (optional)

    try:
        # Update Team Endpoint
        api_response = api_instance.update_team_endpoint_v1_teams_team_id_patch(team_id, name=name)
        print("The response of TeamsApi->update_team_endpoint_v1_teams_team_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->update_team_endpoint_v1_teams_team_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **name** | **str**|  | [optional] 

### Return type

[**Teams**](Teams.md)

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

