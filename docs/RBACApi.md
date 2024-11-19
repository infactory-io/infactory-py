# openapi_client.RBACApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rbac_endpoint_v1_rbac_post**](RBACApi.md#create_rbac_endpoint_v1_rbac_post) | **POST** /v1/rbac/ | Create Rbac Endpoint
[**delete_rbac_endpoint_v1_rbac_rbac_id_delete**](RBACApi.md#delete_rbac_endpoint_v1_rbac_rbac_id_delete) | **DELETE** /v1/rbac/{rbac_id} | Delete Rbac Endpoint
[**get_rbac_by_team_endpoint_v1_rbac_team_team_id_get**](RBACApi.md#get_rbac_by_team_endpoint_v1_rbac_team_team_id_get) | **GET** /v1/rbac/team/{team_id} | Get Rbac By Team Endpoint
[**get_rbac_by_user_endpoint_v1_rbac_user_user_id_get**](RBACApi.md#get_rbac_by_user_endpoint_v1_rbac_user_user_id_get) | **GET** /v1/rbac/user/{user_id} | Get Rbac By User Endpoint
[**get_rbac_endpoint_v1_rbac_rbac_id_get**](RBACApi.md#get_rbac_endpoint_v1_rbac_rbac_id_get) | **GET** /v1/rbac/{rbac_id} | Get Rbac Endpoint
[**update_rbac_endpoint_v1_rbac_rbac_id_patch**](RBACApi.md#update_rbac_endpoint_v1_rbac_rbac_id_patch) | **PATCH** /v1/rbac/{rbac_id} | Update Rbac Endpoint


# **create_rbac_endpoint_v1_rbac_post**
> Rbac create_rbac_endpoint_v1_rbac_post(role_name=role_name, user_id=user_id, team_id=team_id, body=body)

Create Rbac Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    role_name = 'role_name_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    team_id = 'team_id_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Create Rbac Endpoint
        api_response = api_instance.create_rbac_endpoint_v1_rbac_post(role_name=role_name, user_id=user_id, team_id=team_id, body=body)
        print("The response of RBACApi->create_rbac_endpoint_v1_rbac_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->create_rbac_endpoint_v1_rbac_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **team_id** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**Rbac**](Rbac.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rbac_endpoint_v1_rbac_rbac_id_delete**
> Rbac delete_rbac_endpoint_v1_rbac_rbac_id_delete(rbac_id)

Delete Rbac Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    rbac_id = 'rbac_id_example' # str | 

    try:
        # Delete Rbac Endpoint
        api_response = api_instance.delete_rbac_endpoint_v1_rbac_rbac_id_delete(rbac_id)
        print("The response of RBACApi->delete_rbac_endpoint_v1_rbac_rbac_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->delete_rbac_endpoint_v1_rbac_rbac_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_id** | **str**|  | 

### Return type

[**Rbac**](Rbac.md)

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

# **get_rbac_by_team_endpoint_v1_rbac_team_team_id_get**
> List[Rbac] get_rbac_by_team_endpoint_v1_rbac_team_team_id_get(team_id)

Get Rbac By Team Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Get Rbac By Team Endpoint
        api_response = api_instance.get_rbac_by_team_endpoint_v1_rbac_team_team_id_get(team_id)
        print("The response of RBACApi->get_rbac_by_team_endpoint_v1_rbac_team_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->get_rbac_by_team_endpoint_v1_rbac_team_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**List[Rbac]**](Rbac.md)

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

# **get_rbac_by_user_endpoint_v1_rbac_user_user_id_get**
> List[Rbac] get_rbac_by_user_endpoint_v1_rbac_user_user_id_get(user_id)

Get Rbac By User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get Rbac By User Endpoint
        api_response = api_instance.get_rbac_by_user_endpoint_v1_rbac_user_user_id_get(user_id)
        print("The response of RBACApi->get_rbac_by_user_endpoint_v1_rbac_user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->get_rbac_by_user_endpoint_v1_rbac_user_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[Rbac]**](Rbac.md)

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

# **get_rbac_endpoint_v1_rbac_rbac_id_get**
> Rbac get_rbac_endpoint_v1_rbac_rbac_id_get(rbac_id)

Get Rbac Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    rbac_id = 'rbac_id_example' # str | 

    try:
        # Get Rbac Endpoint
        api_response = api_instance.get_rbac_endpoint_v1_rbac_rbac_id_get(rbac_id)
        print("The response of RBACApi->get_rbac_endpoint_v1_rbac_rbac_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->get_rbac_endpoint_v1_rbac_rbac_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_id** | **str**|  | 

### Return type

[**Rbac**](Rbac.md)

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

# **update_rbac_endpoint_v1_rbac_rbac_id_patch**
> Rbac update_rbac_endpoint_v1_rbac_rbac_id_patch(rbac_id, role_name=role_name, body=body)

Update Rbac Endpoint

### Example


```python
import openapi_client
from openapi_client.models.rbac import Rbac
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
    api_instance = openapi_client.RBACApi(api_client)
    rbac_id = 'rbac_id_example' # str | 
    role_name = 'role_name_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update Rbac Endpoint
        api_response = api_instance.update_rbac_endpoint_v1_rbac_rbac_id_patch(rbac_id, role_name=role_name, body=body)
        print("The response of RBACApi->update_rbac_endpoint_v1_rbac_rbac_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RBACApi->update_rbac_endpoint_v1_rbac_rbac_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_id** | **str**|  | 
 **role_name** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**Rbac**](Rbac.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

