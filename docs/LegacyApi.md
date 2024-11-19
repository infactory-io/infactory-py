# openapi_client.LegacyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataline_get_dataline_file_name_get**](LegacyApi.md#dataline_get_dataline_file_name_get) | **GET** /dataline/{file_name} | Dataline Get
[**dataline_post_dataline_post**](LegacyApi.md#dataline_post_dataline_post) | **POST** /dataline | Dataline Post
[**manifest_manifest_post**](LegacyApi.md#manifest_manifest_post) | **POST** /manifest | Manifest
[**run_command_with_i7y_exec_post**](LegacyApi.md#run_command_with_i7y_exec_post) | **POST** / | Run Command With I7Y Exec


# **dataline_get_dataline_file_name_get**
> object dataline_get_dataline_file_name_get(file_name)

Dataline Get

### Example


```python
import openapi_client
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
    api_instance = openapi_client.LegacyApi(api_client)
    file_name = 'file_name_example' # str | 

    try:
        # Dataline Get
        api_response = api_instance.dataline_get_dataline_file_name_get(file_name)
        print("The response of LegacyApi->dataline_get_dataline_file_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyApi->dataline_get_dataline_file_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 

### Return type

**object**

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

# **dataline_post_dataline_post**
> object dataline_post_dataline_post()

Dataline Post

Payload has fields: 'type' in {'suggest_queries', 'run_query', 'code'} if 'type' is code, then look for 'code' in the payload

### Example


```python
import openapi_client
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
    api_instance = openapi_client.LegacyApi(api_client)

    try:
        # Dataline Post
        api_response = api_instance.dataline_post_dataline_post()
        print("The response of LegacyApi->dataline_post_dataline_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyApi->dataline_post_dataline_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **manifest_manifest_post**
> object manifest_manifest_post()

Manifest

### Example


```python
import openapi_client
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
    api_instance = openapi_client.LegacyApi(api_client)

    try:
        # Manifest
        api_response = api_instance.manifest_manifest_post()
        print("The response of LegacyApi->manifest_manifest_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyApi->manifest_manifest_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **run_command_with_i7y_exec_post**
> object run_command_with_i7y_exec_post()

Run Command With I7Y Exec

Run a command with i7y_exec

### Example


```python
import openapi_client
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
    api_instance = openapi_client.LegacyApi(api_client)

    try:
        # Run Command With I7Y Exec
        api_response = api_instance.run_command_with_i7y_exec_post()
        print("The response of LegacyApi->run_command_with_i7y_exec_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyApi->run_command_with_i7y_exec_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

