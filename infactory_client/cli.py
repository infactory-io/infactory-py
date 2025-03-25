#!/usr/bin/env python3
import json
import logging
import os
import sys

import typer
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from infactory_client.client import InfactoryClient
from infactory_client.errors import APIError, AuthenticationError, ConfigError

# Initialize Typer app
app = typer.Typer(
    help="Infactory Command Line Interface",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

# Sub-apps for different command groups
organizations_app = typer.Typer(help="Manage organizations", no_args_is_help=True)
projects_app = typer.Typer(help="Manage projects", no_args_is_help=True)
datasources_app = typer.Typer(help="Manage datasources", no_args_is_help=True)
datalines_app = typer.Typer(help="Manage datalines", no_args_is_help=True)
query_app = typer.Typer(help="Manage query programs", no_args_is_help=True)
endpoints_app = typer.Typer(help="Manage endpoints", no_args_is_help=True)
jobs_app = typer.Typer(help="Manage jobs", no_args_is_help=True)
teams_app = typer.Typer(help="Manage teams", no_args_is_help=True)

# Add sub-apps to main app
app.add_typer(organizations_app, name="orgs")
app.add_typer(projects_app, name="projects")
app.add_typer(datasources_app, name="datasources")
app.add_typer(datalines_app, name="datalines")
app.add_typer(query_app, name="query")
app.add_typer(endpoints_app, name="endpoints")
app.add_typer(jobs_app, name="jobs")
app.add_typer(teams_app, name="teams")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("infactory-cli")
logger.setLevel(logging.DEBUG)
console = Console()

load_dotenv()


def get_client() -> InfactoryClient:
    """Get an authenticated client instance."""

    client = InfactoryClient()

    try:
        client.connect()
        return client
    except AuthenticationError:
        raise ConfigError("Invalid API key. Please login again with 'nf login'.")


@app.command()
def login():
    """Login with API key."""
    api_key = os.getenv("NF_API_KEY")
    if not api_key:
        api_key = typer.prompt("Enter your API key", hide_input=True)
    else:
        typer.echo(
            f"Using API key from environment variable starting with {api_key[:7]}..."
        )

    if not api_key:
        typer.echo("API key cannot be empty", err=True)
        raise typer.Exit(1)

    client = InfactoryClient(api_key=api_key)
    try:
        client.connect()
        client.save_api_key(api_key)
        client.save_state()

        # List organizations and set first one as active
        first_org = None
        first_team = None
        first_project = None
        try:
            organizations = client.organizations.list()
            if organizations:
                first_org = organizations[0]
                client.set_current_organization(first_org.id)
            else:
                typer.echo("\nNo organizations found")
            # List teams and set first one as active
            if first_org:
                teams = client.teams.list()
                if teams:
                    first_team = teams[0]
                    client.set_current_team(first_team.id)

                    # List projects and set first one as active
                    try:
                        projects = client.projects.list(team_id=first_team.id)
                        if projects:
                            first_project = projects[0]
                            client.set_current_project(first_project.id)
                        else:
                            typer.echo("\nNo projects found for the selected team")
                    except Exception as e:
                        typer.echo(f"\nWarning: Could not list projects: {e}", err=True)
                else:
                    typer.echo("\nNo teams found for the selected organization")

        except Exception as e:
            typer.echo(f"\nWarning: Could not list organizations: {e}", err=True)

    except AuthenticationError:
        typer.echo("Invalid API key. Please check and try again.", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Failed to login: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def logout():
    """Logout and clear all state information."""
    try:
        # Create a temporary client to get config directory
        client = InfactoryClient()
        config_dir = client._get_config_dir()
        print(f"Config directory: {config_dir}")
        state_file = config_dir / "state.json"
        api_key_file = config_dir / "api_key"

        # Remove state file if it exists
        if state_file.exists():
            state_file.unlink()
            typer.echo("State information cleared.")

        # Remove API key file if it exists
        if api_key_file.exists():
            api_key_file.unlink()
            typer.echo("API key removed.")

        # Check if NF_API_KEY is set in environment
        if os.getenv("NF_API_KEY"):
            typer.echo("\nNOTE: The NF_API_KEY environment variable is still set.")
            typer.echo("To completely logout, you should unset it:")
            typer.echo("  export NF_API_KEY=")

        typer.echo("\nLogout successful!")

    except Exception as e:
        typer.echo(f"Error during logout: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def show(  # noqa: C901
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format")
):
    """Show current state including API key (masked), organization, team, and project."""
    # Create a temporary client to get API key
    client = InfactoryClient()
    api_key = os.getenv("NF_API_KEY") or client._load_api_key_from_file()

    if not api_key:
        typer.echo(
            "Configuration error: No API key found. Please login with 'nf login' or set NF_API_KEY environment variable.",
            err=True,
        )
        raise typer.Exit(1)

    try:
        # Try to get client with current API key
        client = get_client()

        # Format API key for display (show only first and last few characters)
        masked_api_key = (
            f"{api_key[:7]}...{api_key[-4:]}"
            if api_key and len(api_key) > 11
            else "Not set"
        )

        if json_output:
            state_data = {
                "api_key": masked_api_key,
                "user": (
                    {
                        "id": client.state.user_id,
                        "email": client.state.user_email,
                        "name": client.state.user_name,
                        "created_at": client.state.user_created_at,
                    }
                    if client.state.user_id
                    else None
                ),
                "organization": None,
                "team": None,
                "project": None,
            }

            # Add organization info if set
            if client.state.organization_id:
                try:
                    org = client.organizations.get(client.state.organization_id)
                    state_data["organization"] = {
                        "id": client.state.organization_id,
                        "name": org.name,
                    }
                except Exception:
                    state_data["organization"] = {"id": client.state.organization_id}

            # Add team info if set
            if client.state.team_id:
                try:
                    team = client.teams.get(client.state.team_id)
                    state_data["team"] = {"id": client.state.team_id, "name": team.name}
                except Exception:
                    state_data["team"] = {"id": client.state.team_id}

            # Add project info if set
            if client.state.project_id:
                try:
                    project = client.projects.get(client.state.project_id)
                    state_data["project"] = {
                        "id": client.state.project_id,
                        "name": project.name,
                    }
                except Exception:
                    state_data["project"] = {"id": client.state.project_id}

            print(json.dumps(state_data, indent=2))
            return

        # Create a table for better formatting
        table = Table(title="Infactory CLI", show_header=False)
        table.add_column("Setting")
        table.add_column("Value")

        # Add API key
        table.add_row("API Key", masked_api_key)

        # Show user info if set
        if client.state.user_id:
            table.add_row("User ID", client.state.user_id)
            table.add_row("User Email", client.state.user_email or "Not set")
            table.add_row("User Name", client.state.user_name or "Not set")
            table.add_row("User Created At", client.state.user_created_at or "Not set")
        else:
            table.add_row("User", "Not set")

        # Show organization info if set
        if client.state.organization_id:
            try:
                org = client.organizations.get(client.state.organization_id)
                table.add_row(
                    "Organization", f"{org.name} (ID: {client.state.organization_id})"
                )
            except Exception:
                table.add_row("Organization ID", client.state.organization_id)
        else:
            table.add_row("Organization", "Not set")

        # Show team info if set
        if client.state.team_id:
            try:
                team = client.teams.get(client.state.team_id)
                table.add_row("Team", f"{team.name} (ID: {client.state.team_id})")
            except Exception:
                table.add_row("Team ID", client.state.team_id)
        else:
            table.add_row("Team", "Not set")

        # Show project info if set
        if client.state.project_id:
            try:
                project = client.projects.get(client.state.project_id)
                table.add_row(
                    "Project", f"{project.name} (ID: {client.state.project_id})"
                )
            except Exception:
                table.add_row("Project ID", client.state.project_id)
        else:
            table.add_row("Project", "Not set")

        console.print(table)

    except ConfigError as e:
        typer.echo(f"Configuration error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Failed to show state: {e}", err=True)
        raise typer.Exit(1)


@organizations_app.command(name="list")
def organizations_list(
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format")
):
    """List organizations the user has access to."""
    client = get_client()

    try:
        organizations = client.organizations.list()

        if not organizations:
            typer.echo("No organizations found")
            return

        if json_output:
            org_data = [
                {
                    "id": org.id,
                    "name": org.name,
                    "is_current": org.id == client.state.organization_id,
                }
                for org in organizations
            ]
            print(json.dumps(org_data, indent=2))
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Current", justify="center")

        for org in organizations:
            is_current = "✓" if org.id == client.state.organization_id else ""
            table.add_row(org.id, org.name, is_current)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list organizations: {e}", err=True)
        raise typer.Exit(1)


@organizations_app.command(name="set")
def set_organization(organization_id: str):
    """Set current organization."""
    client = get_client()

    try:
        org = client.organizations.get(organization_id)
        client.set_current_organization(org.id)
        typer.echo(f"Current organization set to {org.name} (ID: {org.id})")
    except Exception as e:
        typer.echo(f"Failed to set organization: {e}", err=True)
        raise typer.Exit(1)


@organizations_app.command(name="select")
def organizations_select():
    """Interactively select an organization to set as current."""
    client = get_client()

    try:
        organizations = client.organizations.list()

        if not organizations:
            typer.echo("No organizations found")
            return

        # Create a list of choices
        choices = {str(i): org for i, org in enumerate(organizations, 1)}

        # Display organizations with numbers
        table = Table()
        table.add_column("#")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Current", justify="center")

        for num, org in choices.items():
            is_current = "✓" if org.id == client.state.organization_id else ""
            table.add_row(num, org.id, org.name, is_current)

        console.print(table)

        # Prompt for selection
        choice = Prompt.ask(
            "\nSelect organization number",
            choices=list(choices.keys()),
            show_choices=False,
        )

        selected_org = choices[choice]
        client.set_current_organization(selected_org.id)
        typer.echo(
            f"\nCurrent organization set to {selected_org.name} (ID: {selected_org.id})"
        )

    except Exception as e:
        typer.echo(f"Failed to select organization: {e}", err=True)
        raise typer.Exit(1)


@projects_app.command(name="list")
def projects_list(
    team_id: str | None = typer.Option(None, help="Team ID to list projects for"),
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format"),
):
    """List projects."""
    client = get_client()

    try:
        if team_id:
            projects = client.projects.list(team_id=team_id)
        elif client.state.team_id:
            projects = client.projects.list(team_id=client.state.team_id)
        else:
            typer.echo(
                "No team ID provided. Please specify --team-id or set a current team.",
                err=True,
            )
            raise typer.Exit(1)

        if not projects:
            typer.echo("No projects found")
            return

        if json_output:
            project_data = [
                {
                    "id": project.id,
                    "name": project.name,
                    "description": project.description,
                    "is_current": project.id == client.state.project_id,
                }
                for project in projects
            ]
            print(json.dumps(project_data, indent=2))
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")
        table.add_column("Current", justify="center")

        for project in projects:
            description = project.description or ""
            if len(description) > 47:
                description = description[:47] + "..."
            is_current = "✓" if project.id == client.state.project_id else ""
            table.add_row(project.id, project.name, description, is_current)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list projects: {e}", err=True)
        raise typer.Exit(1)


@projects_app.command(name="set")
def set_project(project_id: str):
    """Set current project."""
    client = get_client()

    try:
        project = client.projects.get(project_id)
        client.set_current_project(project.id)
        typer.echo(f"Current project set to {project.name} (ID: {project.id})")
    except Exception as e:
        typer.echo(f"Failed to set project: {e}", err=True)
        raise typer.Exit(1)


@projects_app.command(name="select")
def projects_select():
    """Interactively select a project to set as current."""
    client = get_client()

    try:
        if not client.state.team_id:
            typer.echo(
                "No team selected. Please select a team first with 'nf teams select'"
            )
            return

        projects = client.projects.list(team_id=client.state.team_id)

        if not projects:
            typer.echo("No projects found")
            return

        # Create a list of choices
        choices = {str(i): project for i, project in enumerate(projects, 1)}

        # Display projects with numbers
        table = Table()
        table.add_column("#")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")
        table.add_column("Current", justify="center")

        for num, project in choices.items():
            description = project.description or ""
            if len(description) > 47:
                description = description[:47] + "..."
            is_current = "✓" if project.id == client.state.project_id else ""
            table.add_row(num, project.id, project.name, description, is_current)

        console.print(table)

        # Prompt for selection
        choice = Prompt.ask(
            "\nSelect project number",
            choices=list(choices.keys()),
            show_choices=False,
        )

        selected_project = choices[choice]
        client.set_current_project(selected_project.id)
        typer.echo(
            f"\nCurrent project set to {selected_project.name} (ID: {selected_project.id})"
        )

    except Exception as e:
        typer.echo(f"Failed to select project: {e}", err=True)
        raise typer.Exit(1)


@datasources_app.command(name="list")
def datasources_list(
    project_id: str | None = typer.Option(
        None, help="Project ID to list datasources for"
    )
):
    """List datasources."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo(
                "No project ID provided. Please specify --project-id or set a current project.",
                err=True,
            )
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id
        datasources = client.datasources.list(project_id=project_id)

        if not datasources:
            typer.echo("No datasources found")
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Type")
        table.add_column("URI")

        for ds in datasources:
            uri = ds.uri or ""
            if len(uri) > 47:
                uri = uri[:47] + "..."
            table.add_row(ds.id, ds.name, ds.type or "", uri)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list datasources: {e}", err=True)
        raise typer.Exit(1)


@datasources_app.command(name="create")
def datasource_create(
    name: str,
    type: str = typer.Option(..., help="Datasource type (e.g. postgres, mysql)"),
    project_id: str | None = typer.Option(
        None, help="Project ID to create datasource in"
    ),
    uri: str | None = typer.Option(None, help="Datasource URI"),
):
    """Create a new datasource."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo(
                "No project ID provided. Please specify --project-id or set a current project.",
                err=True,
            )
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id
        datasource = client.datasources.create(
            name=name,
            project_id=project_id,
            type=type,
            uri=uri,
        )

        typer.echo("Datasource created successfully!")
        typer.echo(f"ID: {datasource.id}")
        typer.echo(f"Name: {datasource.name}")
        typer.echo(f"Type: {datasource.type}")
        if datasource.uri:
            typer.echo(f"URI: {datasource.uri}")

    except Exception as e:
        typer.echo(f"Failed to create datasource: {e}", err=True)
        raise typer.Exit(1)


@datalines_app.command(name="list")
def datalines_list(
    project_id: str | None = typer.Option(
        None, help="Project ID to list datalines for"
    ),
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format"),
):
    """List datalines."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo(
                "No project ID provided. Please specify --project-id or set a current project.",
                err=True,
            )
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id
        datalines = client.datalines.list(project_id=project_id)

        if not datalines:
            typer.echo("No datalines found")
            return

        if json_output:
            datalines_data = [
                {
                    "id": dl.id,
                    "name": dl.name
                    or dl.data_model.get("schemaT", {}).get("name", dl.name),
                    # "data_model": dl.data_model,
                    # "schema_code": dl.schema_code,
                    "project_id": dl.project_id,
                    "dataobject_id": dl.dataobject_id,
                    # "created_at": dl.created_at,
                    # "updated_at": dl.updated_at,
                    # "deleted_at": dl.deleted_at,
                }
                for dl in datalines
            ]
            print(json.dumps(datalines_data))
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")

        for dl in datalines:
            name = dl.name
            if dl.data_model and dl.data_model.get("schemaT"):
                name = dl.data_model["schemaT"].get("name", name) or name
            table.add_row(dl.id, name)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list datalines: {e}", err=True)
        raise typer.Exit(1)


@datalines_app.command(name="select")
def datalines_select(
    model: bool = typer.Option(False, "--model", help="Show data model as JSON"),
    code: bool = typer.Option(False, "--code", help="Show schema code"),
):
    """Interactively select a dataline and show its details."""
    client = get_client()

    if model and code:
        typer.echo("Error: --model and --code cannot be used together", err=True)
        raise typer.Exit(1)

    if not client.state.project_id:
        typer.echo(
            "No project selected. Please select a project first with 'nf projects select'",
            err=True,
        )
        raise typer.Exit(1)

    try:
        datalines = client.datalines.list(project_id=client.state.project_id)

        if not datalines:
            typer.echo("No datalines found")
            return

        # Create a list of choices
        choices = {str(i): dl for i, dl in enumerate(datalines, 1)}

        # Display datalines with numbers
        table = Table()
        table.add_column("#")
        table.add_column("ID")
        table.add_column("Name")

        for num, dl in choices.items():
            table.add_row(num, dl.id, dl.name)

        console.print(table)

        # Prompt for selection
        choice = Prompt.ask(
            "\nSelect dataline number",
            choices=list(choices.keys()),
            show_choices=False,
        )

        selected_dataline = choices[choice]

        if model and selected_dataline.data_model:
            print(json.dumps(selected_dataline.data_model, indent=2))
        elif code and selected_dataline.schema_code:
            print(selected_dataline.schema_code)
        else:
            typer.echo(
                f"\nSelected dataline: {selected_dataline.name} (ID: {selected_dataline.id})"
            )

    except Exception as e:
        typer.echo(f"Failed to select dataline: {e}", err=True)
        raise typer.Exit(1)


@datalines_app.command(name="get")
def datalines_get(
    dataline_id: str,
    model: bool = typer.Option(False, "--model", help="Show data model as JSON"),
    code: bool = typer.Option(False, "--code", help="Show schema code"),
):
    """Get a dataline by ID."""
    client = get_client()

    try:
        if model and code:
            typer.echo("Error: --model and --code cannot be used together", err=True)
            raise typer.Exit(1)

        dataline = client.datalines.get(dataline_id)

        if model and dataline.data_model:
            print(json.dumps(dataline.data_model, indent=2))
        elif code and dataline.schema_code:
            print(dataline.schema_code)
        else:
            typer.echo(f"Dataline: {dataline.name} (ID: {dataline.id})")

    except Exception as e:
        typer.echo(f"Failed to get dataline: {e}", err=True)
        raise typer.Exit(1)


@query_app.command(name="list")
def query_programs_list(
    project_id: str | None = typer.Option(
        None, help="Project ID to list query programs for"
    ),
    include_deleted: bool = typer.Option(False, help="Include deleted query programs"),
):
    """List query programs."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo(
                "No project ID provided. Please specify --project-id or set a current project.",
                err=True,
            )
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id
        query_programs = client.query_programs.list(
            project_id=project_id,
            include_deleted=include_deleted,
        )

        if not query_programs:
            typer.echo("No query programs found")
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Published")
        table.add_column("Public")
        table.add_column("Question")

        for qp in query_programs:
            question = qp.query or ""
            if len(question) > 47:
                question = question[:47] + "..."
            table.add_row(
                qp.id,
                qp.name or "",
                "Yes" if qp.published else "No",
                "Yes" if qp.public else "No",
                question,
            )

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list query programs: {e}", err=True)
        raise typer.Exit(1)


@query_app.command(name="get")
def query_get(
    query_id: str,
    publish: bool = typer.Option(False, "--publish", help="Publish the query program"),
    unpublish: bool = typer.Option(
        False, "--unpublish", help="Unpublish the query program"
    ),
    run: bool = typer.Option(False, "--run", help="Run the query program"),
    analyze: bool = typer.Option(False, "--analyze", help="Analyze the query program"),
):
    """Get a query program by ID and optionally perform actions on it."""
    client = get_client()

    try:
        query_program = client.query_programs.get(query_id)

        if publish and unpublish:
            typer.echo("Error: Cannot use --publish and --unpublish together", err=True)
            raise typer.Exit(1)

        if publish:
            query_program = client.query_programs.publish(query_id)
            typer.echo(f"Query program {query_id} published successfully")

        if unpublish:
            query_program = client.query_programs.unpublish(query_id)
            typer.echo(f"Query program {query_id} unpublished successfully")

        if run:
            result = client.query_programs.evaluate(query_id)
            if isinstance(result, dict) and "data" in result:
                data = result["data"]
                if isinstance(data, list) and data:
                    table = Table()
                    headers = list(data[0].keys())
                    for header in headers:
                        table.add_column(header)

                    for row in data:
                        table.add_row(*[str(row.get(h, "")) for h in headers])

                    console.print(table)
                else:
                    print(json.dumps(data, indent=2))
            else:
                print(json.dumps(result, indent=2))

        if analyze:
            # This is a placeholder for the analyze functionality
            # Implement according to your API's analyze endpoint
            typer.echo("Analyzing query program...")
            analysis = client.query_programs.analyze(query_id)
            print(json.dumps(analysis, indent=2))

        if not any([publish, unpublish, run, analyze]):
            # Display query program details
            table = Table()
            table.add_column("Field")
            table.add_column("Value")

            table.add_row("ID", query_program.id)
            table.add_row("Name", query_program.name or "")
            table.add_row("Published", "Yes" if query_program.published else "No")
            table.add_row("Public", "Yes" if query_program.public else "No")
            table.add_row("Query", query_program.query or "")
            if query_program.created_at:
                table.add_row("Created At", str(query_program.created_at))
            if query_program.updated_at:
                table.add_row("Updated At", str(query_program.updated_at))

            console.print(table)

    except Exception as e:
        typer.echo(f"Failed to get query program: {e}", err=True)
        raise typer.Exit(1)


@query_app.command(name="select")
def query_select(
    publish: bool = typer.Option(
        False, "--publish", help="Publish the selected query program"
    ),
    unpublish: bool = typer.Option(
        False, "--unpublish", help="Unpublish the selected query program"
    ),
    run: bool = typer.Option(False, "--run", help="Run the selected query program"),
    analyze: bool = typer.Option(
        False, "--analyze", help="Analyze the selected query program"
    ),
):
    """Interactively select a query program and optionally perform actions on it."""
    client = get_client()

    if publish and unpublish:
        typer.echo("Error: Cannot use --publish and --unpublish together", err=True)
        raise typer.Exit(1)

    if not client.state.project_id:
        typer.echo(
            "No project selected. Please select a project first with 'nf projects select'",
            err=True,
        )
        raise typer.Exit(1)

    try:
        query_programs = client.query_programs.list(project_id=client.state.project_id)

        if not query_programs:
            typer.echo("No query programs found")
            return

        # Create a list of choices
        choices = {str(i): qp for i, qp in enumerate(query_programs, 1)}

        # Display query programs with numbers
        table = Table()
        table.add_column("#")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Published")
        table.add_column("Public")
        table.add_column("Question")

        for num, qp in choices.items():
            question = qp.query or ""
            if len(question) > 47:
                question = question[:47] + "..."
            table.add_row(
                num,
                qp.id,
                qp.name or "",
                "Yes" if qp.published else "No",
                "Yes" if qp.public else "No",
                question,
            )

        console.print(table)

        # Prompt for selection
        choice = Prompt.ask(
            "\nSelect query program number",
            choices=list(choices.keys()),
            show_choices=False,
        )

        selected_query = choices[choice]
        typer.echo(
            f"\nSelected query program: {selected_query.name} (ID: {selected_query.id})"
        )

        # Handle actions based on flags
        if publish:
            result = client.query_programs.publish(selected_query.id)
            typer.echo(f"Query program {selected_query.id} published successfully")

        if unpublish:
            result = client.query_programs.unpublish(selected_query.id)
            typer.echo(f"Query program {selected_query.id} unpublished successfully")

        if run:
            result = client.query_programs.evaluate(selected_query.id)
            if isinstance(result, dict) and "data" in result:
                data = result["data"]
                if isinstance(data, list) and data:
                    table = Table()
                    headers = list(data[0].keys())
                    for header in headers:
                        table.add_column(header)

                    for row in data:
                        table.add_row(*[str(row.get(h, "")) for h in headers])

                    console.print(table)
                else:
                    print(json.dumps(data, indent=2))
            else:
                print(json.dumps(result, indent=2))

        if analyze:
            # This is a placeholder for the analyze functionality
            # Implement according to your API's analyze endpoint
            typer.echo("Analyzing query program...")
            analysis = client.query_programs.analyze(selected_query.id)
            print(json.dumps(analysis, indent=2))

    except Exception as e:
        typer.echo(f"Failed to select query program: {e}", err=True)
        raise typer.Exit(1)


@endpoints_app.command(name="list")
def endpoints_list(
    project_id: str | None = typer.Option(None, help="Project ID to list endpoints for")
):
    """List endpoints."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo(
                "No project ID provided. Please specify --project-id or set a current project.",
                err=True,
            )
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id

        # Mock data for example
        endpoints = [
            {
                "id": "ep-123abc",
                "name": "Monthly Sales",
                "url": "/v1/live/monthly-sales/v1/data",
                "method": "GET",
            },
            {
                "id": "ep-456def",
                "name": "Product Details",
                "url": "/v1/live/product-details/v1/data",
                "method": "GET",
            },
        ]

        if not endpoints:
            typer.echo("No endpoints found")
            return

        table = Table()
        table.add_column("Endpoint ID")
        table.add_column("Name")
        table.add_column("URL")
        table.add_column("Method")

        for ep in endpoints:
            table.add_row(ep["id"], ep["name"], ep["url"], ep["method"])

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list endpoints: {e}", err=True)
        raise typer.Exit(1)


@endpoints_app.command(name="curl-example")
def endpoints_curl(endpoint_id: str):
    """Show curl example for endpoint."""
    get_client()

    try:
        # Mock data for example
        endpoint = {
            "id": "ep-123abc",
            "name": "Monthly Sales",
            "url": "/v1/live/monthly-sales/v1/data",
            "method": "GET",
        }

        base_url = "https://api.infactory.ai"
        full_url = f"{base_url}{endpoint['url']}"

        typer.echo(f"CURL example for endpoint {endpoint['id']}:\n")
        typer.echo(f'curl -X {endpoint["method"]} "{full_url}" \\')
        typer.echo('  -H "Authorization: Bearer YOUR_API_KEY" \\')
        typer.echo('  -H "Content-Type: application/json"')

    except Exception as e:
        typer.echo(f"Failed to generate curl example: {e}", err=True)
        raise typer.Exit(1)


@jobs_app.command(name="subscribe")
def jobs_subscribe(datasource_id: str):
    """Subscribe to job updates."""
    get_client()

    try:
        typer.echo(f"Subscribing to jobs for datasource {datasource_id}...")

        # Mock data for example
        typer.echo(
            "[2025-03-25 14:30:21] Job j-123456 started: Connecting to PostgreSQL database"
        )
        typer.echo(
            "[2025-03-25 14:30:22] Job j-123456 progress: Successfully connected to database"
        )
        typer.echo(
            "[2025-03-25 14:30:25] Job j-123456 progress: Analyzing table structure"
        )
        typer.echo(
            "[2025-03-25 14:30:30] Job j-123456 progress: Found 12 tables with 450,000 rows total"
        )
        typer.echo(
            "[2025-03-25 14:30:45] Job j-123456 completed: Database connection established and schema analyzed"
        )

    except Exception as e:
        typer.echo(f"Failed to subscribe to jobs: {e}", err=True)
        raise typer.Exit(1)


@teams_app.command(name="list")
def teams_list(
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format")
):
    """List teams the user has access to."""
    client = get_client()

    try:
        teams = client.teams.list()

        if not teams:
            typer.echo("No teams found")
            return

        if json_output:
            team_data = [
                {
                    "id": team.id,
                    "name": team.name,
                    "is_current": team.id == client.state.team_id,
                }
                for team in teams
            ]
            print(json.dumps(team_data, indent=2))
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Current", justify="center")

        for team in teams:
            is_current = "✓" if team.id == client.state.team_id else ""
            table.add_row(team.id, team.name, is_current)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list teams: {e}", err=True)
        raise typer.Exit(1)


@teams_app.command(name="set")
def set_team(team_id: str):
    """Set current team."""
    client = get_client()

    try:
        team = client.teams.get(team_id)
        client.set_current_team(team.id)
        typer.echo(f"Current team set to {team.name} (ID: {team.id})")
    except Exception as e:
        typer.echo(f"Failed to set team: {e}", err=True)
        raise typer.Exit(1)


@teams_app.command(name="select")
def teams_select():
    """Interactively select a team to set as current."""
    client = get_client()

    try:
        teams = client.teams.list()

        if not teams:
            typer.echo("No teams found")
            return

        # Create a list of choices
        choices = {str(i): team for i, team in enumerate(teams, 1)}

        # Display teams with numbers
        table = Table()
        table.add_column("#")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Current", justify="center")

        for num, team in choices.items():
            is_current = "✓" if team.id == client.state.team_id else ""
            table.add_row(num, team.id, team.name, is_current)

        console.print(table)

        # Prompt for selection
        choice = Prompt.ask(
            "\nSelect team number",
            choices=list(choices.keys()),
            show_choices=False,
        )

        selected_team = choices[choice]
        client.set_current_team(selected_team.id)
        typer.echo(
            f"\nCurrent team set to {selected_team.name} (ID: {selected_team.id})"
        )

    except Exception as e:
        typer.echo(f"Failed to select team: {e}", err=True)
        raise typer.Exit(1)


def main():
    """Main entry point for the CLI."""
    try:
        app()
    except ConfigError as e:
        typer.echo(str(e), err=True)
        sys.exit(1)
    except AuthenticationError as e:
        typer.echo(f"Authentication failed: {e}", err=True)
        sys.exit(1)
    except APIError as e:
        typer.echo(f"API error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
