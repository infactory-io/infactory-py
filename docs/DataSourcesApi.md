# openapi_client.DataSourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_datasource_endpoint_v1_datasources_project_id_post**](DataSourcesApi.md#create_datasource_endpoint_v1_datasources_project_id_post) | **POST** /v1/datasources/{project_id} | Create Datasource Endpoint
[**delete_datasource_endpoint_v1_datasources_datasource_id_delete**](DataSourcesApi.md#delete_datasource_endpoint_v1_datasources_datasource_id_delete) | **DELETE** /v1/datasources/{datasource_id} | Delete Datasource Endpoint
[**get_datasource_endpoint_v1_datasources_datasource_id_get**](DataSourcesApi.md#get_datasource_endpoint_v1_datasources_datasource_id_get) | **GET** /v1/datasources/{datasource_id} | Get Datasource Endpoint
[**get_datasources_endpoint_v1_datasources_project_project_id_get**](DataSourcesApi.md#get_datasources_endpoint_v1_datasources_project_project_id_get) | **GET** /v1/datasources/project/{project_id} | Get Datasources Endpoint
[**update_datasource_endpoint_v1_datasources_datasource_id_patch**](DataSourcesApi.md#update_datasource_endpoint_v1_datasources_datasource_id_patch) | **PATCH** /v1/datasources/{datasource_id} | Update Datasource Endpoint
[**upload_source_v1_datasources_datasource_id_upload_post**](DataSourcesApi.md#upload_source_v1_datasources_datasource_id_upload_post) | **POST** /v1/datasources/{datasource_id}/upload | Upload a data source file


# **create_datasource_endpoint_v1_datasources_project_id_post**
> Datasources create_datasource_endpoint_v1_datasources_project_id_post(project_id, name=name, type=type, uri=uri)

Create Datasource Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datasources import Datasources
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
    api_instance = openapi_client.DataSourcesApi(api_client)
    project_id = 'project_id_example' # str | 
    name = 'name_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    uri = 'uri_example' # str |  (optional)

    try:
        # Create Datasource Endpoint
        api_response = api_instance.create_datasource_endpoint_v1_datasources_project_id_post(project_id, name=name, type=type, uri=uri)
        print("The response of DataSourcesApi->create_datasource_endpoint_v1_datasources_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->create_datasource_endpoint_v1_datasources_project_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **uri** | **str**|  | [optional] 

### Return type

[**Datasources**](Datasources.md)

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

# **delete_datasource_endpoint_v1_datasources_datasource_id_delete**
> Datasources delete_datasource_endpoint_v1_datasources_datasource_id_delete(datasource_id, permanent=permanent)

Delete Datasource Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datasources import Datasources
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
    api_instance = openapi_client.DataSourcesApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    permanent = False # bool |  (optional) (default to False)

    try:
        # Delete Datasource Endpoint
        api_response = api_instance.delete_datasource_endpoint_v1_datasources_datasource_id_delete(datasource_id, permanent=permanent)
        print("The response of DataSourcesApi->delete_datasource_endpoint_v1_datasources_datasource_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->delete_datasource_endpoint_v1_datasources_datasource_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **permanent** | **bool**|  | [optional] [default to False]

### Return type

[**Datasources**](Datasources.md)

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

# **get_datasource_endpoint_v1_datasources_datasource_id_get**
> Datasources get_datasource_endpoint_v1_datasources_datasource_id_get(datasource_id)

Get Datasource Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datasources import Datasources
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
    api_instance = openapi_client.DataSourcesApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Get Datasource Endpoint
        api_response = api_instance.get_datasource_endpoint_v1_datasources_datasource_id_get(datasource_id)
        print("The response of DataSourcesApi->get_datasource_endpoint_v1_datasources_datasource_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->get_datasource_endpoint_v1_datasources_datasource_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

### Return type

[**Datasources**](Datasources.md)

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

# **get_datasources_endpoint_v1_datasources_project_project_id_get**
> List[Datasources] get_datasources_endpoint_v1_datasources_project_project_id_get(project_id)

Get Datasources Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datasources import Datasources
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
    api_instance = openapi_client.DataSourcesApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Datasources Endpoint
        api_response = api_instance.get_datasources_endpoint_v1_datasources_project_project_id_get(project_id)
        print("The response of DataSourcesApi->get_datasources_endpoint_v1_datasources_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->get_datasources_endpoint_v1_datasources_project_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[Datasources]**](Datasources.md)

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

# **update_datasource_endpoint_v1_datasources_datasource_id_patch**
> Datasources update_datasource_endpoint_v1_datasources_datasource_id_patch(datasource_id, name=name, type=type, uri=uri)

Update Datasource Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datasources import Datasources
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
    api_instance = openapi_client.DataSourcesApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    name = 'name_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    uri = 'uri_example' # str |  (optional)

    try:
        # Update Datasource Endpoint
        api_response = api_instance.update_datasource_endpoint_v1_datasources_datasource_id_patch(datasource_id, name=name, type=type, uri=uri)
        print("The response of DataSourcesApi->update_datasource_endpoint_v1_datasources_datasource_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->update_datasource_endpoint_v1_datasources_datasource_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **uri** | **str**|  | [optional] 

### Return type

[**Datasources**](Datasources.md)

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

# **upload_source_v1_datasources_datasource_id_upload_post**
> object upload_source_v1_datasources_datasource_id_upload_post(datasource_id, project_id, source_url=source_url, file_type=file_type, file=file)

Upload a data source file

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
    api_instance = openapi_client.DataSourcesApi(api_client)
    datasource_id = 'datasource_id_example' # str | 
    project_id = 'project_id_example' # str | 
    source_url = 'source_url_example' # str |  (optional)
    file_type = 'file_type_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Upload a data source file
        api_response = api_instance.upload_source_v1_datasources_datasource_id_upload_post(datasource_id, project_id, source_url=source_url, file_type=file_type, file=file)
        print("The response of DataSourcesApi->upload_source_v1_datasources_datasource_id_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourcesApi->upload_source_v1_datasources_datasource_id_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 
 **project_id** | **str**|  | 
 **source_url** | **str**|  | [optional] 
 **file_type** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

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
**201** | File successfully uploaded and processed |  -  |
**400** | Invalid file or URL |  -  |
**500** | Internal server error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

