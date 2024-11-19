# openapi_client.ToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_dataline_request_v1_tools_ask_dataline_post**](ToolsApi.md#ask_dataline_request_v1_tools_ask_dataline_post) | **POST** /v1/tools/ask-dataline | Ask Dataline Request
[**create_workspace_request_v1_tools_create_workspace_post**](ToolsApi.md#create_workspace_request_v1_tools_create_workspace_post) | **POST** /v1/tools/create-workspace | Create Workspace Request
[**generate_dataline_request_v1_tools_generate_dataline_post**](ToolsApi.md#generate_dataline_request_v1_tools_generate_dataline_post) | **POST** /v1/tools/generate-dataline | Generate Dataline Request
[**generate_queries_request_v1_tools_generate_queries_post**](ToolsApi.md#generate_queries_request_v1_tools_generate_queries_post) | **POST** /v1/tools/generate-queries | Generate Queries Request
[**get_list_of_tools_v1_tools_get**](ToolsApi.md#get_list_of_tools_v1_tools_get) | **GET** /v1/tools/ | List Available Tools
[**get_tool_help_v1_tools_tool_name_get**](ToolsApi.md#get_tool_help_v1_tools_tool_name_get) | **GET** /v1/tools/{tool_name} | Get Tool Information
[**run_tool_v1_tools_tool_name_post**](ToolsApi.md#run_tool_v1_tools_tool_name_post) | **POST** /v1/tools/{tool_name} | Run Tool
[**transform_data_request_v1_tools_transform_data_post**](ToolsApi.md#transform_data_request_v1_tools_transform_data_post) | **POST** /v1/tools/transform-data | Transform Data Request


# **ask_dataline_request_v1_tools_ask_dataline_post**
> ask_dataline_request_v1_tools_ask_dataline_post(ask_dataline_request)

Ask Dataline Request

### Example


```python
import openapi_client
from openapi_client.models.ask_dataline_request import AskDatalineRequest
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
    api_instance = openapi_client.ToolsApi(api_client)
    ask_dataline_request = openapi_client.AskDatalineRequest() # AskDatalineRequest | 

    try:
        # Ask Dataline Request
        api_instance.ask_dataline_request_v1_tools_ask_dataline_post(ask_dataline_request)
    except Exception as e:
        print("Exception when calling ToolsApi->ask_dataline_request_v1_tools_ask_dataline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ask_dataline_request** | [**AskDatalineRequest**](AskDatalineRequest.md)|  | 

### Return type

void (empty response body)

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

# **create_workspace_request_v1_tools_create_workspace_post**
> WorkspaceToolRequest create_workspace_request_v1_tools_create_workspace_post(workspace_tool_request=workspace_tool_request)

Create Workspace Request

### Example


```python
import openapi_client
from openapi_client.models.workspace_tool_request import WorkspaceToolRequest
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
    api_instance = openapi_client.ToolsApi(api_client)
    workspace_tool_request = openapi_client.WorkspaceToolRequest() # WorkspaceToolRequest |  (optional)

    try:
        # Create Workspace Request
        api_response = api_instance.create_workspace_request_v1_tools_create_workspace_post(workspace_tool_request=workspace_tool_request)
        print("The response of ToolsApi->create_workspace_request_v1_tools_create_workspace_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_workspace_request_v1_tools_create_workspace_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_tool_request** | [**WorkspaceToolRequest**](WorkspaceToolRequest.md)|  | [optional] 

### Return type

[**WorkspaceToolRequest**](WorkspaceToolRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful execution of the tool |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_dataline_request_v1_tools_generate_dataline_post**
> generate_dataline_request_v1_tools_generate_dataline_post(dataline_request)

Generate Dataline Request

### Example


```python
import openapi_client
from openapi_client.models.dataline_request import DatalineRequest
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
    api_instance = openapi_client.ToolsApi(api_client)
    dataline_request = openapi_client.DatalineRequest() # DatalineRequest | 

    try:
        # Generate Dataline Request
        api_instance.generate_dataline_request_v1_tools_generate_dataline_post(dataline_request)
    except Exception as e:
        print("Exception when calling ToolsApi->generate_dataline_request_v1_tools_generate_dataline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_request** | [**DatalineRequest**](DatalineRequest.md)|  | 

### Return type

void (empty response body)

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

# **generate_queries_request_v1_tools_generate_queries_post**
> generate_queries_request_v1_tools_generate_queries_post(dataline_request)

Generate Queries Request

### Example


```python
import openapi_client
from openapi_client.models.dataline_request import DatalineRequest
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
    api_instance = openapi_client.ToolsApi(api_client)
    dataline_request = openapi_client.DatalineRequest() # DatalineRequest | 

    try:
        # Generate Queries Request
        api_instance.generate_queries_request_v1_tools_generate_queries_post(dataline_request)
    except Exception as e:
        print("Exception when calling ToolsApi->generate_queries_request_v1_tools_generate_queries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_request** | [**DatalineRequest**](DatalineRequest.md)|  | 

### Return type

void (empty response body)

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

# **get_list_of_tools_v1_tools_get**
> List[Tool] get_list_of_tools_v1_tools_get()

List Available Tools

Retrieve a list of all available tools in the system.  This endpoint executes the 'list-tools' command in i7ysh and returns information about all available tools. Each tool entry includes its name, description, version, and category.  Returns:     List[Tool]: A list of Tool objects containing information about each available tool.  Raises:     HTTPException:         - 500: If there's an error executing the list-tools command         - 500: If there's an error parsing the tool information

### Example


```python
import openapi_client
from openapi_client.models.tool import Tool
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
    api_instance = openapi_client.ToolsApi(api_client)

    try:
        # List Available Tools
        api_response = api_instance.get_list_of_tools_v1_tools_get()
        print("The response of ToolsApi->get_list_of_tools_v1_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_list_of_tools_v1_tools_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Tool]**](Tool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of tools |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tool_help_v1_tools_tool_name_get**
> Tool get_tool_help_v1_tools_tool_name_get(tool_name)

Get Tool Information

### Example


```python
import openapi_client
from openapi_client.models.tool import Tool
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
    api_instance = openapi_client.ToolsApi(api_client)
    tool_name = 'tool_name_example' # str | 

    try:
        # Get Tool Information
        api_response = api_instance.get_tool_help_v1_tools_tool_name_get(tool_name)
        print("The response of ToolsApi->get_tool_help_v1_tools_tool_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tool_help_v1_tools_tool_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_name** | **str**|  | 

### Return type

[**Tool**](Tool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tool help and versions |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_tool_v1_tools_tool_name_post**
> object run_tool_v1_tools_tool_name_post(tool_name, body)

Run Tool

Execute a specific tool with the given arguments.  This endpoint runs the specified tool using the provided arguments.  Args:     tool_name (str): The name of the tool to execute.     args (dict): A dictionary of arguments to pass to the tool.  Returns:     ResponseModel: The result of the tool execution.  Raises:     HTTPException:         - 400: help or version arguments used improperly         - 404: If the specified tool is not found         - 500: If there's an error during tool execution

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
    api_instance = openapi_client.ToolsApi(api_client)
    tool_name = 'tool_name_example' # str | 
    body = None # object | 

    try:
        # Run Tool
        api_response = api_instance.run_tool_v1_tools_tool_name_post(tool_name, body)
        print("The response of ToolsApi->run_tool_v1_tools_tool_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->run_tool_v1_tools_tool_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_name** | **str**|  | 
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful execution of the tool |  -  |
**400** | Improper usage of help or version arguments |  -  |
**404** | Tool not found |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_data_request_v1_tools_transform_data_post**
> transform_data_request_v1_tools_transform_data_post(dataline_request)

Transform Data Request

### Example


```python
import openapi_client
from openapi_client.models.dataline_request import DatalineRequest
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
    api_instance = openapi_client.ToolsApi(api_client)
    dataline_request = openapi_client.DatalineRequest() # DatalineRequest | 

    try:
        # Transform Data Request
        api_instance.transform_data_request_v1_tools_transform_data_post(dataline_request)
    except Exception as e:
        print("Exception when calling ToolsApi->transform_data_request_v1_tools_transform_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_request** | [**DatalineRequest**](DatalineRequest.md)|  | 

### Return type

void (empty response body)

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

