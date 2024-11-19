# openapi_client.TeamMembershipsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_membership_endpoint_v1_team_memberships_post**](TeamMembershipsApi.md#create_team_membership_endpoint_v1_team_memberships_post) | **POST** /v1/team-memberships/ | Create Team Membership Endpoint
[**delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete**](TeamMembershipsApi.md#delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete) | **DELETE** /v1/team-memberships/{user_id}/{team_id} | Delete Team Membership Endpoint
[**get_team_members_endpoint_v1_team_memberships_team_team_id_get**](TeamMembershipsApi.md#get_team_members_endpoint_v1_team_memberships_team_team_id_get) | **GET** /v1/team-memberships/team/{team_id} | Get Team Members Endpoint
[**get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get**](TeamMembershipsApi.md#get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get) | **GET** /v1/team-memberships/{user_id}/{team_id} | Get Team Membership Endpoint
[**get_user_memberships_endpoint_v1_team_memberships_user_user_id_get**](TeamMembershipsApi.md#get_user_memberships_endpoint_v1_team_memberships_user_user_id_get) | **GET** /v1/team-memberships/user/{user_id} | Get User Memberships Endpoint
[**update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch**](TeamMembershipsApi.md#update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch) | **PATCH** /v1/team-memberships/{user_id}/{team_id} | Update Team Membership Endpoint


# **create_team_membership_endpoint_v1_team_memberships_post**
> UserTeams create_team_membership_endpoint_v1_team_memberships_post(user_id, team_id, role)

Create Team Membership Endpoint

### Example


```python
import openapi_client
from openapi_client.models.team_membership_role import TeamMembershipRole
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    user_id = 'user_id_example' # str | 
    team_id = 'team_id_example' # str | 
    role = openapi_client.TeamMembershipRole() # TeamMembershipRole | 

    try:
        # Create Team Membership Endpoint
        api_response = api_instance.create_team_membership_endpoint_v1_team_memberships_post(user_id, team_id, role)
        print("The response of TeamMembershipsApi->create_team_membership_endpoint_v1_team_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->create_team_membership_endpoint_v1_team_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **team_id** | **str**|  | 
 **role** | [**TeamMembershipRole**](.md)|  | 

### Return type

[**UserTeams**](UserTeams.md)

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

# **delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete**
> UserTeams delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete(user_id, team_id, permanent=permanent)

Delete Team Membership Endpoint

### Example


```python
import openapi_client
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    user_id = 'user_id_example' # str | 
    team_id = 'team_id_example' # str | 
    permanent = False # bool |  (optional) (default to False)

    try:
        # Delete Team Membership Endpoint
        api_response = api_instance.delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete(user_id, team_id, permanent=permanent)
        print("The response of TeamMembershipsApi->delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **team_id** | **str**|  | 
 **permanent** | **bool**|  | [optional] [default to False]

### Return type

[**UserTeams**](UserTeams.md)

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

# **get_team_members_endpoint_v1_team_memberships_team_team_id_get**
> List[UserTeams] get_team_members_endpoint_v1_team_memberships_team_team_id_get(team_id)

Get Team Members Endpoint

### Example


```python
import openapi_client
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Get Team Members Endpoint
        api_response = api_instance.get_team_members_endpoint_v1_team_memberships_team_team_id_get(team_id)
        print("The response of TeamMembershipsApi->get_team_members_endpoint_v1_team_memberships_team_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->get_team_members_endpoint_v1_team_memberships_team_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**List[UserTeams]**](UserTeams.md)

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

# **get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get**
> UserTeams get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get(user_id, team_id)

Get Team Membership Endpoint

### Example


```python
import openapi_client
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    user_id = 'user_id_example' # str | 
    team_id = 'team_id_example' # str | 

    try:
        # Get Team Membership Endpoint
        api_response = api_instance.get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get(user_id, team_id)
        print("The response of TeamMembershipsApi->get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **team_id** | **str**|  | 

### Return type

[**UserTeams**](UserTeams.md)

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

# **get_user_memberships_endpoint_v1_team_memberships_user_user_id_get**
> List[UserTeams] get_user_memberships_endpoint_v1_team_memberships_user_user_id_get(user_id)

Get User Memberships Endpoint

### Example


```python
import openapi_client
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Memberships Endpoint
        api_response = api_instance.get_user_memberships_endpoint_v1_team_memberships_user_user_id_get(user_id)
        print("The response of TeamMembershipsApi->get_user_memberships_endpoint_v1_team_memberships_user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->get_user_memberships_endpoint_v1_team_memberships_user_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[UserTeams]**](UserTeams.md)

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

# **update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch**
> UserTeams update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch(user_id, team_id, role)

Update Team Membership Endpoint

### Example


```python
import openapi_client
from openapi_client.models.team_membership_role import TeamMembershipRole
from openapi_client.models.user_teams import UserTeams
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    user_id = 'user_id_example' # str | 
    team_id = 'team_id_example' # str | 
    role = openapi_client.TeamMembershipRole() # TeamMembershipRole | 

    try:
        # Update Team Membership Endpoint
        api_response = api_instance.update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch(user_id, team_id, role)
        print("The response of TeamMembershipsApi->update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **team_id** | **str**|  | 
 **role** | [**TeamMembershipRole**](.md)|  | 

### Return type

[**UserTeams**](UserTeams.md)

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

