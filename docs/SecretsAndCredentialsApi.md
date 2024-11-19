# openapi_client.SecretsAndCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential_v1_credentials_post**](SecretsAndCredentialsApi.md#create_credential_v1_credentials_post) | **POST** /v1/credentials/ | Create Credential
[**create_secret_endpoint_v1_secrets_team_id_post**](SecretsAndCredentialsApi.md#create_secret_endpoint_v1_secrets_team_id_post) | **POST** /v1/secrets/{team_id} | Create Secret Endpoint
[**delete_all_team_secrets_endpoint_v1_secrets_team_id_delete**](SecretsAndCredentialsApi.md#delete_all_team_secrets_endpoint_v1_secrets_team_id_delete) | **DELETE** /v1/secrets/{team_id} | Delete All Team Secrets Endpoint
[**delete_credential_v1_credentials_credential_id_delete**](SecretsAndCredentialsApi.md#delete_credential_v1_credentials_credential_id_delete) | **DELETE** /v1/credentials/{credential_id} | Delete Credential
[**delete_secret_endpoint_v1_secrets_team_id_key_delete**](SecretsAndCredentialsApi.md#delete_secret_endpoint_v1_secrets_team_id_key_delete) | **DELETE** /v1/secrets/{team_id}/{key} | Delete Secret Endpoint
[**delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete**](SecretsAndCredentialsApi.md#delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete) | **DELETE** /v1/secrets/{team_id}/type/{type} | Delete Secrets By Type Endpoint
[**get_credential_v1_credentials_credential_id_get**](SecretsAndCredentialsApi.md#get_credential_v1_credentials_credential_id_get) | **GET** /v1/credentials/{credential_id} | Get Credential
[**get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get**](SecretsAndCredentialsApi.md#get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get) | **GET** /v1/credentials/datasource/{datasource_id} | Get Credentials By Datasource
[**get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get**](SecretsAndCredentialsApi.md#get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get) | **GET** /v1/credentials/infrastructure/{infrastructure_id} | Get Credentials By Infrastructure
[**get_credentials_by_organization_v1_credentials_organization_organization_id_get**](SecretsAndCredentialsApi.md#get_credentials_by_organization_v1_credentials_organization_organization_id_get) | **GET** /v1/credentials/organization/{organization_id} | Get Credentials By Organization
[**get_credentials_by_team_v1_credentials_team_team_id_get**](SecretsAndCredentialsApi.md#get_credentials_by_team_v1_credentials_team_team_id_get) | **GET** /v1/credentials/team/{team_id} | Get Credentials By Team
[**get_secret_endpoint_v1_secrets_team_id_key_get**](SecretsAndCredentialsApi.md#get_secret_endpoint_v1_secrets_team_id_key_get) | **GET** /v1/secrets/{team_id}/{key} | Get Secret Endpoint
[**get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get**](SecretsAndCredentialsApi.md#get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get) | **GET** /v1/secrets/credentials/{credentials_id} | Get Secrets By Credential Endpoint
[**get_secrets_by_type_endpoint_v1_secrets_team_id_get**](SecretsAndCredentialsApi.md#get_secrets_by_type_endpoint_v1_secrets_team_id_get) | **GET** /v1/secrets/{team_id} | Get Secrets By Type Endpoint
[**import_secrets_endpoint_v1_secrets_team_id_import_post**](SecretsAndCredentialsApi.md#import_secrets_endpoint_v1_secrets_team_id_import_post) | **POST** /v1/secrets/{team_id}/import | Import Secrets Endpoint
[**rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post**](SecretsAndCredentialsApi.md#rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post) | **POST** /v1/secrets/{team_id}/{key}/rotate | Rotate Secret Endpoint
[**update_credential_v1_credentials_credential_id_patch**](SecretsAndCredentialsApi.md#update_credential_v1_credentials_credential_id_patch) | **PATCH** /v1/credentials/{credential_id} | Update Credential
[**update_secret_endpoint_v1_secrets_team_id_key_patch**](SecretsAndCredentialsApi.md#update_secret_endpoint_v1_secrets_team_id_key_patch) | **PATCH** /v1/secrets/{team_id}/{key} | Update Secret Endpoint


# **create_credential_v1_credentials_post**
> object create_credential_v1_credentials_post(credential_create)

Create Credential

### Example


```python
import openapi_client
from openapi_client.models.credential_create import CredentialCreate
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    credential_create = openapi_client.CredentialCreate() # CredentialCreate | 

    try:
        # Create Credential
        api_response = api_instance.create_credential_v1_credentials_post(credential_create)
        print("The response of SecretsAndCredentialsApi->create_credential_v1_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->create_credential_v1_credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_create** | [**CredentialCreate**](CredentialCreate.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_secret_endpoint_v1_secrets_team_id_post**
> List[Secrets] create_secret_endpoint_v1_secrets_team_id_post(team_id, name, type=type, description=description, credentials_id=credentials_id, body_create_secret_endpoint_v1_secrets_team_id_post=body_create_secret_endpoint_v1_secrets_team_id_post)

Create Secret Endpoint

### Example


```python
import openapi_client
from openapi_client.models.body_create_secret_endpoint_v1_secrets_team_id_post import BodyCreateSecretEndpointV1SecretsTeamIdPost
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    name = 'name_example' # str | 
    type = 'type_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    credentials_id = 'credentials_id_example' # str |  (optional)
    body_create_secret_endpoint_v1_secrets_team_id_post = openapi_client.BodyCreateSecretEndpointV1SecretsTeamIdPost() # BodyCreateSecretEndpointV1SecretsTeamIdPost |  (optional)

    try:
        # Create Secret Endpoint
        api_response = api_instance.create_secret_endpoint_v1_secrets_team_id_post(team_id, name, type=type, description=description, credentials_id=credentials_id, body_create_secret_endpoint_v1_secrets_team_id_post=body_create_secret_endpoint_v1_secrets_team_id_post)
        print("The response of SecretsAndCredentialsApi->create_secret_endpoint_v1_secrets_team_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->create_secret_endpoint_v1_secrets_team_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **name** | **str**|  | 
 **type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **credentials_id** | **str**|  | [optional] 
 **body_create_secret_endpoint_v1_secrets_team_id_post** | [**BodyCreateSecretEndpointV1SecretsTeamIdPost**](BodyCreateSecretEndpointV1SecretsTeamIdPost.md)|  | [optional] 

### Return type

[**List[Secrets]**](Secrets.md)

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

# **delete_all_team_secrets_endpoint_v1_secrets_team_id_delete**
> object delete_all_team_secrets_endpoint_v1_secrets_team_id_delete(team_id)

Delete All Team Secrets Endpoint

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Delete All Team Secrets Endpoint
        api_response = api_instance.delete_all_team_secrets_endpoint_v1_secrets_team_id_delete(team_id)
        print("The response of SecretsAndCredentialsApi->delete_all_team_secrets_endpoint_v1_secrets_team_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->delete_all_team_secrets_endpoint_v1_secrets_team_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

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

# **delete_credential_v1_credentials_credential_id_delete**
> object delete_credential_v1_credentials_credential_id_delete(credential_id)

Delete Credential

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Delete Credential
        api_response = api_instance.delete_credential_v1_credentials_credential_id_delete(credential_id)
        print("The response of SecretsAndCredentialsApi->delete_credential_v1_credentials_credential_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->delete_credential_v1_credentials_credential_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

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

# **delete_secret_endpoint_v1_secrets_team_id_key_delete**
> Secrets delete_secret_endpoint_v1_secrets_team_id_key_delete(team_id, key)

Delete Secret Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    key = 'key_example' # str | 

    try:
        # Delete Secret Endpoint
        api_response = api_instance.delete_secret_endpoint_v1_secrets_team_id_key_delete(team_id, key)
        print("The response of SecretsAndCredentialsApi->delete_secret_endpoint_v1_secrets_team_id_key_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->delete_secret_endpoint_v1_secrets_team_id_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**Secrets**](Secrets.md)

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

# **delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete**
> object delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete(team_id, type)

Delete Secrets By Type Endpoint

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    type = 'type_example' # str | 

    try:
        # Delete Secrets By Type Endpoint
        api_response = api_instance.delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete(team_id, type)
        print("The response of SecretsAndCredentialsApi->delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **type** | **str**|  | 

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

# **get_credential_v1_credentials_credential_id_get**
> object get_credential_v1_credentials_credential_id_get(credential_id)

Get Credential

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Get Credential
        api_response = api_instance.get_credential_v1_credentials_credential_id_get(credential_id)
        print("The response of SecretsAndCredentialsApi->get_credential_v1_credentials_credential_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_credential_v1_credentials_credential_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

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

# **get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get**
> object get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get(datasource_id)

Get Credentials By Datasource

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    datasource_id = 'datasource_id_example' # str | 

    try:
        # Get Credentials By Datasource
        api_response = api_instance.get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get(datasource_id)
        print("The response of SecretsAndCredentialsApi->get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_id** | **str**|  | 

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

# **get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get**
> object get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get(infrastructure_id)

Get Credentials By Infrastructure

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    infrastructure_id = 'infrastructure_id_example' # str | 

    try:
        # Get Credentials By Infrastructure
        api_response = api_instance.get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get(infrastructure_id)
        print("The response of SecretsAndCredentialsApi->get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infrastructure_id** | **str**|  | 

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

# **get_credentials_by_organization_v1_credentials_organization_organization_id_get**
> object get_credentials_by_organization_v1_credentials_organization_organization_id_get(organization_id)

Get Credentials By Organization

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Credentials By Organization
        api_response = api_instance.get_credentials_by_organization_v1_credentials_organization_organization_id_get(organization_id)
        print("The response of SecretsAndCredentialsApi->get_credentials_by_organization_v1_credentials_organization_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_credentials_by_organization_v1_credentials_organization_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **get_credentials_by_team_v1_credentials_team_team_id_get**
> object get_credentials_by_team_v1_credentials_team_team_id_get(team_id)

Get Credentials By Team

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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Get Credentials By Team
        api_response = api_instance.get_credentials_by_team_v1_credentials_team_team_id_get(team_id)
        print("The response of SecretsAndCredentialsApi->get_credentials_by_team_v1_credentials_team_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_credentials_by_team_v1_credentials_team_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

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

# **get_secret_endpoint_v1_secrets_team_id_key_get**
> Secrets get_secret_endpoint_v1_secrets_team_id_key_get(team_id, key)

Get Secret Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    key = 'key_example' # str | 

    try:
        # Get Secret Endpoint
        api_response = api_instance.get_secret_endpoint_v1_secrets_team_id_key_get(team_id, key)
        print("The response of SecretsAndCredentialsApi->get_secret_endpoint_v1_secrets_team_id_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_secret_endpoint_v1_secrets_team_id_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **key** | **str**|  | 

### Return type

[**Secrets**](Secrets.md)

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

# **get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get**
> List[Secrets] get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get(credentials_id)

Get Secrets By Credential Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    credentials_id = 'credentials_id_example' # str | 

    try:
        # Get Secrets By Credential Endpoint
        api_response = api_instance.get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get(credentials_id)
        print("The response of SecretsAndCredentialsApi->get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**|  | 

### Return type

[**List[Secrets]**](Secrets.md)

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

# **get_secrets_by_type_endpoint_v1_secrets_team_id_get**
> List[Secrets] get_secrets_by_type_endpoint_v1_secrets_team_id_get(team_id, type=type)

Get Secrets By Type Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    type = 'type_example' # str |  (optional)

    try:
        # Get Secrets By Type Endpoint
        api_response = api_instance.get_secrets_by_type_endpoint_v1_secrets_team_id_get(team_id, type=type)
        print("The response of SecretsAndCredentialsApi->get_secrets_by_type_endpoint_v1_secrets_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->get_secrets_by_type_endpoint_v1_secrets_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **type** | **str**|  | [optional] 

### Return type

[**List[Secrets]**](Secrets.md)

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

# **import_secrets_endpoint_v1_secrets_team_id_import_post**
> List[Secrets] import_secrets_endpoint_v1_secrets_team_id_import_post(team_id, request_body)

Import Secrets Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    request_body = None # List[Optional[object]] | 

    try:
        # Import Secrets Endpoint
        api_response = api_instance.import_secrets_endpoint_v1_secrets_team_id_import_post(team_id, request_body)
        print("The response of SecretsAndCredentialsApi->import_secrets_endpoint_v1_secrets_team_id_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->import_secrets_endpoint_v1_secrets_team_id_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **request_body** | [**List[Optional[object]]**](object.md)|  | 

### Return type

[**List[Secrets]**](Secrets.md)

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

# **rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post**
> Secrets rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post(team_id, key, new_value)

Rotate Secret Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    key = 'key_example' # str | 
    new_value = 'new_value_example' # str | 

    try:
        # Rotate Secret Endpoint
        api_response = api_instance.rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post(team_id, key, new_value)
        print("The response of SecretsAndCredentialsApi->rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **key** | **str**|  | 
 **new_value** | **str**|  | 

### Return type

[**Secrets**](Secrets.md)

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

# **update_credential_v1_credentials_credential_id_patch**
> object update_credential_v1_credentials_credential_id_patch(credential_id, credential_update)

Update Credential

### Example


```python
import openapi_client
from openapi_client.models.credential_update import CredentialUpdate
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    credential_id = 'credential_id_example' # str | 
    credential_update = openapi_client.CredentialUpdate() # CredentialUpdate | 

    try:
        # Update Credential
        api_response = api_instance.update_credential_v1_credentials_credential_id_patch(credential_id, credential_update)
        print("The response of SecretsAndCredentialsApi->update_credential_v1_credentials_credential_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->update_credential_v1_credentials_credential_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **credential_update** | [**CredentialUpdate**](CredentialUpdate.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret_endpoint_v1_secrets_team_id_key_patch**
> Secrets update_secret_endpoint_v1_secrets_team_id_key_patch(team_id, key, value=value, type=type, credentials_id=credentials_id)

Update Secret Endpoint

### Example


```python
import openapi_client
from openapi_client.models.secrets import Secrets
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
    api_instance = openapi_client.SecretsAndCredentialsApi(api_client)
    team_id = 'team_id_example' # str | 
    key = 'key_example' # str | 
    value = 'value_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    credentials_id = 'credentials_id_example' # str |  (optional)

    try:
        # Update Secret Endpoint
        api_response = api_instance.update_secret_endpoint_v1_secrets_team_id_key_patch(team_id, key, value=value, type=type, credentials_id=credentials_id)
        print("The response of SecretsAndCredentialsApi->update_secret_endpoint_v1_secrets_team_id_key_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsAndCredentialsApi->update_secret_endpoint_v1_secrets_team_id_key_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **key** | **str**|  | 
 **value** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **credentials_id** | **str**|  | [optional] 

### Return type

[**Secrets**](Secrets.md)

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

