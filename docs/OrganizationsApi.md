# openapi_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_endpoint_v1_orgs_post**](OrganizationsApi.md#create_organization_endpoint_v1_orgs_post) | **POST** /v1/orgs/ | Create Organization Endpoint
[**delete_organization_endpoint_v1_orgs_organization_id_delete**](OrganizationsApi.md#delete_organization_endpoint_v1_orgs_organization_id_delete) | **DELETE** /v1/orgs/{organization_id} | Delete Organization Endpoint
[**get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get**](OrganizationsApi.md#get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get) | **GET** /v1/orgs/clerk/{clerk_org_id} | Get Organization By Clerk Id Endpoint
[**get_organization_endpoint_v1_orgs_organization_id_get**](OrganizationsApi.md#get_organization_endpoint_v1_orgs_organization_id_get) | **GET** /v1/orgs/{organization_id} | Get Organization Endpoint
[**get_organizations_endpoint_v1_orgs_get**](OrganizationsApi.md#get_organizations_endpoint_v1_orgs_get) | **GET** /v1/orgs/ | Get Organizations Endpoint
[**move_organization_endpoint_v1_orgs_organization_id_move_post**](OrganizationsApi.md#move_organization_endpoint_v1_orgs_organization_id_move_post) | **POST** /v1/orgs/{organization_id}/move | Move Organization Endpoint
[**update_organization_endpoint_v1_orgs_organization_id_patch**](OrganizationsApi.md#update_organization_endpoint_v1_orgs_organization_id_patch) | **PATCH** /v1/orgs/{organization_id} | Update Organization Endpoint


# **create_organization_endpoint_v1_orgs_post**
> Organizations create_organization_endpoint_v1_orgs_post(name=name, description=description, platform_id=platform_id, clerk_org_id=clerk_org_id)

Create Organization Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    platform_id = 'platform_id_example' # str |  (optional)
    clerk_org_id = 'clerk_org_id_example' # str |  (optional)

    try:
        # Create Organization Endpoint
        api_response = api_instance.create_organization_endpoint_v1_orgs_post(name=name, description=description, platform_id=platform_id, clerk_org_id=clerk_org_id)
        print("The response of OrganizationsApi->create_organization_endpoint_v1_orgs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization_endpoint_v1_orgs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **platform_id** | **str**|  | [optional] 
 **clerk_org_id** | **str**|  | [optional] 

### Return type

[**Organizations**](Organizations.md)

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

# **delete_organization_endpoint_v1_orgs_organization_id_delete**
> Organizations delete_organization_endpoint_v1_orgs_organization_id_delete(organization_id)

Delete Organization Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Delete Organization Endpoint
        api_response = api_instance.delete_organization_endpoint_v1_orgs_organization_id_delete(organization_id)
        print("The response of OrganizationsApi->delete_organization_endpoint_v1_orgs_organization_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_endpoint_v1_orgs_organization_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**Organizations**](Organizations.md)

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

# **get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get**
> Organizations get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get(clerk_org_id)

Get Organization By Clerk Id Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    clerk_org_id = 'clerk_org_id_example' # str | 

    try:
        # Get Organization By Clerk Id Endpoint
        api_response = api_instance.get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get(clerk_org_id)
        print("The response of OrganizationsApi->get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clerk_org_id** | **str**|  | 

### Return type

[**Organizations**](Organizations.md)

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

# **get_organization_endpoint_v1_orgs_organization_id_get**
> Organizations get_organization_endpoint_v1_orgs_organization_id_get(organization_id)

Get Organization Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Organization Endpoint
        api_response = api_instance.get_organization_endpoint_v1_orgs_organization_id_get(organization_id)
        print("The response of OrganizationsApi->get_organization_endpoint_v1_orgs_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_endpoint_v1_orgs_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**Organizations**](Organizations.md)

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

# **get_organizations_endpoint_v1_orgs_get**
> List[Organizations] get_organizations_endpoint_v1_orgs_get(platform_id=platform_id)

Get Organizations Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    platform_id = 'platform_id_example' # str |  (optional)

    try:
        # Get Organizations Endpoint
        api_response = api_instance.get_organizations_endpoint_v1_orgs_get(platform_id=platform_id)
        print("The response of OrganizationsApi->get_organizations_endpoint_v1_orgs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations_endpoint_v1_orgs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**|  | [optional] 

### Return type

[**List[Organizations]**](Organizations.md)

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

# **move_organization_endpoint_v1_orgs_organization_id_move_post**
> Organizations move_organization_endpoint_v1_orgs_organization_id_move_post(organization_id, new_platform_id)

Move Organization Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    new_platform_id = 'new_platform_id_example' # str | 

    try:
        # Move Organization Endpoint
        api_response = api_instance.move_organization_endpoint_v1_orgs_organization_id_move_post(organization_id, new_platform_id)
        print("The response of OrganizationsApi->move_organization_endpoint_v1_orgs_organization_id_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->move_organization_endpoint_v1_orgs_organization_id_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **new_platform_id** | **str**|  | 

### Return type

[**Organizations**](Organizations.md)

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

# **update_organization_endpoint_v1_orgs_organization_id_patch**
> Organizations update_organization_endpoint_v1_orgs_organization_id_patch(organization_id, name=name, description=description)

Update Organization Endpoint

### Example


```python
import openapi_client
from openapi_client.models.organizations import Organizations
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)

    try:
        # Update Organization Endpoint
        api_response = api_instance.update_organization_endpoint_v1_orgs_organization_id_patch(organization_id, name=name, description=description)
        print("The response of OrganizationsApi->update_organization_endpoint_v1_orgs_organization_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization_endpoint_v1_orgs_organization_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**Organizations**](Organizations.md)

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

