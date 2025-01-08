# coding: utf-8

"""
    Find the knowledge in your data

    <h2><img src='/logo.svg' alt='Infactory' height='50'></h2><p><ul><li><a href='/er.svg'>Entity-Relationship Diagram</a></li><li><a href='/er.md'>Documentation</a></li></ul></p>

    The version of the OpenAPI document: 0.5.0
    Contact: support@infactory.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from infactory_client.models.tasks import Tasks

class TestTasks(unittest.TestCase):
    """Tasks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tasks:
        """Test Tasks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tasks`
        """
        model = Tasks()
        if include_optional:
            return Tasks(
                id = '',
                task_type = '',
                status = '',
                schedule = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                project_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                projects = openapi_client.models.projects.projects(
                    id = '', 
                    name = '', 
                    team_id = '', 
                    description = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    datasources = [
                        openapi_client.models.datasources.datasources(
                            id = '', 
                            name = '', 
                            type = '', 
                            uri = '', 
                            project_id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            credentials = [
                                openapi_client.models.credentials.credentials(
                                    id = '', 
                                    name = '', 
                                    description = '', 
                                    metadata = null, 
                                    datasource_id = '', 
                                    team_id = '', 
                                    organization_id = '', 
                                    infrastructure_id = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    infrastructure = openapi_client.models.infrastructure.infrastructure(
                                        id = '', 
                                        organization_id = '', 
                                        resources_allocated = null, 
                                        limits = null, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        organizations = openapi_client.models.organizations.organizations(
                                            id = '', 
                                            name = '', 
                                            description = '', 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            platform_id = '', 
                                            platform = openapi_client.models.platform.platform(
                                                id = '', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                description = '', 
                                                metadata = null, 
                                                name = '', ), 
                                            teams = [
                                                openapi_client.models.teams.teams(
                                                    id = '', 
                                                    name = '', 
                                                    organization_id = '', 
                                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    rbac = [
                                                        openapi_client.models.rbac.rbac(
                                                            id = '', 
                                                            role_name = '', 
                                                            permissions = null, 
                                                            user_id = '', 
                                                            team_id = '', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            users = openapi_client.models.users.users(
                                                                email = '', 
                                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                name = '', 
                                                                organization_id = '', 
                                                                role = '', 
                                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                id = '', 
                                                                authentication = [
                                                                    openapi_client.models.authentication.authentication(
                                                                        id = '', 
                                                                        token = '', 
                                                                        user_id = '', 
                                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                                    ], 
                                                                user_teams = [
                                                                    openapi_client.models.user_teams.user_teams(
                                                                        id = '', 
                                                                        user_id = '', 
                                                                        team_id = '', 
                                                                        role = '', 
                                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        team = openapi_client.models.teams.teams(
                                                                            id = '', 
                                                                            name = '', 
                                                                            organization_id = '', 
                                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                            secrets = [
                                                                                openapi_client.models.secrets.secrets(
                                                                                    id = '', 
                                                                                    key = '', 
                                                                                    value = '', 
                                                                                    team_id = '', 
                                                                                    type = '', 
                                                                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                                    credentials_id = '', )
                                                                                ], ), 
                                                                        user = openapi_client.models.users.users(
                                                                            email = '', 
                                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                            name = '', 
                                                                            organization_id = '', 
                                                                            role = '', 
                                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                            id = '', ), )
                                                                    ], ), )
                                                        ], 
                                                    secrets = [
                                                        openapi_client.models.secrets.secrets(
                                                            id = '', 
                                                            key = '', 
                                                            value = '', 
                                                            team_id = '', 
                                                            type = '', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            credentials_id = '', )
                                                        ], 
                                                    user_teams = [
                                                        openapi_client.models.user_teams.user_teams(
                                                            id = '', 
                                                            user_id = '', 
                                                            team_id = '', 
                                                            role = '', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                        ], )
                                                ], 
                                            users = [
                                                
                                                ], 
                                            clerk_org_id = '', ), ), 
                                    organizations = openapi_client.models.organizations.organizations(
                                        id = '', 
                                        name = '', 
                                        description = '', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        platform_id = '', 
                                        clerk_org_id = '', ), 
                                    teams = , 
                                    secrets = , )
                                ], 
                            dataobjects = [
                                openapi_client.models.dataobjects.dataobjects(
                                    id = '', 
                                    bucket = '', 
                                    key = '', 
                                    file_type = '', 
                                    file_size = 56, 
                                    etag = '', 
                                    mime_type = '', 
                                    metadata = null, 
                                    datasource_id = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    downstream_lineage = [
                                        openapi_client.models.datalineage.datalineage(
                                            id = '', 
                                            upstream_id = '', 
                                            downstream_id = '', 
                                            transformation = '', 
                                            metadata = null, 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            downstream = openapi_client.models.dataobjects.dataobjects(
                                                id = '', 
                                                bucket = '', 
                                                key = '', 
                                                file_type = '', 
                                                file_size = 56, 
                                                etag = '', 
                                                mime_type = '', 
                                                metadata = null, 
                                                datasource_id = '', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                upstream_lineage = [
                                                    openapi_client.models.datalineage.datalineage(
                                                        id = '', 
                                                        upstream_id = '', 
                                                        downstream_id = '', 
                                                        transformation = '', 
                                                        metadata = null, 
                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        upstream = , )
                                                    ], 
                                                datalines = [
                                                    openapi_client.models.datalines.datalines(
                                                        id = '', 
                                                        name = '', 
                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        dataobject_id = '', 
                                                        schema_code = '', 
                                                        project_id = '', 
                                                        queryprograms = [
                                                            openapi_client.models.queryprograms.queryprograms(
                                                                id = '', 
                                                                dataline_id = '', 
                                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                name = '', 
                                                                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                dataobject_id = '', 
                                                                query = '', 
                                                                query_program = '', 
                                                                queryresponses = [
                                                                    openapi_client.models.queryresponses.queryresponses(
                                                                        id = '', 
                                                                        object = '', 
                                                                        text = '', 
                                                                        queryprogram_id = '', 
                                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                                    ], )
                                                            ], )
                                                    ], 
                                                queryprograms = [
                                                    openapi_client.models.queryprograms.queryprograms(
                                                        id = '', 
                                                        dataline_id = '', 
                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        name = '', 
                                                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        dataobject_id = '', 
                                                        query = '', 
                                                        query_program = '', )
                                                    ], ), 
                                            upstream = , )
                                        ], 
                                    upstream_lineage = [
                                        
                                        ], 
                                    datalines = [
                                        openapi_client.models.datalines.datalines(
                                            id = '', 
                                            name = '', 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            dataobject_id = '', 
                                            schema_code = '', 
                                            project_id = '', )
                                        ], 
                                    queryprograms = , )
                                ], )
                        ], 
                    events = [
                        openapi_client.models.events.events(
                            id = '', 
                            event_type = '', 
                            description = '', 
                            timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            project_id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    teams = , 
                    tasks = [
                        openapi_client.models.tasks.tasks(
                            id = '', 
                            task_type = '', 
                            status = '', 
                            schedule = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            project_id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    datalines = , )
            )
        else:
            return Tasks(
                id = '',
        )
        """

    def testTasks(self):
        """Test Tasks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
