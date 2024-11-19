# openapi_client.ActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post**](ActionsApi.md#analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post) | **POST** /v1/actions/load/analyze/{project_id}/{dataobject_id} | Analyze Data Endpoint
[**ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post**](ActionsApi.md#ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/{transform_file_id}/{dataline_id} | Ask Endpoint
[**compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post**](ActionsApi.md#compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/compile/{transform_file_id}/{dataline_id} | Compile Query Endpoint
[**convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post**](ActionsApi.md#convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post) | **POST** /v1/actions/load/convert/{project_id}/{dataobject_id} | Convert Data Endpoint
[**evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post**](ActionsApi.md#evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/evaluate/{query_program_id}/{transform_file_id}/{dataline_id} | Evaluate Query Endpoint
[**format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post**](ActionsApi.md#format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post) | **POST** /v1/actions/ask/format/{query_program_id}/{query_response_id}/{dataline_id} | Format Response Endpoint
[**generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post**](ActionsApi.md#generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post) | **POST** /v1/actions/generate/queries/{transform_file_id}/{dataline_id} | Generate Queries Endpoint
[**load_data_endpoint_v1_actions_load_project_id_post**](ActionsApi.md#load_data_endpoint_v1_actions_load_project_id_post) | **POST** /v1/actions/load/{project_id} | Load Data Endpoint
[**prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post**](ActionsApi.md#prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post) | **POST** /v1/actions/load/prepare/{project_id}/{parquet_file_id}/{dataline_file_id} | Prepare Data Endpoint
[**update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post**](ActionsApi.md#update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/compile/update/{query_program_id}/{transform_file_id}/{dataline_id} | Update Compile Query Endpoint
[**upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post**](ActionsApi.md#upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post) | **POST** /v1/actions/load/upload/{project_id}/{datasource_id} | Upload Data Endpoint


# **analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post**
> object analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post(project_id, dataobject_id)

Analyze Data Endpoint

Analyze parquet data and create dataline

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
    api_instance = openapi_client.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataobject_id = 'dataobject_id_example' # str | 

    try:
        # Analyze Data Endpoint
        api_response = api_instance.analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post(project_id, dataobject_id)
        print("The response of ActionsApi->analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataobject_id** | **str**|  | 

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

# **ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post**
> object ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post(transform_file_id, dataline_id, query)

Ask Endpoint

Combined endpoint for compile, evaluate and format

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
    api_instance = openapi_client.ActionsApi(api_client)
    transform_file_id = 'transform_file_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 
    query = 'query_example' # str | 

    try:
        # Ask Endpoint
        api_response = api_instance.ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post(transform_file_id, dataline_id, query)
        print("The response of ActionsApi->ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform_file_id** | **str**|  | 
 **dataline_id** | **str**|  | 
 **query** | **str**|  | 

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

# **compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post**
> object compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post(transform_file_id, dataline_id, query)

Compile Query Endpoint

Compile a query into a query program

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
    api_instance = openapi_client.ActionsApi(api_client)
    transform_file_id = 'transform_file_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 
    query = 'query_example' # str | 

    try:
        # Compile Query Endpoint
        api_response = api_instance.compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post(transform_file_id, dataline_id, query)
        print("The response of ActionsApi->compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform_file_id** | **str**|  | 
 **dataline_id** | **str**|  | 
 **query** | **str**|  | 

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

# **convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post**
> object convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post(project_id, dataobject_id)

Convert Data Endpoint

Convert data to parquet format

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
    api_instance = openapi_client.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    dataobject_id = 'dataobject_id_example' # str | 

    try:
        # Convert Data Endpoint
        api_response = api_instance.convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post(project_id, dataobject_id)
        print("The response of ActionsApi->convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **dataobject_id** | **str**|  | 

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

# **evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post**
> object evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post(query_program_id, transform_file_id, dataline_id)

Evaluate Query Endpoint

Evaluate a query program

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
    api_instance = openapi_client.ActionsApi(api_client)
    query_program_id = 'query_program_id_example' # str | 
    transform_file_id = 'transform_file_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 

    try:
        # Evaluate Query Endpoint
        api_response = api_instance.evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post(query_program_id, transform_file_id, dataline_id)
        print("The response of ActionsApi->evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_program_id** | **str**|  | 
 **transform_file_id** | **str**|  | 
 **dataline_id** | **str**|  | 

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

# **format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post**
> object format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post(query_program_id, query_response_id, dataline_id, query)

Format Response Endpoint

Format a query response

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
    api_instance = openapi_client.ActionsApi(api_client)
    query_program_id = 'query_program_id_example' # str | 
    query_response_id = 'query_response_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 
    query = 'query_example' # str | 

    try:
        # Format Response Endpoint
        api_response = api_instance.format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post(query_program_id, query_response_id, dataline_id, query)
        print("The response of ActionsApi->format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_program_id** | **str**|  | 
 **query_response_id** | **str**|  | 
 **dataline_id** | **str**|  | 
 **query** | **str**|  | 

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

# **generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post**
> object generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post(transform_file_id, dataline_id, workspace_name)

Generate Queries Endpoint

Generate queries for a dataset and dataline model

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
    api_instance = openapi_client.ActionsApi(api_client)
    transform_file_id = 'transform_file_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 
    workspace_name = 'workspace_name_example' # str | 

    try:
        # Generate Queries Endpoint
        api_response = api_instance.generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post(transform_file_id, dataline_id, workspace_name)
        print("The response of ActionsApi->generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform_file_id** | **str**|  | 
 **dataline_id** | **str**|  | 
 **workspace_name** | **str**|  | 

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

# **load_data_endpoint_v1_actions_load_project_id_post**
> object load_data_endpoint_v1_actions_load_project_id_post(project_id, datasource_id=datasource_id, file=file, source_url=source_url, file_type=file_type, source_credentials=source_credentials)

Load Data Endpoint

Combined endpoint for upload, analysis, and preparation

### Example


```python
import openapi_client
from openapi_client.models.source_credentials import SourceCredentials
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
    api_instance = openapi_client.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    datasource_id = 'datasource_id_example' # str |  (optional)
    file = None # bytearray |  (optional)
    source_url = 'source_url_example' # str |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    source_credentials = openapi_client.SourceCredentials() # SourceCredentials |  (optional)

    try:
        # Load Data Endpoint
        api_response = api_instance.load_data_endpoint_v1_actions_load_project_id_post(project_id, datasource_id=datasource_id, file=file, source_url=source_url, file_type=file_type, source_credentials=source_credentials)
        print("The response of ActionsApi->load_data_endpoint_v1_actions_load_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->load_data_endpoint_v1_actions_load_project_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **datasource_id** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 
 **source_url** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] 
 **source_credentials** | [**SourceCredentials**](SourceCredentials.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post**
> object prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post(project_id, parquet_file_id, dataline_file_id)

Prepare Data Endpoint

Prepare and transform data using a dataline file.  Args:     project_id: The ID of the project     parquet_file_id: ID of the parquet file to transform     dataline_file_id: ID of the dataline file containing transformation rules     app_storage_client: Database client dependency     user_storage: User storage service dependency  Returns:     EventSourceResponse: Streaming response of the preparation process  Raises:     HTTPException:         - 404: If either parquet or dataline file is not found         - 400: For validation errors         - 500: For internal server errors

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
    api_instance = openapi_client.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    parquet_file_id = 'parquet_file_id_example' # str | 
    dataline_file_id = 'dataline_file_id_example' # str | 

    try:
        # Prepare Data Endpoint
        api_response = api_instance.prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post(project_id, parquet_file_id, dataline_file_id)
        print("The response of ActionsApi->prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **parquet_file_id** | **str**|  | 
 **dataline_file_id** | **str**|  | 

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

# **update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post**
> object update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post(query_program_id, transform_file_id, dataline_id, query)

Update Compile Query Endpoint

Update an existing query program with a new compilation

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
    api_instance = openapi_client.ActionsApi(api_client)
    query_program_id = 'query_program_id_example' # str | 
    transform_file_id = 'transform_file_id_example' # str | 
    dataline_id = 'dataline_id_example' # str | 
    query = 'query_example' # str | 

    try:
        # Update Compile Query Endpoint
        api_response = api_instance.update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post(query_program_id, transform_file_id, dataline_id, query)
        print("The response of ActionsApi->update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_program_id** | **str**|  | 
 **transform_file_id** | **str**|  | 
 **dataline_id** | **str**|  | 
 **query** | **str**|  | 

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

# **upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post**
> object upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post(project_id, datasource_id, file=file, source_url=source_url, file_type=file_type, source_credentials=source_credentials)

Upload Data Endpoint

Upload endpoint with automatic datasource creation if needed

### Example


```python
import openapi_client
from openapi_client.models.source_credentials import SourceCredentials
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
    api_instance = openapi_client.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    datasource_id = 'datasource_id_example' # str | 
    file = None # bytearray |  (optional)
    source_url = 'source_url_example' # str |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    source_credentials = openapi_client.SourceCredentials() # SourceCredentials |  (optional)

    try:
        # Upload Data Endpoint
        api_response = api_instance.upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post(project_id, datasource_id, file=file, source_url=source_url, file_type=file_type, source_credentials=source_credentials)
        print("The response of ActionsApi->upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **datasource_id** | **str**|  | 
 **file** | **bytearray**|  | [optional] 
 **source_url** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] 
 **source_credentials** | [**SourceCredentials**](SourceCredentials.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

