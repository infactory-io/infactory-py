# openapi_client.InfrastructureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_infrastructure_endpoint_v1_infrastructure_post**](InfrastructureApi.md#create_infrastructure_endpoint_v1_infrastructure_post) | **POST** /v1/infrastructure/ | Create Infrastructure Endpoint
[**delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete**](InfrastructureApi.md#delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete) | **DELETE** /v1/infrastructure/{infrastructure_id} | Delete Infrastructure Endpoint
[**get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get**](InfrastructureApi.md#get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get) | **GET** /v1/infrastructure/organization/{organization_id} | Get Infrastructure By Org Endpoint
[**get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get**](InfrastructureApi.md#get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get) | **GET** /v1/infrastructure/{infrastructure_id} | Get Infrastructure Endpoint
[**update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch**](InfrastructureApi.md#update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch) | **PATCH** /v1/infrastructure/{infrastructure_id} | Update Infrastructure Endpoint


# **create_infrastructure_endpoint_v1_infrastructure_post**
> Infrastructure create_infrastructure_endpoint_v1_infrastructure_post(organization_id=organization_id, body_create_infrastructure_endpoint_v1_infrastructure_post=body_create_infrastructure_endpoint_v1_infrastructure_post)

Create Infrastructure Endpoint

### Example


```python
import openapi_client
from openapi_client.models.body_create_infrastructure_endpoint_v1_infrastructure_post import BodyCreateInfrastructureEndpointV1InfrastructurePost
from openapi_client.models.infrastructure import Infrastructure
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
    api_instance = openapi_client.InfrastructureApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    body_create_infrastructure_endpoint_v1_infrastructure_post = openapi_client.BodyCreateInfrastructureEndpointV1InfrastructurePost() # BodyCreateInfrastructureEndpointV1InfrastructurePost |  (optional)

    try:
        # Create Infrastructure Endpoint
        api_response = api_instance.create_infrastructure_endpoint_v1_infrastructure_post(organization_id=organization_id, body_create_infrastructure_endpoint_v1_infrastructure_post=body_create_infrastructure_endpoint_v1_infrastructure_post)
        print("The response of InfrastructureApi->create_infrastructure_endpoint_v1_infrastructure_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->create_infrastructure_endpoint_v1_infrastructure_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **body_create_infrastructure_endpoint_v1_infrastructure_post** | [**BodyCreateInfrastructureEndpointV1InfrastructurePost**](BodyCreateInfrastructureEndpointV1InfrastructurePost.md)|  | [optional] 

### Return type

[**Infrastructure**](Infrastructure.md)

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

# **delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete**
> Infrastructure delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete(infrastructure_id)

Delete Infrastructure Endpoint

### Example


```python
import openapi_client
from openapi_client.models.infrastructure import Infrastructure
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
    api_instance = openapi_client.InfrastructureApi(api_client)
    infrastructure_id = 'infrastructure_id_example' # str | 

    try:
        # Delete Infrastructure Endpoint
        api_response = api_instance.delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete(infrastructure_id)
        print("The response of InfrastructureApi->delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infrastructure_id** | **str**|  | 

### Return type

[**Infrastructure**](Infrastructure.md)

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

# **get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get**
> List[Infrastructure] get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get(organization_id)

Get Infrastructure By Org Endpoint

### Example


```python
import openapi_client
from openapi_client.models.infrastructure import Infrastructure
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
    api_instance = openapi_client.InfrastructureApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Infrastructure By Org Endpoint
        api_response = api_instance.get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get(organization_id)
        print("The response of InfrastructureApi->get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[Infrastructure]**](Infrastructure.md)

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

# **get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get**
> Infrastructure get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get(infrastructure_id)

Get Infrastructure Endpoint

### Example


```python
import openapi_client
from openapi_client.models.infrastructure import Infrastructure
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
    api_instance = openapi_client.InfrastructureApi(api_client)
    infrastructure_id = 'infrastructure_id_example' # str | 

    try:
        # Get Infrastructure Endpoint
        api_response = api_instance.get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get(infrastructure_id)
        print("The response of InfrastructureApi->get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infrastructure_id** | **str**|  | 

### Return type

[**Infrastructure**](Infrastructure.md)

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

# **update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch**
> Infrastructure update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch(infrastructure_id, body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch=body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch)

Update Infrastructure Endpoint

### Example


```python
import openapi_client
from openapi_client.models.body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch import BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch
from openapi_client.models.infrastructure import Infrastructure
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
    api_instance = openapi_client.InfrastructureApi(api_client)
    infrastructure_id = 'infrastructure_id_example' # str | 
    body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch = openapi_client.BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch() # BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch |  (optional)

    try:
        # Update Infrastructure Endpoint
        api_response = api_instance.update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch(infrastructure_id, body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch=body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch)
        print("The response of InfrastructureApi->update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infrastructure_id** | **str**|  | 
 **body_update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch** | [**BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch**](BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch.md)|  | [optional] 

### Return type

[**Infrastructure**](Infrastructure.md)

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

