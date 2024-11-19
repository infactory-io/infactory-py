# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_endpoint_v1_users_post**](UsersApi.md#create_user_endpoint_v1_users_post) | **POST** /v1/users/ | Create User Endpoint
[**delete_user_endpoint_v1_users_user_id_delete**](UsersApi.md#delete_user_endpoint_v1_users_user_id_delete) | **DELETE** /v1/users/{user_id} | Delete User Endpoint
[**get_user_endpoint_v1_users_user_id_get**](UsersApi.md#get_user_endpoint_v1_users_user_id_get) | **GET** /v1/users/{user_id} | Get User Endpoint
[**get_users_endpoint_v1_users_get**](UsersApi.md#get_users_endpoint_v1_users_get) | **GET** /v1/users/ | Get Users Endpoint
[**move_user_endpoint_v1_users_user_id_move_post**](UsersApi.md#move_user_endpoint_v1_users_user_id_move_post) | **POST** /v1/users/{user_id}/move | Move User Endpoint
[**update_user_endpoint_v1_users_user_id_patch**](UsersApi.md#update_user_endpoint_v1_users_user_id_patch) | **PATCH** /v1/users/{user_id} | Update User Endpoint


# **create_user_endpoint_v1_users_post**
> Users create_user_endpoint_v1_users_post(email=email, name=name, organization_id=organization_id, role=role)

Create User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    email = 'email_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    organization_id = 'organization_id_example' # str |  (optional)
    role = 'role_example' # str |  (optional)

    try:
        # Create User Endpoint
        api_response = api_instance.create_user_endpoint_v1_users_post(email=email, name=name, organization_id=organization_id, role=role)
        print("The response of UsersApi->create_user_endpoint_v1_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_endpoint_v1_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **organization_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 

### Return type

[**Users**](Users.md)

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

# **delete_user_endpoint_v1_users_user_id_delete**
> Users delete_user_endpoint_v1_users_user_id_delete(user_id)

Delete User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Delete User Endpoint
        api_response = api_instance.delete_user_endpoint_v1_users_user_id_delete(user_id)
        print("The response of UsersApi->delete_user_endpoint_v1_users_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_endpoint_v1_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Users**](Users.md)

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

# **get_user_endpoint_v1_users_user_id_get**
> Users get_user_endpoint_v1_users_user_id_get(user_id)

Get User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Endpoint
        api_response = api_instance.get_user_endpoint_v1_users_user_id_get(user_id)
        print("The response of UsersApi->get_user_endpoint_v1_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_endpoint_v1_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Users**](Users.md)

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

# **get_users_endpoint_v1_users_get**
> List[Users] get_users_endpoint_v1_users_get(organization_id=organization_id)

Get Users Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)

    try:
        # Get Users Endpoint
        api_response = api_instance.get_users_endpoint_v1_users_get(organization_id=organization_id)
        print("The response of UsersApi->get_users_endpoint_v1_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_endpoint_v1_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 

### Return type

[**List[Users]**](Users.md)

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

# **move_user_endpoint_v1_users_user_id_move_post**
> Users move_user_endpoint_v1_users_user_id_move_post(user_id, new_organization_id)

Move User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    new_organization_id = 'new_organization_id_example' # str | 

    try:
        # Move User Endpoint
        api_response = api_instance.move_user_endpoint_v1_users_user_id_move_post(user_id, new_organization_id)
        print("The response of UsersApi->move_user_endpoint_v1_users_user_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->move_user_endpoint_v1_users_user_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **new_organization_id** | **str**|  | 

### Return type

[**Users**](Users.md)

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

# **update_user_endpoint_v1_users_user_id_patch**
> Users update_user_endpoint_v1_users_user_id_patch(user_id, email=email, name=name, role=role)

Update User Endpoint

### Example


```python
import openapi_client
from openapi_client.models.users import Users
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
    api_instance = openapi_client.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    email = 'email_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    role = 'role_example' # str |  (optional)

    try:
        # Update User Endpoint
        api_response = api_instance.update_user_endpoint_v1_users_user_id_patch(user_id, email=email, name=name, role=role)
        print("The response of UsersApi->update_user_endpoint_v1_users_user_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_endpoint_v1_users_user_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **email** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 

### Return type

[**Users**](Users.md)

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

