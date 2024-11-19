# openapi-client
<h2><img src='/logo.svg' alt='Infactory' height='50'></h2><p><ul><li><a href='/er.svg'>Entity-Relationship Diagram</a></li><li><a href='/er.md'>Documentation</a></li></ul></p>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.5.0
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.infactory.ai/contact](https://www.infactory.ai/contact)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling ActionsApi->analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionsApi* | [**analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post**](docs/ActionsApi.md#analyze_data_endpoint_v1_actions_load_analyze_project_id_dataobject_id_post) | **POST** /v1/actions/load/analyze/{project_id}/{dataobject_id} | Analyze Data Endpoint
*ActionsApi* | [**ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post**](docs/ActionsApi.md#ask_endpoint_v1_actions_ask_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/{transform_file_id}/{dataline_id} | Ask Endpoint
*ActionsApi* | [**compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post**](docs/ActionsApi.md#compile_query_endpoint_v1_actions_ask_compile_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/compile/{transform_file_id}/{dataline_id} | Compile Query Endpoint
*ActionsApi* | [**convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post**](docs/ActionsApi.md#convert_data_endpoint_v1_actions_load_convert_project_id_dataobject_id_post) | **POST** /v1/actions/load/convert/{project_id}/{dataobject_id} | Convert Data Endpoint
*ActionsApi* | [**evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post**](docs/ActionsApi.md#evaluate_query_endpoint_v1_actions_ask_evaluate_query_program_id_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/evaluate/{query_program_id}/{transform_file_id}/{dataline_id} | Evaluate Query Endpoint
*ActionsApi* | [**format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post**](docs/ActionsApi.md#format_response_endpoint_v1_actions_ask_format_query_program_id_query_response_id_dataline_id_post) | **POST** /v1/actions/ask/format/{query_program_id}/{query_response_id}/{dataline_id} | Format Response Endpoint
*ActionsApi* | [**generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post**](docs/ActionsApi.md#generate_queries_endpoint_v1_actions_generate_queries_transform_file_id_dataline_id_post) | **POST** /v1/actions/generate/queries/{transform_file_id}/{dataline_id} | Generate Queries Endpoint
*ActionsApi* | [**load_data_endpoint_v1_actions_load_project_id_post**](docs/ActionsApi.md#load_data_endpoint_v1_actions_load_project_id_post) | **POST** /v1/actions/load/{project_id} | Load Data Endpoint
*ActionsApi* | [**prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post**](docs/ActionsApi.md#prepare_data_endpoint_v1_actions_load_prepare_project_id_parquet_file_id_dataline_file_id_post) | **POST** /v1/actions/load/prepare/{project_id}/{parquet_file_id}/{dataline_file_id} | Prepare Data Endpoint
*ActionsApi* | [**update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post**](docs/ActionsApi.md#update_compile_query_endpoint_v1_actions_ask_compile_update_query_program_id_transform_file_id_dataline_id_post) | **POST** /v1/actions/ask/compile/update/{query_program_id}/{transform_file_id}/{dataline_id} | Update Compile Query Endpoint
*ActionsApi* | [**upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post**](docs/ActionsApi.md#upload_data_endpoint_v1_actions_load_upload_project_id_datasource_id_post) | **POST** /v1/actions/load/upload/{project_id}/{datasource_id} | Upload Data Endpoint
*AuthApi* | [**login_v1_authentication_token_post**](docs/AuthApi.md#login_v1_authentication_token_post) | **POST** /v1/authentication/token | Login
*AuthApi* | [**read_users_me_v1_authentication_me_get**](docs/AuthApi.md#read_users_me_v1_authentication_me_get) | **GET** /v1/authentication/me | Read Users Me
*AuthApi* | [**signup_v1_authentication_signup_post**](docs/AuthApi.md#signup_v1_authentication_signup_post) | **POST** /v1/authentication/signup | Signup
*DataLinesApi* | [**create_dataline_endpoint_v1_datalines_post**](docs/DataLinesApi.md#create_dataline_endpoint_v1_datalines_post) | **POST** /v1/datalines/ | Create Dataline Endpoint
*DataLinesApi* | [**create_queryprogram_endpoint_v1_queryprograms_post**](docs/DataLinesApi.md#create_queryprogram_endpoint_v1_queryprograms_post) | **POST** /v1/queryprograms/ | Create Queryprogram Endpoint
*DataLinesApi* | [**create_queryresponse_endpoint_v1_queryresponses_post**](docs/DataLinesApi.md#create_queryresponse_endpoint_v1_queryresponses_post) | **POST** /v1/queryresponses/ | Create Queryresponse Endpoint
*DataLinesApi* | [**delete_dataline_endpoint_v1_datalines_dataline_id_delete**](docs/DataLinesApi.md#delete_dataline_endpoint_v1_datalines_dataline_id_delete) | **DELETE** /v1/datalines/{dataline_id} | Delete Dataline Endpoint
*DataLinesApi* | [**delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete**](docs/DataLinesApi.md#delete_queryprogram_endpoint_v1_queryprograms_queryprogram_id_delete) | **DELETE** /v1/queryprograms/{queryprogram_id} | Delete Queryprogram Endpoint
*DataLinesApi* | [**delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete**](docs/DataLinesApi.md#delete_queryresponse_endpoint_v1_queryresponses_queryresponse_id_delete) | **DELETE** /v1/queryresponses/{queryresponse_id} | Delete Queryresponse Endpoint
*DataLinesApi* | [**get_dataline_endpoint_v1_datalines_dataline_id_get**](docs/DataLinesApi.md#get_dataline_endpoint_v1_datalines_dataline_id_get) | **GET** /v1/datalines/{dataline_id} | Get Dataline Endpoint
*DataLinesApi* | [**get_datalines_endpoint_v1_datalines_project_projects_id_get**](docs/DataLinesApi.md#get_datalines_endpoint_v1_datalines_project_projects_id_get) | **GET** /v1/datalines/project/{projects_id} | Get Datalines Endpoint
*DataLinesApi* | [**get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get**](docs/DataLinesApi.md#get_queryprogram_endpoint_v1_queryprograms_queryprogram_id_get) | **GET** /v1/queryprograms/{queryprogram_id} | Get Queryprogram Endpoint
*DataLinesApi* | [**get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get**](docs/DataLinesApi.md#get_queryprograms_endpoint_v1_queryprograms_dataline_dataline_id_get) | **GET** /v1/queryprograms/dataline/{dataline_id} | Get Queryprograms Endpoint
*DataLinesApi* | [**get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get**](docs/DataLinesApi.md#get_queryresponse_endpoint_v1_queryresponses_queryresponse_id_get) | **GET** /v1/queryresponses/{queryresponse_id} | Get Queryresponse Endpoint
*DataLinesApi* | [**get_queryresponses_endpoint_v1_queryresponses_get**](docs/DataLinesApi.md#get_queryresponses_endpoint_v1_queryresponses_get) | **GET** /v1/queryresponses/ | Get Queryresponses Endpoint
*DataLinesApi* | [**update_dataline_endpoint_v1_datalines_dataline_id_patch**](docs/DataLinesApi.md#update_dataline_endpoint_v1_datalines_dataline_id_patch) | **PATCH** /v1/datalines/{dataline_id} | Update Dataline Endpoint
*DataLinesApi* | [**update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch**](docs/DataLinesApi.md#update_queryprogram_endpoint_v1_queryprograms_queryprogram_id_patch) | **PATCH** /v1/queryprograms/{queryprogram_id} | Update Queryprogram Endpoint
*DataLinesApi* | [**update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch**](docs/DataLinesApi.md#update_queryresponse_endpoint_v1_queryresponses_queryresponse_id_patch) | **PATCH** /v1/queryresponses/{queryresponse_id} | Update Queryresponse Endpoint
*DataSourcesApi* | [**create_datasource_endpoint_v1_datasources_project_id_post**](docs/DataSourcesApi.md#create_datasource_endpoint_v1_datasources_project_id_post) | **POST** /v1/datasources/{project_id} | Create Datasource Endpoint
*DataSourcesApi* | [**delete_datasource_endpoint_v1_datasources_datasource_id_delete**](docs/DataSourcesApi.md#delete_datasource_endpoint_v1_datasources_datasource_id_delete) | **DELETE** /v1/datasources/{datasource_id} | Delete Datasource Endpoint
*DataSourcesApi* | [**get_datasource_endpoint_v1_datasources_datasource_id_get**](docs/DataSourcesApi.md#get_datasource_endpoint_v1_datasources_datasource_id_get) | **GET** /v1/datasources/{datasource_id} | Get Datasource Endpoint
*DataSourcesApi* | [**get_datasources_endpoint_v1_datasources_project_project_id_get**](docs/DataSourcesApi.md#get_datasources_endpoint_v1_datasources_project_project_id_get) | **GET** /v1/datasources/project/{project_id} | Get Datasources Endpoint
*DataSourcesApi* | [**update_datasource_endpoint_v1_datasources_datasource_id_patch**](docs/DataSourcesApi.md#update_datasource_endpoint_v1_datasources_datasource_id_patch) | **PATCH** /v1/datasources/{datasource_id} | Update Datasource Endpoint
*DataSourcesApi* | [**upload_source_v1_datasources_datasource_id_upload_post**](docs/DataSourcesApi.md#upload_source_v1_datasources_datasource_id_upload_post) | **POST** /v1/datasources/{datasource_id}/upload | Upload a data source file
*EventsApi* | [**create_event_endpoint_v1_events_post**](docs/EventsApi.md#create_event_endpoint_v1_events_post) | **POST** /v1/events/ | Create Event Endpoint
*EventsApi* | [**delete_event_endpoint_v1_events_event_id_delete**](docs/EventsApi.md#delete_event_endpoint_v1_events_event_id_delete) | **DELETE** /v1/events/{event_id} | Delete Event Endpoint
*EventsApi* | [**get_event_endpoint_v1_events_event_id_get**](docs/EventsApi.md#get_event_endpoint_v1_events_event_id_get) | **GET** /v1/events/{event_id} | Get Event Endpoint
*EventsApi* | [**get_events_endpoint_v1_events_project_project_id_get**](docs/EventsApi.md#get_events_endpoint_v1_events_project_project_id_get) | **GET** /v1/events/project/{project_id} | Get Events Endpoint
*EventsApi* | [**update_event_endpoint_v1_events_event_id_patch**](docs/EventsApi.md#update_event_endpoint_v1_events_event_id_patch) | **PATCH** /v1/events/{event_id} | Update Event Endpoint
*InfrastructureApi* | [**create_infrastructure_endpoint_v1_infrastructure_post**](docs/InfrastructureApi.md#create_infrastructure_endpoint_v1_infrastructure_post) | **POST** /v1/infrastructure/ | Create Infrastructure Endpoint
*InfrastructureApi* | [**delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete**](docs/InfrastructureApi.md#delete_infrastructure_endpoint_v1_infrastructure_infrastructure_id_delete) | **DELETE** /v1/infrastructure/{infrastructure_id} | Delete Infrastructure Endpoint
*InfrastructureApi* | [**get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get**](docs/InfrastructureApi.md#get_infrastructure_by_org_endpoint_v1_infrastructure_organization_organization_id_get) | **GET** /v1/infrastructure/organization/{organization_id} | Get Infrastructure By Org Endpoint
*InfrastructureApi* | [**get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get**](docs/InfrastructureApi.md#get_infrastructure_endpoint_v1_infrastructure_infrastructure_id_get) | **GET** /v1/infrastructure/{infrastructure_id} | Get Infrastructure Endpoint
*InfrastructureApi* | [**update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch**](docs/InfrastructureApi.md#update_infrastructure_endpoint_v1_infrastructure_infrastructure_id_patch) | **PATCH** /v1/infrastructure/{infrastructure_id} | Update Infrastructure Endpoint
*LegacyApi* | [**dataline_get_dataline_file_name_get**](docs/LegacyApi.md#dataline_get_dataline_file_name_get) | **GET** /dataline/{file_name} | Dataline Get
*LegacyApi* | [**dataline_post_dataline_post**](docs/LegacyApi.md#dataline_post_dataline_post) | **POST** /dataline | Dataline Post
*LegacyApi* | [**manifest_manifest_post**](docs/LegacyApi.md#manifest_manifest_post) | **POST** /manifest | Manifest
*LegacyApi* | [**run_command_with_i7y_exec_post**](docs/LegacyApi.md#run_command_with_i7y_exec_post) | **POST** / | Run Command With I7Y Exec
*OrganizationsApi* | [**create_organization_endpoint_v1_orgs_post**](docs/OrganizationsApi.md#create_organization_endpoint_v1_orgs_post) | **POST** /v1/orgs/ | Create Organization Endpoint
*OrganizationsApi* | [**delete_organization_endpoint_v1_orgs_organization_id_delete**](docs/OrganizationsApi.md#delete_organization_endpoint_v1_orgs_organization_id_delete) | **DELETE** /v1/orgs/{organization_id} | Delete Organization Endpoint
*OrganizationsApi* | [**get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get**](docs/OrganizationsApi.md#get_organization_by_clerk_id_endpoint_v1_orgs_clerk_clerk_org_id_get) | **GET** /v1/orgs/clerk/{clerk_org_id} | Get Organization By Clerk Id Endpoint
*OrganizationsApi* | [**get_organization_endpoint_v1_orgs_organization_id_get**](docs/OrganizationsApi.md#get_organization_endpoint_v1_orgs_organization_id_get) | **GET** /v1/orgs/{organization_id} | Get Organization Endpoint
*OrganizationsApi* | [**get_organizations_endpoint_v1_orgs_get**](docs/OrganizationsApi.md#get_organizations_endpoint_v1_orgs_get) | **GET** /v1/orgs/ | Get Organizations Endpoint
*OrganizationsApi* | [**move_organization_endpoint_v1_orgs_organization_id_move_post**](docs/OrganizationsApi.md#move_organization_endpoint_v1_orgs_organization_id_move_post) | **POST** /v1/orgs/{organization_id}/move | Move Organization Endpoint
*OrganizationsApi* | [**update_organization_endpoint_v1_orgs_organization_id_patch**](docs/OrganizationsApi.md#update_organization_endpoint_v1_orgs_organization_id_patch) | **PATCH** /v1/orgs/{organization_id} | Update Organization Endpoint
*PlatformApi* | [**create_platform_endpoint_v1_platforms_post**](docs/PlatformApi.md#create_platform_endpoint_v1_platforms_post) | **POST** /v1/platforms/ | Create Platform Endpoint
*PlatformApi* | [**delete_platform_endpoint_v1_platforms_platform_id_delete**](docs/PlatformApi.md#delete_platform_endpoint_v1_platforms_platform_id_delete) | **DELETE** /v1/platforms/{platform_id} | Delete Platform Endpoint
*PlatformApi* | [**get_platform_endpoint_v1_platforms_platform_id_get**](docs/PlatformApi.md#get_platform_endpoint_v1_platforms_platform_id_get) | **GET** /v1/platforms/{platform_id} | Get Platform Endpoint
*PlatformApi* | [**get_platforms_endpoint_v1_platforms_get**](docs/PlatformApi.md#get_platforms_endpoint_v1_platforms_get) | **GET** /v1/platforms/ | Get Platforms Endpoint
*PlatformApi* | [**update_platform_endpoint_v1_platforms_platform_id_patch**](docs/PlatformApi.md#update_platform_endpoint_v1_platforms_platform_id_patch) | **PATCH** /v1/platforms/{platform_id} | Update Platform Endpoint
*ProjectsApi* | [**create_project_endpoint_v1_projects_team_id_post**](docs/ProjectsApi.md#create_project_endpoint_v1_projects_team_id_post) | **POST** /v1/projects/{team_id} | Create Project Endpoint
*ProjectsApi* | [**delete_project_endpoint_v1_projects_team_id_project_id_delete**](docs/ProjectsApi.md#delete_project_endpoint_v1_projects_team_id_project_id_delete) | **DELETE** /v1/projects/{team_id}/{project_id} | Delete Project Endpoint
*ProjectsApi* | [**get_project_endpoint_v1_projects_team_id_project_id_get**](docs/ProjectsApi.md#get_project_endpoint_v1_projects_team_id_project_id_get) | **GET** /v1/projects/{team_id}/{project_id} | Get Project Endpoint
*ProjectsApi* | [**get_projects_endpoint_v1_projects_team_id_get**](docs/ProjectsApi.md#get_projects_endpoint_v1_projects_team_id_get) | **GET** /v1/projects/{team_id} | Get Projects Endpoint
*ProjectsApi* | [**move_project_endpoint_v1_projects_team_id_project_id_move_post**](docs/ProjectsApi.md#move_project_endpoint_v1_projects_team_id_project_id_move_post) | **POST** /v1/projects/{team_id}/{project_id}/move | Move Project Endpoint
*ProjectsApi* | [**update_project_endpoint_v1_projects_team_id_project_id_patch**](docs/ProjectsApi.md#update_project_endpoint_v1_projects_team_id_project_id_patch) | **PATCH** /v1/projects/{team_id}/{project_id} | Update Project Endpoint
*RBACApi* | [**create_rbac_endpoint_v1_rbac_post**](docs/RBACApi.md#create_rbac_endpoint_v1_rbac_post) | **POST** /v1/rbac/ | Create Rbac Endpoint
*RBACApi* | [**delete_rbac_endpoint_v1_rbac_rbac_id_delete**](docs/RBACApi.md#delete_rbac_endpoint_v1_rbac_rbac_id_delete) | **DELETE** /v1/rbac/{rbac_id} | Delete Rbac Endpoint
*RBACApi* | [**get_rbac_by_team_endpoint_v1_rbac_team_team_id_get**](docs/RBACApi.md#get_rbac_by_team_endpoint_v1_rbac_team_team_id_get) | **GET** /v1/rbac/team/{team_id} | Get Rbac By Team Endpoint
*RBACApi* | [**get_rbac_by_user_endpoint_v1_rbac_user_user_id_get**](docs/RBACApi.md#get_rbac_by_user_endpoint_v1_rbac_user_user_id_get) | **GET** /v1/rbac/user/{user_id} | Get Rbac By User Endpoint
*RBACApi* | [**get_rbac_endpoint_v1_rbac_rbac_id_get**](docs/RBACApi.md#get_rbac_endpoint_v1_rbac_rbac_id_get) | **GET** /v1/rbac/{rbac_id} | Get Rbac Endpoint
*RBACApi* | [**update_rbac_endpoint_v1_rbac_rbac_id_patch**](docs/RBACApi.md#update_rbac_endpoint_v1_rbac_rbac_id_patch) | **PATCH** /v1/rbac/{rbac_id} | Update Rbac Endpoint
*SecretsAndCredentialsApi* | [**create_credential_v1_credentials_post**](docs/SecretsAndCredentialsApi.md#create_credential_v1_credentials_post) | **POST** /v1/credentials/ | Create Credential
*SecretsAndCredentialsApi* | [**create_secret_endpoint_v1_secrets_team_id_post**](docs/SecretsAndCredentialsApi.md#create_secret_endpoint_v1_secrets_team_id_post) | **POST** /v1/secrets/{team_id} | Create Secret Endpoint
*SecretsAndCredentialsApi* | [**delete_all_team_secrets_endpoint_v1_secrets_team_id_delete**](docs/SecretsAndCredentialsApi.md#delete_all_team_secrets_endpoint_v1_secrets_team_id_delete) | **DELETE** /v1/secrets/{team_id} | Delete All Team Secrets Endpoint
*SecretsAndCredentialsApi* | [**delete_credential_v1_credentials_credential_id_delete**](docs/SecretsAndCredentialsApi.md#delete_credential_v1_credentials_credential_id_delete) | **DELETE** /v1/credentials/{credential_id} | Delete Credential
*SecretsAndCredentialsApi* | [**delete_secret_endpoint_v1_secrets_team_id_key_delete**](docs/SecretsAndCredentialsApi.md#delete_secret_endpoint_v1_secrets_team_id_key_delete) | **DELETE** /v1/secrets/{team_id}/{key} | Delete Secret Endpoint
*SecretsAndCredentialsApi* | [**delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete**](docs/SecretsAndCredentialsApi.md#delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete) | **DELETE** /v1/secrets/{team_id}/type/{type} | Delete Secrets By Type Endpoint
*SecretsAndCredentialsApi* | [**get_credential_v1_credentials_credential_id_get**](docs/SecretsAndCredentialsApi.md#get_credential_v1_credentials_credential_id_get) | **GET** /v1/credentials/{credential_id} | Get Credential
*SecretsAndCredentialsApi* | [**get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get**](docs/SecretsAndCredentialsApi.md#get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get) | **GET** /v1/credentials/datasource/{datasource_id} | Get Credentials By Datasource
*SecretsAndCredentialsApi* | [**get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get**](docs/SecretsAndCredentialsApi.md#get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get) | **GET** /v1/credentials/infrastructure/{infrastructure_id} | Get Credentials By Infrastructure
*SecretsAndCredentialsApi* | [**get_credentials_by_organization_v1_credentials_organization_organization_id_get**](docs/SecretsAndCredentialsApi.md#get_credentials_by_organization_v1_credentials_organization_organization_id_get) | **GET** /v1/credentials/organization/{organization_id} | Get Credentials By Organization
*SecretsAndCredentialsApi* | [**get_credentials_by_team_v1_credentials_team_team_id_get**](docs/SecretsAndCredentialsApi.md#get_credentials_by_team_v1_credentials_team_team_id_get) | **GET** /v1/credentials/team/{team_id} | Get Credentials By Team
*SecretsAndCredentialsApi* | [**get_secret_endpoint_v1_secrets_team_id_key_get**](docs/SecretsAndCredentialsApi.md#get_secret_endpoint_v1_secrets_team_id_key_get) | **GET** /v1/secrets/{team_id}/{key} | Get Secret Endpoint
*SecretsAndCredentialsApi* | [**get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get**](docs/SecretsAndCredentialsApi.md#get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get) | **GET** /v1/secrets/credentials/{credentials_id} | Get Secrets By Credential Endpoint
*SecretsAndCredentialsApi* | [**get_secrets_by_type_endpoint_v1_secrets_team_id_get**](docs/SecretsAndCredentialsApi.md#get_secrets_by_type_endpoint_v1_secrets_team_id_get) | **GET** /v1/secrets/{team_id} | Get Secrets By Type Endpoint
*SecretsAndCredentialsApi* | [**import_secrets_endpoint_v1_secrets_team_id_import_post**](docs/SecretsAndCredentialsApi.md#import_secrets_endpoint_v1_secrets_team_id_import_post) | **POST** /v1/secrets/{team_id}/import | Import Secrets Endpoint
*SecretsAndCredentialsApi* | [**rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post**](docs/SecretsAndCredentialsApi.md#rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post) | **POST** /v1/secrets/{team_id}/{key}/rotate | Rotate Secret Endpoint
*SecretsAndCredentialsApi* | [**update_credential_v1_credentials_credential_id_patch**](docs/SecretsAndCredentialsApi.md#update_credential_v1_credentials_credential_id_patch) | **PATCH** /v1/credentials/{credential_id} | Update Credential
*SecretsAndCredentialsApi* | [**update_secret_endpoint_v1_secrets_team_id_key_patch**](docs/SecretsAndCredentialsApi.md#update_secret_endpoint_v1_secrets_team_id_key_patch) | **PATCH** /v1/secrets/{team_id}/{key} | Update Secret Endpoint
*StatusApi* | [**health_check_health_check_get**](docs/StatusApi.md#health_check_health_check_get) | **GET** /health-check | Health Check
*TasksApi* | [**create_task_endpoint_v1_tasks_post**](docs/TasksApi.md#create_task_endpoint_v1_tasks_post) | **POST** /v1/tasks/ | Create Task Endpoint
*TasksApi* | [**delete_task_endpoint_v1_tasks_task_id_delete**](docs/TasksApi.md#delete_task_endpoint_v1_tasks_task_id_delete) | **DELETE** /v1/tasks/{task_id} | Delete Task Endpoint
*TasksApi* | [**get_task_endpoint_v1_tasks_task_id_get**](docs/TasksApi.md#get_task_endpoint_v1_tasks_task_id_get) | **GET** /v1/tasks/{task_id} | Get Task Endpoint
*TasksApi* | [**get_tasks_endpoint_v1_tasks_project_project_id_get**](docs/TasksApi.md#get_tasks_endpoint_v1_tasks_project_project_id_get) | **GET** /v1/tasks/project/{project_id} | Get Tasks Endpoint
*TasksApi* | [**update_task_endpoint_v1_tasks_task_id_patch**](docs/TasksApi.md#update_task_endpoint_v1_tasks_task_id_patch) | **PATCH** /v1/tasks/{task_id} | Update Task Endpoint
*TeamMembershipsApi* | [**create_team_membership_endpoint_v1_team_memberships_post**](docs/TeamMembershipsApi.md#create_team_membership_endpoint_v1_team_memberships_post) | **POST** /v1/team-memberships/ | Create Team Membership Endpoint
*TeamMembershipsApi* | [**delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete**](docs/TeamMembershipsApi.md#delete_team_membership_endpoint_v1_team_memberships_user_id_team_id_delete) | **DELETE** /v1/team-memberships/{user_id}/{team_id} | Delete Team Membership Endpoint
*TeamMembershipsApi* | [**get_team_members_endpoint_v1_team_memberships_team_team_id_get**](docs/TeamMembershipsApi.md#get_team_members_endpoint_v1_team_memberships_team_team_id_get) | **GET** /v1/team-memberships/team/{team_id} | Get Team Members Endpoint
*TeamMembershipsApi* | [**get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get**](docs/TeamMembershipsApi.md#get_team_membership_endpoint_v1_team_memberships_user_id_team_id_get) | **GET** /v1/team-memberships/{user_id}/{team_id} | Get Team Membership Endpoint
*TeamMembershipsApi* | [**get_user_memberships_endpoint_v1_team_memberships_user_user_id_get**](docs/TeamMembershipsApi.md#get_user_memberships_endpoint_v1_team_memberships_user_user_id_get) | **GET** /v1/team-memberships/user/{user_id} | Get User Memberships Endpoint
*TeamMembershipsApi* | [**update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch**](docs/TeamMembershipsApi.md#update_team_membership_endpoint_v1_team_memberships_user_id_team_id_patch) | **PATCH** /v1/team-memberships/{user_id}/{team_id} | Update Team Membership Endpoint
*TeamsApi* | [**create_team_endpoint_v1_teams_post**](docs/TeamsApi.md#create_team_endpoint_v1_teams_post) | **POST** /v1/teams/ | Create Team Endpoint
*TeamsApi* | [**delete_team_endpoint_v1_teams_team_id_delete**](docs/TeamsApi.md#delete_team_endpoint_v1_teams_team_id_delete) | **DELETE** /v1/teams/{team_id} | Delete Team Endpoint
*TeamsApi* | [**get_team_endpoint_v1_teams_team_id_get**](docs/TeamsApi.md#get_team_endpoint_v1_teams_team_id_get) | **GET** /v1/teams/{team_id} | Get Team Endpoint
*TeamsApi* | [**get_teams_endpoint_v1_teams_get**](docs/TeamsApi.md#get_teams_endpoint_v1_teams_get) | **GET** /v1/teams/ | Get Teams Endpoint
*TeamsApi* | [**move_team_endpoint_v1_teams_team_id_move_post**](docs/TeamsApi.md#move_team_endpoint_v1_teams_team_id_move_post) | **POST** /v1/teams/{team_id}/move | Move Team Endpoint
*TeamsApi* | [**update_team_endpoint_v1_teams_team_id_patch**](docs/TeamsApi.md#update_team_endpoint_v1_teams_team_id_patch) | **PATCH** /v1/teams/{team_id} | Update Team Endpoint
*ToolsApi* | [**ask_dataline_request_v1_tools_ask_dataline_post**](docs/ToolsApi.md#ask_dataline_request_v1_tools_ask_dataline_post) | **POST** /v1/tools/ask-dataline | Ask Dataline Request
*ToolsApi* | [**create_workspace_request_v1_tools_create_workspace_post**](docs/ToolsApi.md#create_workspace_request_v1_tools_create_workspace_post) | **POST** /v1/tools/create-workspace | Create Workspace Request
*ToolsApi* | [**generate_dataline_request_v1_tools_generate_dataline_post**](docs/ToolsApi.md#generate_dataline_request_v1_tools_generate_dataline_post) | **POST** /v1/tools/generate-dataline | Generate Dataline Request
*ToolsApi* | [**generate_queries_request_v1_tools_generate_queries_post**](docs/ToolsApi.md#generate_queries_request_v1_tools_generate_queries_post) | **POST** /v1/tools/generate-queries | Generate Queries Request
*ToolsApi* | [**get_list_of_tools_v1_tools_get**](docs/ToolsApi.md#get_list_of_tools_v1_tools_get) | **GET** /v1/tools/ | List Available Tools
*ToolsApi* | [**get_tool_help_v1_tools_tool_name_get**](docs/ToolsApi.md#get_tool_help_v1_tools_tool_name_get) | **GET** /v1/tools/{tool_name} | Get Tool Information
*ToolsApi* | [**run_tool_v1_tools_tool_name_post**](docs/ToolsApi.md#run_tool_v1_tools_tool_name_post) | **POST** /v1/tools/{tool_name} | Run Tool
*ToolsApi* | [**transform_data_request_v1_tools_transform_data_post**](docs/ToolsApi.md#transform_data_request_v1_tools_transform_data_post) | **POST** /v1/tools/transform-data | Transform Data Request
*UsersApi* | [**create_user_endpoint_v1_users_post**](docs/UsersApi.md#create_user_endpoint_v1_users_post) | **POST** /v1/users/ | Create User Endpoint
*UsersApi* | [**delete_user_endpoint_v1_users_user_id_delete**](docs/UsersApi.md#delete_user_endpoint_v1_users_user_id_delete) | **DELETE** /v1/users/{user_id} | Delete User Endpoint
*UsersApi* | [**get_user_endpoint_v1_users_user_id_get**](docs/UsersApi.md#get_user_endpoint_v1_users_user_id_get) | **GET** /v1/users/{user_id} | Get User Endpoint
*UsersApi* | [**get_users_endpoint_v1_users_get**](docs/UsersApi.md#get_users_endpoint_v1_users_get) | **GET** /v1/users/ | Get Users Endpoint
*UsersApi* | [**move_user_endpoint_v1_users_user_id_move_post**](docs/UsersApi.md#move_user_endpoint_v1_users_user_id_move_post) | **POST** /v1/users/{user_id}/move | Move User Endpoint
*UsersApi* | [**update_user_endpoint_v1_users_user_id_patch**](docs/UsersApi.md#update_user_endpoint_v1_users_user_id_patch) | **PATCH** /v1/users/{user_id} | Update User Endpoint


## Documentation For Models

 - [AskDatalineRequest](docs/AskDatalineRequest.md)
 - [Authentication](docs/Authentication.md)
 - [BodyCreateInfrastructureEndpointV1InfrastructurePost](docs/BodyCreateInfrastructureEndpointV1InfrastructurePost.md)
 - [BodyCreateSecretEndpointV1SecretsTeamIdPost](docs/BodyCreateSecretEndpointV1SecretsTeamIdPost.md)
 - [BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch](docs/BodyUpdateInfrastructureEndpointV1InfrastructureInfrastructureIdPatch.md)
 - [CredentialCreate](docs/CredentialCreate.md)
 - [CredentialUpdate](docs/CredentialUpdate.md)
 - [Credentials](docs/Credentials.md)
 - [DatalineRequest](docs/DatalineRequest.md)
 - [Datalineage](docs/Datalineage.md)
 - [Datalines](docs/Datalines.md)
 - [Dataobjects](docs/Dataobjects.md)
 - [Datasources](docs/Datasources.md)
 - [Events](docs/Events.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Infrastructure](docs/Infrastructure.md)
 - [Organizations](docs/Organizations.md)
 - [Platform](docs/Platform.md)
 - [PlatformCreate](docs/PlatformCreate.md)
 - [Projects](docs/Projects.md)
 - [Queryprograms](docs/Queryprograms.md)
 - [Queryresponses](docs/Queryresponses.md)
 - [Rbac](docs/Rbac.md)
 - [Secrets](docs/Secrets.md)
 - [SourceCredentials](docs/SourceCredentials.md)
 - [Tasks](docs/Tasks.md)
 - [TeamMembershipRole](docs/TeamMembershipRole.md)
 - [Teams](docs/Teams.md)
 - [Tool](docs/Tool.md)
 - [UserCreateInput](docs/UserCreateInput.md)
 - [UserTeams](docs/UserTeams.md)
 - [Users](docs/Users.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [WorkspaceToolRequest](docs/WorkspaceToolRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="APP API Key Bearer"></a>
### APP API Key Bearer

- **Type**: Bearer authentication

<a id="User JWT Bearer"></a>
### User JWT Bearer

- **Type**: Bearer authentication


## Author

support@infactory.ai


