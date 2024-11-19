# openapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_v1_authentication_token_post**](AuthApi.md#login_v1_authentication_token_post) | **POST** /v1/authentication/token | Login
[**read_users_me_v1_authentication_me_get**](AuthApi.md#read_users_me_v1_authentication_me_get) | **GET** /v1/authentication/me | Read Users Me
[**signup_v1_authentication_signup_post**](AuthApi.md#signup_v1_authentication_signup_post) | **POST** /v1/authentication/signup | Signup


# **login_v1_authentication_token_post**
> object login_v1_authentication_token_post(username)

Login

### Example

* Bearer Authentication (APP API Key Bearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APP API Key Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)
    username = 'username_example' # str | 

    try:
        # Login
        api_response = api_instance.login_v1_authentication_token_post(username)
        print("The response of AuthApi->login_v1_authentication_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_v1_authentication_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

**object**

### Authorization

[APP API Key Bearer](../README.md#APP API Key Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_users_me_v1_authentication_me_get**
> Users read_users_me_v1_authentication_me_get()

Read Users Me

### Example

* Bearer Authentication (User JWT Bearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: User JWT Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)

    try:
        # Read Users Me
        api_response = api_instance.read_users_me_v1_authentication_me_get()
        print("The response of AuthApi->read_users_me_v1_authentication_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->read_users_me_v1_authentication_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

### Authorization

[User JWT Bearer](../README.md#User JWT Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_v1_authentication_signup_post**
> object signup_v1_authentication_signup_post(user_create_input)

Signup

### Example

* Bearer Authentication (APP API Key Bearer):

```python
import openapi_client
from openapi_client.models.user_create_input import UserCreateInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APP API Key Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthApi(api_client)
    user_create_input = openapi_client.UserCreateInput() # UserCreateInput | 

    try:
        # Signup
        api_response = api_instance.signup_v1_authentication_signup_post(user_create_input)
        print("The response of AuthApi->signup_v1_authentication_signup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->signup_v1_authentication_signup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_input** | [**UserCreateInput**](UserCreateInput.md)|  | 

### Return type

**object**

### Authorization

[APP API Key Bearer](../README.md#APP API Key Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

