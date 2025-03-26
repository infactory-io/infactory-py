import os

from infactory_client.base import BaseService, ModelFactory
from infactory_client.models import (
    DataLine,
    DataSource,
    Organization,
    Project,
    QueryProgram,
    Team,
    User,
)


class ProjectsService(BaseService):
    """Service for managing projects."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(Project)

    def list(
        self, team_id: str | None = None, include_deleted: bool = False
    ) -> list[Project]:
        """
        List projects.

        Args:
            team_id: The team ID to filter by
            include_deleted: Whether to include deleted projects

        Returns:
            List of projects
        """
        params = {"include_deleted": include_deleted}
        if team_id:
            params["team_id"] = team_id

        response = self._get("v1/projects", params)
        return self.factory.create_list(response)

    def get(self, project_id: str, team_id: str | None = None) -> Project:
        """
        Get a project by ID.

        Args:
            project_id: The project ID
            team_id: The team ID (optional)

        Returns:
            Project details
        """
        params = {}
        if team_id:
            params["team_id"] = team_id

        response = self._get(f"v1/projects/{project_id}", params)
        return self.factory.create(response)

    def create(
        self, name: str, team_id: str, description: str | None = None
    ) -> Project:
        """
        Create a new project.

        Args:
            name: The project name
            team_id: The team ID
            description: The project description (optional)

        Returns:
            Created project
        """
        data = {"name": name, "team_id": team_id}

        if description:
            data["description"] = description

        response = self._post("v1/projects", data)
        project = self.factory.create(response)

        # Update client state with the current project
        self.client.set_current_project(project.id)

        return project

    def update(
        self, project_id: str, name: str | None = None, description: str | None = None
    ) -> Project:
        """
        Update a project.

        Args:
            project_id: The project ID
            name: The new project name (optional)
            description: The new project description (optional)

        Returns:
            Updated project
        """
        params = {}

        if name:
            params["name"] = name

        if description:
            params["description"] = description

        response = self._patch(f"v1/projects/{project_id}", params=params)
        return self.factory.create(response)

    def delete(self, project_id: str, permanent: bool = False) -> Project:
        """
        Delete a project.

        Args:
            project_id: The project ID
            permanent: Whether to permanently delete the project

        Returns:
            Deleted project
        """
        params = {"permanent": permanent}
        response = self._delete(f"v1/projects/{project_id}", params)

        # If the deleted project is the current one, clear it from state
        if self.client.state.project_id == project_id:
            self.client.state.project_id = None
            self.client.save_state()

        return self.factory.create(response)

    def move(self, project_id: str, new_team_id: str) -> Project:
        """
        Move a project to a different team.

        Args:
            project_id: The project ID
            new_team_id: The new team ID

        Returns:
            Moved project
        """
        params = {"new_team_id": new_team_id}
        response = self._post(f"v1/projects/{project_id}/move", params=params)
        return self.factory.create(response)


class DataSourcesService(BaseService):
    """Service for managing data sources."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(DataSource)

    def list(self, project_id: str | None = None) -> list[DataSource]:
        """
        List data sources for a project.

        Args:
            project_id: The project ID (uses current project if not specified)

        Returns:
            List of data sources
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        response = self._get(f"v1/datasources/project/{project_id}")
        return self.factory.create_list(response)

    def get(self, datasource_id: str) -> DataSource:
        """
        Get a data source by ID.

        Args:
            datasource_id: The data source ID

        Returns:
            Data source details
        """
        response = self._get(f"v1/datasources/{datasource_id}")
        return self.factory.create(response)

    def create(
        self,
        name: str,
        project_id: str | None = None,
        type: str | None = None,
        uri: str | None = None,
    ) -> DataSource:
        """
        Create a new data source.

        Args:
            name: The data source name
            project_id: The project ID (uses current project if not specified)
            type: The data source type (optional)
            uri: The data source URI (optional)

        Returns:
            Created data source
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        data = {"name": name, "project_id": project_id}

        if type:
            data["type"] = type

        if uri:
            data["uri"] = uri

        response = self._post("v1/datasources", data)
        return self.factory.create(response)

    def update(
        self,
        datasource_id: str,
        name: str | None = None,
        type: str | None = None,
        uri: str | None = None,
    ) -> DataSource:
        """
        Update a data source.

        Args:
            datasource_id: The data source ID
            name: The new data source name (optional)
            type: The new data source type (optional)
            uri: The new data source URI (optional)

        Returns:
            Updated data source
        """
        params = {}

        if name:
            params["name"] = name

        if type:
            params["type"] = type

        if uri:
            params["uri"] = uri

        response = self._patch(f"v1/datasources/{datasource_id}", params=params)
        return self.factory.create(response)

    def delete(self, datasource_id: str, permanent: bool = False) -> DataSource:
        """
        Delete a data source.

        Args:
            datasource_id: The data source ID
            permanent: Whether to permanently delete the data source

        Returns:
            Deleted data source
        """
        params = {"permanent": permanent}
        response = self._delete(f"v1/datasources/{datasource_id}", params)
        return self.factory.create(response)

    def load_data(
        self,
        datasource_id: str,
        file_path: str,
        project_id: str | None = None,
        source_url: str | None = None,
        file_type: str | None = None,
        job_id: str | None = None,
    ) -> dict:
        """
        Upload a file to a data source using the load_data endpoint.

        Args:
            datasource_id: The data source ID
            file_path: Path to the file to upload
            project_id: The project ID (uses current project if not specified)
            source_url: Source URL (optional)
            file_type: File type (optional)
            job_id: Job ID for tracking progress (optional)

        Returns:
            Upload response
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        # Prepare query parameters
        params = {}
        if job_id:
            params["job_id"] = job_id
        if source_url:
            params["source_url"] = source_url
        if file_type:
            params["file_type"] = file_type

        # Add API key to query params if needed
        if self.client.api_key:
            params["nf_api_key"] = self.client.api_key

        # Prepare the file for upload
        with open(file_path, "rb") as f:
            # Using httpx directly to handle the multipart/form-data properly
            files = {"file": (os.path.basename(file_path), f)}
            form = {"datasource_id": datasource_id}

            response = self.client.http_client.post(
                f"{self.client.base_url}/v1/actions/load/{project_id}",
                params=params,
                files=files,
                data=form,
            )

            return self.client._handle_response(response)

    # Keep the original method for backward compatibility
    def upload(
        self,
        datasource_id: str,
        file_path: str,
        project_id: str | None = None,
        source_url: str | None = None,
        file_type: str | None = None,
        job_id: str | None = None,
    ) -> dict:
        """
        Upload a file to a data source.

        This method is kept for backward compatibility.
        It calls the new load_data method internally.

        Args:
            datasource_id: The data source ID
            file_path: Path to the file to upload
            project_id: The project ID (uses current project if not specified)
            source_url: Source URL (optional)
            file_type: File type (optional)
            job_id: Job ID for tracking progress (optional)

        Returns:
            Upload response
        """
        return self.load_data(
            datasource_id=datasource_id,
            file_path=file_path,
            project_id=project_id,
            source_url=source_url,
            file_type=file_type,
            job_id=job_id,
        )


class DataLinesService(BaseService):
    """Service for managing data lines."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(DataLine)

    def list(self, project_id: str | None = None) -> list[DataLine]:
        """
        List data lines for a project.

        Args:
            project_id: The project ID (uses current project if not specified)

        Returns:
            List of data lines
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        response = self._get(f"v1/datalines/project/{project_id}")
        return self.factory.create_list(response)

    def get(self, dataline_id: str) -> DataLine:
        """
        Get a data line by ID.

        Args:
            dataline_id: The data line ID

        Returns:
            Data line details
        """
        response = self._get(f"v1/datalines/{dataline_id}")
        return self.factory.create(response)

    def create(
        self,
        name: str,
        project_id: str | None = None,
        dataobject_id: str | None = None,
        schema_code: str | None = None,
        data_model: dict | None = None,
    ) -> DataLine:
        """
        Create a new data line.

        Args:
            name: The data line name
            project_id: The project ID (uses current project if not specified)
            dataobject_id: The data object ID (optional)
            schema_code: The schema code (optional)
            data_model: The data model (optional)

        Returns:
            Created data line
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        params = {"name": name, "project_id": project_id}

        if dataobject_id:
            params["dataobject_id"] = dataobject_id

        if schema_code:
            params["schema_code"] = schema_code

        response = self._post("v1/datalines", params=params, data=data_model)
        return self.factory.create(response)

    def update(
        self,
        dataline_id: str,
        name: str | None = None,
        dataobject_id: str | None = None,
        data_model: dict | None = None,
    ) -> DataLine:
        """
        Update a data line.

        Args:
            dataline_id: The data line ID
            name: The new data line name (optional)
            dataobject_id: The new data object ID (optional)
            data_model: The new data model (optional)

        Returns:
            Updated data line
        """
        params = {}

        if name:
            params["name"] = name

        if dataobject_id:
            params["dataobject_id"] = dataobject_id

        response = self._patch(
            f"v1/datalines/{dataline_id}", params=params, data=data_model
        )
        return self.factory.create(response)

    def update_schema(self, dataline_id: str, schema_code: str) -> DataLine:
        """
        Update a data line's schema.

        Args:
            dataline_id: The data line ID
            schema_code: The new schema code

        Returns:
            Updated data line
        """
        response = self._patch(
            f"v1/datalines/{dataline_id}/schema", data={"schema_code": schema_code}
        )
        return self.factory.create(response)

    def delete(self, dataline_id: str, permanent: bool = False) -> DataLine:
        """
        Delete a data line.

        Args:
            dataline_id: The data line ID
            permanent: Whether to permanently delete the data line

        Returns:
            Deleted data line
        """
        params = {"permanent": permanent}
        response = self._delete(f"v1/datalines/{dataline_id}", params)
        return self.factory.create(response)


class TeamsService(BaseService):
    """Service for managing teams."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(Team)

    def list(self, organization_id: str | None = None) -> list[Team]:
        """
        List teams.

        Args:
            organization_id: The organization ID to filter by (uses current organization if not specified)

        Returns:
            List of teams
        """
        if organization_id is None:
            organization_id = self.client.state.organization_id
            if organization_id is None:
                raise ValueError(
                    "No organization_id provided and no current organization set"
                )

        params = {"organization_id": organization_id}
        response = self._get("v1/teams", params)
        return self.factory.create_list(response)

    def get(self, team_id: str) -> Team:
        """
        Get a team by ID.

        Args:
            team_id: The team ID

        Returns:
            Team details
        """
        response = self._get(f"v1/teams/{team_id}")
        return self.factory.create(response)

    def create(self, name: str, organization_id: str | None = None) -> Team:
        """
        Create a new team.

        Args:
            name: The team name
            organization_id: The organization ID (uses current organization if not specified)

        Returns:
            Created team
        """
        if organization_id is None:
            organization_id = self.client.state.organization_id
            if organization_id is None:
                raise ValueError(
                    "No organization_id provided and no current organization set"
                )

        params = {"name": name, "organization_id": organization_id}

        response = self._post("v1/teams", params=params)
        team = self.factory.create(response)

        # Update client state with the current team
        self.client.set_current_team(team.id)

        return team

    def update(self, team_id: str, name: str) -> Team:
        """
        Update a team.

        Args:
            team_id: The team ID
            name: The new team name

        Returns:
            Updated team
        """
        params = {"name": name}
        response = self._patch(f"v1/teams/{team_id}", params=params)
        return self.factory.create(response)

    def delete(self, team_id: str) -> Team:
        """
        Delete a team.

        Args:
            team_id: The team ID

        Returns:
            Deleted team
        """
        response = self._delete(f"v1/teams/{team_id}")

        # If the deleted team is the current one, clear it from state
        if self.client.state.team_id == team_id:
            self.client.state.team_id = None
            self.client.save_state()

        return self.factory.create(response)

    def move(self, team_id: str, new_organization_id: str) -> Team:
        """
        Move a team to a different organization.

        Args:
            team_id: The team ID
            new_organization_id: The new organization ID

        Returns:
            Moved team
        """
        params = {"new_organization_id": new_organization_id}
        response = self._post(f"v1/teams/{team_id}/move", params=params)
        return self.factory.create(response)


class OrganizationsService(BaseService):
    """Service for managing organizations."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(Organization)

    def list(self, platform_id: str | None = None) -> list[Organization]:
        """
        List organizations.

        Args:
            platform_id: The platform ID to filter by

        Returns:
            List of organizations
        """
        params = {}
        if platform_id:
            params["platform_id"] = platform_id

        response = self.client.get("v1/orgs", params)
        return self.factory.create_list(response)

    def get(self, organization_id: str) -> Organization:
        """
        Get an organization by ID.

        Args:
            organization_id: The organization ID

        Returns:
            Organization details
        """
        response = self._get(f"v1/orgs/{organization_id}")
        return self.factory.create(response)

    def get_by_clerk_id(self, clerk_org_id: str) -> Organization:
        """
        Get an organization by Clerk ID.

        Args:
            clerk_org_id: The Clerk organization ID

        Returns:
            Organization details
        """
        response = self._get(f"v1/orgs/clerk/{clerk_org_id}")
        return self.factory.create(response)

    def create(
        self,
        name: str,
        description: str | None = None,
        platform_id: str | None = None,
        clerk_org_id: str | None = None,
    ) -> Organization:
        """
        Create a new organization.

        Args:
            name: The organization name
            description: The organization description (optional)
            platform_id: The platform ID (optional)
            clerk_org_id: The Clerk organization ID (optional)

        Returns:
            Created organization
        """
        params = {"name": name}

        if description:
            params["description"] = description

        if platform_id:
            params["platform_id"] = platform_id

        if clerk_org_id:
            params["clerk_org_id"] = clerk_org_id

        response = self._post("v1/orgs", params=params)
        org = self.factory.create(response)

        # Update client state with the current organization
        self.client.set_current_organization(org.id)

        return org

    def update(
        self,
        organization_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> Organization:
        """
        Update an organization.

        Args:
            organization_id: The organization ID
            name: The new organization name (optional)
            description: The new organization description (optional)

        Returns:
            Updated organization
        """
        params = {}

        if name:
            params["name"] = name

        if description:
            params["description"] = description

        response = self._patch(f"v1/orgs/{organization_id}", params=params)
        return self.factory.create(response)

    def delete(self, organization_id: str) -> Organization:
        """
        Delete an organization.

        Args:
            organization_id: The organization ID

        Returns:
            Deleted organization
        """
        response = self._delete(f"v1/orgs/{organization_id}")

        # If the deleted organization is the current one, clear it from state
        if self.client.state.organization_id == organization_id:
            self.client.state.organization_id = None
            self.client.save_state()

        return self.factory.create(response)

    def move(self, organization_id: str, new_platform_id: str) -> Organization:
        """
        Move an organization to a different platform.

        Args:
            organization_id: The organization ID
            new_platform_id: The new platform ID

        Returns:
            Moved organization
        """
        params = {"new_platform_id": new_platform_id}
        response = self._post(f"v1/orgs/{organization_id}/move", params=params)
        return self.factory.create(response)


class UsersService(BaseService):
    """Service for managing users."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(User)

    def list(self, organization_id: str | None = None) -> list[User]:
        """
        List users.

        Args:
            organization_id: The organization ID to filter by

        Returns:
            List of users
        """
        params = {}
        if organization_id:
            params["organization_id"] = organization_id

        response = self._get("v1/users", params)
        return self.factory.create_list(response)

    def get(self, user_id: str) -> User:
        """
        Get a user by ID.

        Args:
            user_id: The user ID

        Returns:
            User details
        """
        response = self._get(f"v1/users/{user_id}")
        return self.factory.create(response)

    def get_current(self) -> User:
        """
        Get the current authenticated user.

        Returns:
            Current user details
        """
        response = self._get("v1/authentication/me")
        return self.factory.create(response)

    def create(
        self,
        email: str,
        name: str | None = None,
        organization_id: str | None = None,
        role: str | None = None,
    ) -> User:
        """
        Create a new user.

        Args:
            email: The user email
            name: The user name (optional)
            organization_id: The organization ID (optional)
            role: The user role (optional)

        Returns:
            Created user
        """
        params = {"email": email}

        if name:
            params["name"] = name

        if organization_id:
            params["organization_id"] = organization_id

        if role:
            params["role"] = role

        response = self._post("v1/users", params=params)
        return self.factory.create(response)

    def update(
        self,
        user_id: str,
        email: str | None = None,
        name: str | None = None,
        role: str | None = None,
    ) -> User:
        """
        Update a user.

        Args:
            user_id: The user ID
            email: The new user email (optional)
            name: The new user name (optional)
            role: The new user role (optional)

        Returns:
            Updated user
        """
        params = {}

        if email:
            params["email"] = email

        if name:
            params["name"] = name

        if role:
            params["role"] = role

        response = self._patch(f"v1/users/{user_id}", params=params)
        return self.factory.create(response)

    def delete(self, user_id: str) -> User:
        """
        Delete a user.

        Args:
            user_id: The user ID

        Returns:
            Deleted user
        """
        response = self._delete(f"v1/users/{user_id}")
        return self.factory.create(response)

    def move(self, user_id: str, new_organization_id: str) -> User:
        """
        Move a user to a different organization.

        Args:
            user_id: The user ID
            new_organization_id: The new organization ID

        Returns:
            Moved user
        """
        params = {"new_organization_id": new_organization_id}
        response = self._post(f"v1/users/{user_id}/move", params=params)
        return self.factory.create(response)

    def get_teams_with_organizations_and_projects(
        self,
        user_id: str | None = None,
        clerk_user_id: str | None = None,
        email: str | None = None,
    ) -> dict:
        """
        Get teams, organizations, and projects for a user.

        Args:
            user_id: The user ID (optional)
            clerk_user_id: The Clerk user ID (optional)
            email: The user email (optional)

        Returns:
            Teams, organizations, and projects for the user
        """
        params = {}

        if user_id:
            params["user_id"] = user_id

        if clerk_user_id:
            params["clerk_user_id"] = clerk_user_id

        if email:
            params["email"] = email

        response = self._get(
            "v1/users/get_teams_with_organizations_and_projects", params
        )
        return response


class QueryProgramsService(BaseService):
    """Service for managing query programs."""

    def __init__(self, client):
        super().__init__(client)
        self.factory = ModelFactory(QueryProgram)

    def list(
        self,
        project_id: str | None = None,
        dataline_id: str | None = None,
        skip: int = 0,
        take: int = 100,
        include_deleted: bool = False,
    ) -> list[QueryProgram]:
        """
        List query programs.

        Args:
            project_id: The project ID to filter by (uses current project if not specified)
            dataline_id: The dataline ID to filter by
            skip: Number of records to skip
            take: Number of records to take
            include_deleted: Whether to include deleted query programs

        Returns:
            List of query programs
        """
        if project_id is None and dataline_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        params = {"skip": skip, "take": take, "deleted_at": include_deleted}

        if project_id:
            params["project_id"] = project_id

        if dataline_id:
            endpoint = f"v1/queryprograms/dataline/{dataline_id}"
        else:
            endpoint = "v1/queryprograms"

        response = self._get(endpoint, params)
        return self.factory.create_list(response)

    def get(self, queryprogram_id: str) -> QueryProgram:
        """
        Get a query program by ID.

        Args:
            queryprogram_id: The query program ID

        Returns:
            Query program details
        """
        response = self._get(f"v1/queryprograms/{queryprogram_id}")
        return self.factory.create(response)

    def create(
        self,
        name: str,
        question: str,
        code: str,
        dataline_id: str,
        project_id: str | None = None,
    ) -> QueryProgram:
        """
        Create a new query program.

        Args:
            name: The query program name
            question: The query question
            code: The query code
            dataline_id: The dataline ID
            project_id: The project ID (uses current project if not specified)

        Returns:
            Created query program
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        data = {
            "name": name,
            "question": question,
            "code": code,
            "dataline_id": dataline_id,
            "project_id": project_id,
        }

        response = self._post("v1/queryprograms", data)
        return self.factory.create(response)

    def update(
        self,
        queryprogram_id: str,
        name: str | None = None,
        question: str | None = None,
        code: str | None = None,
    ) -> QueryProgram:
        """
        Update a query program.

        Args:
            queryprogram_id: The query program ID
            name: The new query program name (optional)
            question: The new query question (optional)
            code: The new query code (optional)

        Returns:
            Updated query program
        """
        data = {}

        if name:
            data["name"] = name

        if question:
            data["question"] = question

        if code:
            data["code"] = code

        response = self._patch(f"v1/queryprograms/{queryprogram_id}", data)
        return self.factory.create(response)

    def delete(self, queryprogram_id: str, permanent: bool = False) -> QueryProgram:
        """
        Delete a query program.

        Args:
            queryprogram_id: The query program ID
            permanent: Whether to permanently delete the query program

        Returns:
            Deleted query program
        """
        params = {"permanent": permanent}
        response = self._delete(f"v1/queryprograms/{queryprogram_id}", params)
        return self.factory.create(response)

    def publish(self, queryprogram_id: str, group_slots: bool = False) -> QueryProgram:
        """
        Publish a query program.

        Args:
            queryprogram_id: The query program ID
            group_slots: Whether to group slots

        Returns:
            Published query program
        """
        params = {"group_slots": group_slots}
        response = self._patch(
            f"v1/queryprograms/{queryprogram_id}/publish", params=params
        )
        return self.factory.create(response)

    def unpublish(self, queryprogram_id: str) -> QueryProgram:
        """
        Unpublish a query program.

        Args:
            queryprogram_id: The query program ID

        Returns:
            Unpublished query program
        """
        response = self._patch(f"v1/queryprograms/{queryprogram_id}/unpublish")
        return self.factory.create(response)

    def evaluate(
        self,
        queryprogram_id: str,
        dataline_id: str | None = None,
        project_id: str | None = None,
    ) -> dict:
        """
        Evaluate a query program.

        Args:
            queryprogram_id: The query program ID
            dataline_id: The dataline ID (optional)
            project_id: The project ID (uses current project if not specified)

        Returns:
            Evaluation results
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        data = {"queryprogram_id": queryprogram_id, "project_id": project_id}

        if dataline_id:
            data["dataline_id"] = dataline_id

        response = self._post("v1/actions/evaluate/queryprogram", data)
        return response


class JobsService(BaseService):
    """Service for managing jobs."""

    def submit_job(
        self,
        project_id: str | None = None,
        job_type: str = "upload",
        payload: dict | None = None,
        do_not_send_to_queue: bool = True,
        source_id: str | None = None,
        source: str | None = None,
        source_event_type: str | None = None,
        source_metadata: dict | str | None = None,
    ) -> dict:
        """
        Submit a new job.

        Args:
            project_id: The project ID (uses current project if not specified)
            job_type: The job type (e.g. 'upload', 'process', etc.)
            payload: Job-specific payload data
            do_not_send_to_queue: Whether to not send the job to queue
            source_id: ID of the source object
            source: Source type (e.g. 'datasource')
            source_event_type: Type of source event (e.g. 'file_upload')
            source_metadata: Additional metadata as dict or JSON string

        Returns:
            Job submission response
        """
        if project_id is None:
            project_id = self.client.state.project_id
            if project_id is None:
                raise ValueError("No project_id provided and no current project set")

        # Prepare the job data
        data = {
            "project_id": project_id,
            "job_type": job_type,
            "do_not_send_to_queue": do_not_send_to_queue,
        }

        if payload:
            data["payload"] = payload

        if source_id:
            data["source_id"] = source_id

        if source:
            data["source"] = source

        if source_event_type:
            data["source_event_type"] = source_event_type

        if source_metadata:
            if isinstance(source_metadata, dict):
                import json

                data["source_metadata"] = json.dumps(source_metadata)
            else:
                data["source_metadata"] = source_metadata

        response = self._post("v1/jobs", data)
        return response

    def get_job(self, job_id: str) -> dict:
        """
        Get job details by ID.

        Args:
            job_id: The job ID

        Returns:
            Job details
        """
        response = self._get(f"v1/jobs/{job_id}")
        return response

    def list_jobs(
        self,
        project_id: str | None = None,
        job_type: str | None = None,
        source_id: str | None = None,
        status: str | None = None,
        skip: int = 0,
        take: int = 100,
    ) -> list[dict]:
        """
        List jobs with optional filtering.

        Args:
            project_id: The project ID to filter by
            job_type: Filter by job type
            source_id: Filter by source ID
            status: Filter by job status
            skip: Number of records to skip
            take: Number of records to take

        Returns:
            List of jobs
        """
        params = {"skip": skip, "take": take}

        if project_id:
            params["project_id"] = project_id

        if job_type:
            params["job_type"] = job_type

        if source_id:
            params["source_id"] = source_id

        if status:
            params["status"] = status

        response = self._get("v1/jobs", params)
        return response

    def subscribe_to_job_events(
        self, source_id: str | None = None, job_id: str | None = None
    ) -> dict:
        """
        Subscribe to job events via server-sent events.

        This is a placeholder for the SSE implementation.
        In a real implementation, this would return a streaming connection.

        Args:
            source_id: The source ID to filter events by
            job_id: The job ID to filter events by

        Returns:
            Subscription details
        """
        params = {}

        if source_id:
            params["source_id"] = source_id

        if job_id:
            params["job_id"] = job_id

        # This would be implemented with SSE or WebSockets in a real client
        response = {"status": "subscribed", "source_id": source_id, "job_id": job_id}
        return response
