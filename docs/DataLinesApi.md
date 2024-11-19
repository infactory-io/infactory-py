# openapi_client.DataLinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataline_endpoint_v1_datalines_post**](DataLinesApi.md#create_dataline_endpoint_v1_datalines_post) | **POST** /v1/datalines/ | Create Dataline Endpoint
[**create_queryprogram_endpoint_v1_queryprograms_post**](DataLinesApi.md#create_queryprogram_endpoint_v1_queryprograms_post) | **POST** /v1/queryprograms/ | Create Queryprogram Endpoint
[**create_queryresponse_endpoint_v1_queryresponses_post**](DataLinesApi.md#create_queryresponse_endpoint_v1_queryresponses_post) | **POST** /v1/queryresponses/ | Create Queryresponse Endpoint
[**delete_dataline_endpoint_v1_datalines_dataline_id_delete**](DataLinesApi.md#delete_dataline_endpoint_v1_datalines_dataline_id_delete) | **DELETE** /v1/datalines/{dataline_id} | Delete Dataline Endpoint
[**delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete**](DataLinesApi.md#delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete) | **DELETE** /v1/queryprograms/{queryprogram_id} | Delete Queryprogram Endpoint
[**delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete**](DataLinesApi.md#delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete) | **DELETE** /v1/queryresponses/{queryresponse_id} | Delete Queryresponse Endpoint
[**get_dataline_endpoint_v1_datalines_dataline_id_get**](DataLinesApi.md#get_dataline_endpoint_v1_datalines_dataline_id_get) | **GET** /v1/datalines/{dataline_id} | Get Dataline Endpoint
[**get_datalines_endpoint_v1_datalines_project_projects_id_get**](DataLinesApi.md#get_datalines_endpoint_v1_datalines_project_projects_id_get) | **GET** /v1/datalines/project/{projects_id} | Get Datalines Endpoint
[**get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get**](DataLinesApi.md#get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get) | **GET** /v1/queryprograms/{queryprogram_id} | Get Queryprogram Endpoint
[**get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get**](DataLinesApi.md#get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get) | **GET** /v1/queryprograms/dataline/{dataline_id} | Get Queryprograms Endpoint
[**get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get**](DataLinesApi.md#get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get) | **GET** /v1/queryresponses/{queryresponse_id} | Get Queryresponse Endpoint
[**get_queryresponses_endpoint_v1_queryresponses_get**](DataLinesApi.md#get_queryresponses_endpoint_v1_queryresponses_get) | **GET** /v1/queryresponses/ | Get Queryresponses Endpoint
[**update_dataline_endpoint_v1_datalines_dataline_id_patch**](DataLinesApi.md#update_dataline_endpoint_v1_datalines_dataline_id_patch) | **PATCH** /v1/datalines/{dataline_id} | Update Dataline Endpoint
[**update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch**](DataLinesApi.md#update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch) | **PATCH** /v1/queryprograms/{queryprogram_id} | Update Queryprogram Endpoint
[**update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch**](DataLinesApi.md#update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch) | **PATCH** /v1/queryresponses/{queryresponse_id} | Update Queryresponse Endpoint


# **create_dataline_endpoint_v1_datalines_post**
> Datalines create_dataline_endpoint_v1_datalines_post(name=name, dataobject_id=dataobject_id, schema_code=schema_code, project_id=project_id)

Create Dataline Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datalines import Datalines
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
    api_instance = openapi_client.DataLinesApi(api_client)
    name = 'name_example' # str |  (optional)
    dataobject_id = 'dataobject_id_example' # str |  (optional)
    schema_code = 'schema_code_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)

    try:
        # Create Dataline Endpoint
        api_response = api_instance.create_dataline_endpoint_v1_datalines_post(name=name, dataobject_id=dataobject_id, schema_code=schema_code, project_id=project_id)
        print("The response of DataLinesApi->create_dataline_endpoint_v1_datalines_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->create_dataline_endpoint_v1_datalines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **dataobject_id** | **str**|  | [optional] 
 **schema_code** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 

### Return type

[**Datalines**](Datalines.md)

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

# **create_queryprogram_endpoint_v1_queryprograms_post**
> Queryprograms create_queryprogram_endpoint_v1_queryprograms_post(name=name, query=query, query_program=query_program, dataline_id=dataline_id, dataobject_id=dataobject_id)

Create Queryprogram Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryprograms import Queryprograms
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
    api_instance = openapi_client.DataLinesApi(api_client)
    name = 'name_example' # str |  (optional)
    query = 'query_example' # str |  (optional)
    query_program = 'query_program_example' # str |  (optional)
    dataline_id = 'dataline_id_example' # str |  (optional)
    dataobject_id = 'dataobject_id_example' # str |  (optional)

    try:
        # Create Queryprogram Endpoint
        api_response = api_instance.create_queryprogram_endpoint_v1_queryprograms_post(name=name, query=query, query_program=query_program, dataline_id=dataline_id, dataobject_id=dataobject_id)
        print("The response of DataLinesApi->create_queryprogram_endpoint_v1_queryprograms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->create_queryprogram_endpoint_v1_queryprograms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **query_program** | **str**|  | [optional] 
 **dataline_id** | **str**|  | [optional] 
 **dataobject_id** | **str**|  | [optional] 

### Return type

[**Queryprograms**](Queryprograms.md)

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

# **create_queryresponse_endpoint_v1_queryresponses_post**
> Queryresponses create_queryresponse_endpoint_v1_queryresponses_post(object=object, text=text, queryprogram_id=queryprogram_id)

Create Queryresponse Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryresponses import Queryresponses
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
    api_instance = openapi_client.DataLinesApi(api_client)
    object = 'object_example' # str |  (optional)
    text = 'text_example' # str |  (optional)
    queryprogram_id = 'queryprogram_id_example' # str |  (optional)

    try:
        # Create Queryresponse Endpoint
        api_response = api_instance.create_queryresponse_endpoint_v1_queryresponses_post(object=object, text=text, queryprogram_id=queryprogram_id)
        print("The response of DataLinesApi->create_queryresponse_endpoint_v1_queryresponses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->create_queryresponse_endpoint_v1_queryresponses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **queryprogram_id** | **str**|  | [optional] 

### Return type

[**Queryresponses**](Queryresponses.md)

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

# **delete_dataline_endpoint_v1_datalines_dataline_id_delete**
> Datalines delete_dataline_endpoint_v1_datalines_dataline_id_delete(dataline_id, permanent=permanent)

Delete Dataline Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datalines import Datalines
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
    api_instance = openapi_client.DataLinesApi(api_client)
    dataline_id = 'dataline_id_example' # str | 
    permanent = False # bool |  (optional) (default to False)

    try:
        # Delete Dataline Endpoint
        api_response = api_instance.delete_dataline_endpoint_v1_datalines_dataline_id_delete(dataline_id, permanent=permanent)
        print("The response of DataLinesApi->delete_dataline_endpoint_v1_datalines_dataline_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->delete_dataline_endpoint_v1_datalines_dataline_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_id** | **str**|  | 
 **permanent** | **bool**|  | [optional] [default to False]

### Return type

[**Datalines**](Datalines.md)

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

# **delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete**
> Queryprograms delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete(queryprogram_id, permanent=permanent)

Delete Queryprogram Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryprograms import Queryprograms
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryprogram_id = 'queryprogram_id_example' # str | 
    permanent = False # bool |  (optional) (default to False)

    try:
        # Delete Queryprogram Endpoint
        api_response = api_instance.delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete(queryprogram_id, permanent=permanent)
        print("The response of DataLinesApi->delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryprogram_id** | **str**|  | 
 **permanent** | **bool**|  | [optional] [default to False]

### Return type

[**Queryprograms**](Queryprograms.md)

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

# **delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete**
> Queryresponses delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete(queryresponse_id)

Delete Queryresponse Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryresponses import Queryresponses
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryresponse_id = 'queryresponse_id_example' # str | 

    try:
        # Delete Queryresponse Endpoint
        api_response = api_instance.delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete(queryresponse_id)
        print("The response of DataLinesApi->delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryresponse_id** | **str**|  | 

### Return type

[**Queryresponses**](Queryresponses.md)

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

# **get_dataline_endpoint_v1_datalines_dataline_id_get**
> Datalines get_dataline_endpoint_v1_datalines_dataline_id_get(dataline_id)

Get Dataline Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datalines import Datalines
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
    api_instance = openapi_client.DataLinesApi(api_client)
    dataline_id = 'dataline_id_example' # str | 

    try:
        # Get Dataline Endpoint
        api_response = api_instance.get_dataline_endpoint_v1_datalines_dataline_id_get(dataline_id)
        print("The response of DataLinesApi->get_dataline_endpoint_v1_datalines_dataline_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_dataline_endpoint_v1_datalines_dataline_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_id** | **str**|  | 

### Return type

[**Datalines**](Datalines.md)

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

# **get_datalines_endpoint_v1_datalines_project_projects_id_get**
> List[Datalines] get_datalines_endpoint_v1_datalines_project_projects_id_get(projects_id)

Get Datalines Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datalines import Datalines
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
    api_instance = openapi_client.DataLinesApi(api_client)
    projects_id = 'projects_id_example' # str | 

    try:
        # Get Datalines Endpoint
        api_response = api_instance.get_datalines_endpoint_v1_datalines_project_projects_id_get(projects_id)
        print("The response of DataLinesApi->get_datalines_endpoint_v1_datalines_project_projects_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_datalines_endpoint_v1_datalines_project_projects_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_id** | **str**|  | 

### Return type

[**List[Datalines]**](Datalines.md)

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

# **get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get**
> Queryprograms get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get(queryprogram_id)

Get Queryprogram Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryprograms import Queryprograms
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryprogram_id = 'queryprogram_id_example' # str | 

    try:
        # Get Queryprogram Endpoint
        api_response = api_instance.get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get(queryprogram_id)
        print("The response of DataLinesApi->get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryprogram_id** | **str**|  | 

### Return type

[**Queryprograms**](Queryprograms.md)

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

# **get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get**
> List[Queryprograms] get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get(dataline_id)

Get Queryprograms Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryprograms import Queryprograms
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
    api_instance = openapi_client.DataLinesApi(api_client)
    dataline_id = 'dataline_id_example' # str | 

    try:
        # Get Queryprograms Endpoint
        api_response = api_instance.get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get(dataline_id)
        print("The response of DataLinesApi->get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_id** | **str**|  | 

### Return type

[**List[Queryprograms]**](Queryprograms.md)

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

# **get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get**
> Queryresponses get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get(queryresponse_id)

Get Queryresponse Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryresponses import Queryresponses
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryresponse_id = 'queryresponse_id_example' # str | 

    try:
        # Get Queryresponse Endpoint
        api_response = api_instance.get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get(queryresponse_id)
        print("The response of DataLinesApi->get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryresponse_id** | **str**|  | 

### Return type

[**Queryresponses**](Queryresponses.md)

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

# **get_queryresponses_endpoint_v1_queryresponses_get**
> List[Queryresponses] get_queryresponses_endpoint_v1_queryresponses_get(queryprogram_id=queryprogram_id)

Get Queryresponses Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryresponses import Queryresponses
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryprogram_id = 'queryprogram_id_example' # str |  (optional)

    try:
        # Get Queryresponses Endpoint
        api_response = api_instance.get_queryresponses_endpoint_v1_queryresponses_get(queryprogram_id=queryprogram_id)
        print("The response of DataLinesApi->get_queryresponses_endpoint_v1_queryresponses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->get_queryresponses_endpoint_v1_queryresponses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryprogram_id** | **str**|  | [optional] 

### Return type

[**List[Queryresponses]**](Queryresponses.md)

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

# **update_dataline_endpoint_v1_datalines_dataline_id_patch**
> Datalines update_dataline_endpoint_v1_datalines_dataline_id_patch(dataline_id, name=name, dataobject_id=dataobject_id, schema_code=schema_code)

Update Dataline Endpoint

### Example


```python
import openapi_client
from openapi_client.models.datalines import Datalines
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
    api_instance = openapi_client.DataLinesApi(api_client)
    dataline_id = 'dataline_id_example' # str | 
    name = 'name_example' # str |  (optional)
    dataobject_id = 'dataobject_id_example' # str |  (optional)
    schema_code = 'schema_code_example' # str |  (optional)

    try:
        # Update Dataline Endpoint
        api_response = api_instance.update_dataline_endpoint_v1_datalines_dataline_id_patch(dataline_id, name=name, dataobject_id=dataobject_id, schema_code=schema_code)
        print("The response of DataLinesApi->update_dataline_endpoint_v1_datalines_dataline_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->update_dataline_endpoint_v1_datalines_dataline_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataline_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **dataobject_id** | **str**|  | [optional] 
 **schema_code** | **str**|  | [optional] 

### Return type

[**Datalines**](Datalines.md)

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

# **update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch**
> Queryprograms update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch(queryprogram_id, name=name, query=query, query_program=query_program, dataobject_id=dataobject_id)

Update Queryprogram Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryprograms import Queryprograms
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryprogram_id = 'queryprogram_id_example' # str | 
    name = 'name_example' # str |  (optional)
    query = 'query_example' # str |  (optional)
    query_program = 'query_program_example' # str |  (optional)
    dataobject_id = 'dataobject_id_example' # str |  (optional)

    try:
        # Update Queryprogram Endpoint
        api_response = api_instance.update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch(queryprogram_id, name=name, query=query, query_program=query_program, dataobject_id=dataobject_id)
        print("The response of DataLinesApi->update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryprogram_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **query_program** | **str**|  | [optional] 
 **dataobject_id** | **str**|  | [optional] 

### Return type

[**Queryprograms**](Queryprograms.md)

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

# **update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch**
> Queryresponses update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch(queryresponse_id, object=object, text=text, queryprogram_id=queryprogram_id)

Update Queryresponse Endpoint

### Example


```python
import openapi_client
from openapi_client.models.queryresponses import Queryresponses
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
    api_instance = openapi_client.DataLinesApi(api_client)
    queryresponse_id = 'queryresponse_id_example' # str | 
    object = 'object_example' # str |  (optional)
    text = 'text_example' # str |  (optional)
    queryprogram_id = 'queryprogram_id_example' # str |  (optional)

    try:
        # Update Queryresponse Endpoint
        api_response = api_instance.update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch(queryresponse_id, object=object, text=text, queryprogram_id=queryprogram_id)
        print("The response of DataLinesApi->update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataLinesApi->update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryresponse_id** | **str**|  | 
 **object** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **queryprogram_id** | **str**|  | [optional] 

### Return type

[**Queryresponses**](Queryresponses.md)

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

