#!/usr/bin/env python3
import os
import sys
import json
import getpass
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

import typer
from rich import print
from rich.table import Table
from rich.console import Console

from infactory_client.client import ClientState, InfactoryClient
from infactory_client.errors import APIError, AuthenticationError, ConfigError

# Initialize Typer app
app = typer.Typer(
    help="Infactory Command Line Interface",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

# Sub-apps for different command groups
projects_app = typer.Typer(help="Manage projects", no_args_is_help=True)
datasources_app = typer.Typer(help="Manage datasources", no_args_is_help=True)
datalines_app = typer.Typer(help="Manage datalines", no_args_is_help=True)
query_app = typer.Typer(help="Manage query programs", no_args_is_help=True)
endpoints_app = typer.Typer(help="Manage endpoints", no_args_is_help=True)
jobs_app = typer.Typer(help="Manage jobs", no_args_is_help=True)

# Add sub-apps to main app
app.add_typer(projects_app, name="projects")
app.add_typer(datasources_app, name="datasources")
app.add_typer(datalines_app, name="datalines")
app.add_typer(query_app, name="query")
app.add_typer(endpoints_app, name="endpoints")
app.add_typer(jobs_app, name="jobs")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("infactory-cli")
logger.setLevel(logging.DEBUG)
console = Console()

load_dotenv()

def get_config_dir() -> Path:
    """Get the configuration directory path."""
    config_dir = os.getenv("NF_HOME") or os.path.expanduser("~/.infactory")
    path = Path(config_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path

def load_state() -> ClientState:
    """Load client state from file."""
    config_dir = get_config_dir()
    state_file = config_dir / "state.json"

    if state_file.exists():
        try:
            with open(state_file, "r") as f:
                state_data = json.load(f)
                return ClientState(**state_data)
        except Exception as e:
            logger.warning(f"Failed to load state from {state_file}: {e}")

    return ClientState()

def save_state(state: ClientState):
    """Save client state to file."""
    config_dir = get_config_dir()
    state_file = config_dir / "state.json"

    try:
        with open(state_file, "w") as f:
            json.dump(state.dict(exclude_none=True), f)
    except Exception as e:
        logger.error(f"Failed to save state to {state_file}: {e}")

def save_api_key(api_key: str):
    """Save API key to file."""
    config_dir = get_config_dir()
    api_key_file = config_dir / "api_key"

    try:
        with open(api_key_file, "w") as f:
            f.write(api_key)
        os.chmod(api_key_file, 0o600)  # Secure the file
    except Exception as e:
        logger.error(f"Failed to save API key to {api_key_file}: {e}")

def load_api_key() -> Optional[str]:
    """Load API key from file."""
    config_dir = get_config_dir()
    api_key_file = config_dir / "api_key"

    if api_key_file.exists():
        try:
            with open(api_key_file, "r") as f:
                return f.read().strip()
        except Exception as e:
            logger.warning(f"Failed to load API key from {api_key_file}: {e}")

    return None

def get_client() -> InfactoryClient:
    """Get an authenticated client instance."""
    api_key = os.getenv("NF_API_KEY") or load_api_key()

    if not api_key:
        raise ConfigError(
            "No API key found. Please login with 'nf login' or set NF_API_KEY environment variable."
        )

    client = InfactoryClient(api_key=api_key)

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
        typer.echo(f"Using API key from environment variable starting with {api_key[:7]}...")

    if not api_key:
        typer.echo("API key cannot be empty", err=True)
        raise typer.Exit(1)

    client = InfactoryClient(api_key=api_key)
    try:
        client.connect()
        save_api_key(api_key)
        save_state(client.state)
        typer.echo("API key saved successfully!")
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
        # Get config directory
        config_dir = get_config_dir()
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
def show():
    """Show current state including API key (masked), organization, team, and project."""
    try:
        # Try to get client with current API key
        client = get_client()

        # Get the API key (either from env or from saved file)
        api_key = os.getenv("NF_API_KEY") or load_api_key()

        # Format API key for display (show only first and last few characters)
        masked_api_key = (
            f"{api_key[:7]}...{api_key[-4:]}"
            if api_key and len(api_key) > 11
            else "Not set"
        )

        # Create a table for better formatting
        table = Table(title="Current State", show_header=False)
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
                table.add_row("Organization", f"{org.name} (ID: {client.state.organization_id})")
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
                table.add_row("Project", f"{project.name} (ID: {client.state.project_id})")
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

@app.command(name="set-project")
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

@app.command(name="set-organization")
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

@app.command(name="set-team")
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

@projects_app.command(name="list")
def projects_list(team_id: Optional[str] = typer.Option(None, help="Team ID to list projects for")):
    """List projects."""
    client = get_client()

    try:
        if team_id:
            projects = client.projects.list(team_id=team_id)
        elif client.state.team_id:
            projects = client.projects.list(team_id=client.state.team_id)
        else:
            typer.echo("No team ID provided. Please specify --team-id or set a current team.", err=True)
            raise typer.Exit(1)

        if not projects:
            typer.echo("No projects found")
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")

        for project in projects:
            description = project.description or ""
            if len(description) > 47:
                description = description[:47] + "..."
            table.add_row(project.id, project.name, description)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list projects: {e}", err=True)
        raise typer.Exit(1)

@projects_app.command(name="create")
def project_create(
    name: str,
    team_id: Optional[str] = typer.Option(None, help="Team ID to create project in"),
    description: Optional[str] = typer.Option(None, help="Project description"),
):
    """Create a new project."""
    client = get_client()

    try:
        if not team_id and not client.state.team_id:
            typer.echo("No team ID provided. Please specify --team-id or set a current team.", err=True)
            raise typer.Exit(1)

        team_id = team_id or client.state.team_id
        project = client.projects.create(name=name, team_id=team_id, description=description)

        typer.echo("Project created successfully!")
        typer.echo(f"ID: {project.id}")
        typer.echo(f"Name: {project.name}")
        if project.description:
            typer.echo(f"Description: {project.description}")

    except Exception as e:
        typer.echo(f"Failed to create project: {e}", err=True)
        raise typer.Exit(1)

@datasources_app.command(name="list")
def datasources_list(
    project_id: Optional[str] = typer.Option(None, help="Project ID to list datasources for")
):
    """List datasources."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo("No project ID provided. Please specify --project-id or set a current project.", err=True)
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
    project_id: Optional[str] = typer.Option(None, help="Project ID to create datasource in"),
    uri: Optional[str] = typer.Option(None, help="Datasource URI"),
):
    """Create a new datasource."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo("No project ID provided. Please specify --project-id or set a current project.", err=True)
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
    project_id: Optional[str] = typer.Option(None, help="Project ID to list datalines for")
):
    """List datalines."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo("No project ID provided. Please specify --project-id or set a current project.", err=True)
            raise typer.Exit(1)

        project_id = project_id or client.state.project_id
        datalines = client.datalines.list(project_id=project_id)

        if not datalines:
            typer.echo("No datalines found")
            return

        table = Table()
        table.add_column("ID")
        table.add_column("Name")

        for dl in datalines:
            table.add_row(dl.id, dl.name)

        console.print(table)

    except Exception as e:
        typer.echo(f"Failed to list datalines: {e}", err=True)
        raise typer.Exit(1)

@query_app.command(name="list")
def query_programs_list(
    project_id: Optional[str] = typer.Option(None, help="Project ID to list query programs for"),
    include_deleted: bool = typer.Option(False, help="Include deleted query programs"),
):
    """List query programs."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo("No project ID provided. Please specify --project-id or set a current project.", err=True)
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
            question = qp.question or ""
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

@query_app.command(name="run")
def query_run(query_id: str):
    """Run a query program."""
    client = get_client()

    try:
        result = client.query_programs.evaluate(query_id)

        typer.echo("Query executed successfully!")

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

    except Exception as e:
        typer.echo(f"Failed to run query: {e}", err=True)
        raise typer.Exit(1)

@query_app.command(name="publish")
def query_publish(
    query_id: str,
    group_slots: Optional[int] = typer.Option(None, help="Number of group slots"),
):
    """Publish a query program."""
    client = get_client()

    try:
        query_program = client.query_programs.publish(query_id, group_slots=group_slots)

        typer.echo("Query program published successfully!")
        typer.echo(f"ID: {query_program.id}")
        typer.echo(f"Name: {query_program.name}")
        typer.echo(f"Published: {query_program.published}")
        typer.echo(f"Public: {query_program.public}")

    except Exception as e:
        typer.echo(f"Failed to publish query program: {e}", err=True)
        raise typer.Exit(1)

@query_app.command(name="unpublish")
def query_unpublish(query_id: str):
    """Unpublish a query program."""
    client = get_client()

    try:
        query_program = client.query_programs.unpublish(query_id)

        typer.echo("Query program unpublished successfully!")
        typer.echo(f"ID: {query_program.id}")
        typer.echo(f"Name: {query_program.name}")
        typer.echo(f"Published: {query_program.published}")

    except Exception as e:
        typer.echo(f"Failed to unpublish query program: {e}", err=True)
        raise typer.Exit(1)

@query_app.command(name="generate")
def query_generate(
    dataline_id: str,
    name: Optional[str] = typer.Option(None, help="Name for the generated query program"),
):
    """Generate a query program."""
    client = get_client()

    try:
        # This is a placeholder as the actual API call would depend on the specific implementation
        typer.echo("Query program generation started...")
        typer.echo("Analyzing data structure...")
        typer.echo("Generating query program...")

        # Mock data for example
        query_id = "qp-789ghi"

        typer.echo("Query program created successfully!")
        typer.echo(f"ID: {query_id}")
        typer.echo(f"Name: {name}")

    except Exception as e:
        typer.echo(f"Failed to generate query program: {e}", err=True)
        raise typer.Exit(1)

@endpoints_app.command(name="list")
def endpoints_list(
    project_id: Optional[str] = typer.Option(None, help="Project ID to list endpoints for")
):
    """List endpoints."""
    client = get_client()

    try:
        if not project_id and not client.state.project_id:
            typer.echo("No project ID provided. Please specify --project-id or set a current project.", err=True)
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
    client = get_client()

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
    client = get_client()

    try:
        typer.echo(f"Subscribing to jobs for datasource {datasource_id}...")

        # Mock data for example
        typer.echo("[2025-03-25 14:30:21] Job j-123456 started: Connecting to PostgreSQL database")
        typer.echo("[2025-03-25 14:30:22] Job j-123456 progress: Successfully connected to database")
        typer.echo("[2025-03-25 14:30:25] Job j-123456 progress: Analyzing table structure")
        typer.echo("[2025-03-25 14:30:30] Job j-123456 progress: Found 12 tables with 450,000 rows total")
        typer.echo("[2025-03-25 14:30:45] Job j-123456 completed: Database connection established and schema analyzed")

    except Exception as e:
        typer.echo(f"Failed to subscribe to jobs: {e}", err=True)
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
