# openapi_client.PlatformApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_endpoint_v1_platforms_post**](PlatformApi.md#create_platform_endpoint_v1_platforms_post) | **POST** /v1/platforms/ | Create Platform Endpoint
[**delete_platform_endpoint_v1_platforms_platform_id_delete**](PlatformApi.md#delete_platform_endpoint_v1_platforms_platform_id_delete) | **DELETE** /v1/platforms/{platform_id} | Delete Platform Endpoint
[**get_platform_endpoint_v1_platforms_platform_id_get**](PlatformApi.md#get_platform_endpoint_v1_platforms_platform_id_get) | **GET** /v1/platforms/{platform_id} | Get Platform Endpoint
[**get_platforms_endpoint_v1_platforms_get**](PlatformApi.md#get_platforms_endpoint_v1_platforms_get) | **GET** /v1/platforms/ | Get Platforms Endpoint
[**update_platform_endpoint_v1_platforms_platform_id_patch**](PlatformApi.md#update_platform_endpoint_v1_platforms_platform_id_patch) | **PATCH** /v1/platforms/{platform_id} | Update Platform Endpoint


# **create_platform_endpoint_v1_platforms_post**
> Platform create_platform_endpoint_v1_platforms_post(platform_create)

Create Platform Endpoint

### Example


```python
import openapi_client
from openapi_client.models.platform import Platform
from openapi_client.models.platform_create import PlatformCreate
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
    api_instance = openapi_client.PlatformApi(api_client)
    platform_create = openapi_client.PlatformCreate() # PlatformCreate | 

    try:
        # Create Platform Endpoint
        api_response = api_instance.create_platform_endpoint_v1_platforms_post(platform_create)
        print("The response of PlatformApi->create_platform_endpoint_v1_platforms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->create_platform_endpoint_v1_platforms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_create** | [**PlatformCreate**](PlatformCreate.md)|  | 

### Return type

[**Platform**](Platform.md)

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

# **delete_platform_endpoint_v1_platforms_platform_id_delete**
> Platform delete_platform_endpoint_v1_platforms_platform_id_delete(platform_id)

Delete Platform Endpoint

### Example


```python
import openapi_client
from openapi_client.models.platform import Platform
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
    api_instance = openapi_client.PlatformApi(api_client)
    platform_id = 'platform_id_example' # str | 

    try:
        # Delete Platform Endpoint
        api_response = api_instance.delete_platform_endpoint_v1_platforms_platform_id_delete(platform_id)
        print("The response of PlatformApi->delete_platform_endpoint_v1_platforms_platform_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->delete_platform_endpoint_v1_platforms_platform_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**|  | 

### Return type

[**Platform**](Platform.md)

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

# **get_platform_endpoint_v1_platforms_platform_id_get**
> Platform get_platform_endpoint_v1_platforms_platform_id_get(platform_id)

Get Platform Endpoint

### Example


```python
import openapi_client
from openapi_client.models.platform import Platform
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
    api_instance = openapi_client.PlatformApi(api_client)
    platform_id = 'platform_id_example' # str | 

    try:
        # Get Platform Endpoint
        api_response = api_instance.get_platform_endpoint_v1_platforms_platform_id_get(platform_id)
        print("The response of PlatformApi->get_platform_endpoint_v1_platforms_platform_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_platform_endpoint_v1_platforms_platform_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**|  | 

### Return type

[**Platform**](Platform.md)

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

# **get_platforms_endpoint_v1_platforms_get**
> List[Platform] get_platforms_endpoint_v1_platforms_get()

Get Platforms Endpoint

### Example


```python
import openapi_client
from openapi_client.models.platform import Platform
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
    api_instance = openapi_client.PlatformApi(api_client)

    try:
        # Get Platforms Endpoint
        api_response = api_instance.get_platforms_endpoint_v1_platforms_get()
        print("The response of PlatformApi->get_platforms_endpoint_v1_platforms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->get_platforms_endpoint_v1_platforms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Platform]**](Platform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_endpoint_v1_platforms_platform_id_patch**
> Platform update_platform_endpoint_v1_platforms_platform_id_patch(platform_id, name=name, description=description, body=body)

Update Platform Endpoint

### Example


```python
import openapi_client
from openapi_client.models.platform import Platform
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
    api_instance = openapi_client.PlatformApi(api_client)
    platform_id = 'platform_id_example' # str | 
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update Platform Endpoint
        api_response = api_instance.update_platform_endpoint_v1_platforms_platform_id_patch(platform_id, name=name, description=description, body=body)
        print("The response of PlatformApi->update_platform_endpoint_v1_platforms_platform_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformApi->update_platform_endpoint_v1_platforms_platform_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**Platform**](Platform.md)

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

