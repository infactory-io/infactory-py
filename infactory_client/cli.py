#!/usr/bin/env python3
import os
import sys
import json
import getpass
import logging
import argparse
import textwrap
from pathlib import Path
from typing import List, Dict, Optional, Any
from dotenv import load_dotenv

from infactory_client.client import ClientState, InfactoryClient
from infactory_client.errors import APIError, AuthenticationError, ConfigError

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("infactory-cli")


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
    # Try to get API key from environment variable first
    api_key = os.getenv("NF_API_KEY")

    # If not in environment, try to load from file
    if not api_key:
        api_key = load_api_key()

    if not api_key:
        raise ConfigError(
            "No API key found. Please login with 'nf login' or set NF_API_KEY environment variable."
        )

    # Initialize client with API key
    client = InfactoryClient(api_key=api_key)

    # Connect to validate API key
    try:
        client.connect()
        return client
    except AuthenticationError:
        raise ConfigError("Invalid API key. Please login again with 'nf login'.")


def handle_login(args):
    """Handle login command."""
    api_key = os.getenv("NF_API_KEY")
    if not api_key:
        api_key = getpass.getpass("Enter your API key: ")
    else:
        logger.info(
            "Using API key from environment variable starting with %s...", api_key[:7]
        )

    if not api_key:
        logger.error("API key cannot be empty")
        return

    # Test the API key
    client = InfactoryClient(api_key=api_key)
    try:
        client.connect()

        # Save API key
        save_api_key(api_key)

        # Save state
        save_state(client.state)

        logger.info("API key saved successfully!")

    except AuthenticationError:
        logger.error("Invalid API key. Please check and try again.")
    except Exception as e:
        logger.error(f"Failed to login: {e}")


def handle_show_state(args):
    """Handle show-state command to display current client state."""
    try:
        # Try to get client with current API key
        client = get_client()

        # Get the API key (either from env or from saved file)
        api_key = os.getenv("NF_API_KEY")
        if not api_key:
            api_key = load_api_key()

        # Format API key for display (show only first and last few characters)
        masked_api_key = (
            f"{api_key[:7]}...{api_key[-4:]}"
            if api_key and len(api_key) > 11
            else "Not set"
        )

        # Display current state
        logger.info("Current State:")
        logger.info(f"API Key: {masked_api_key}")

        # Show organization info if set
        if client.state.organization_id:
            try:
                org = client.organizations.get(client.state.organization_id)
                logger.info(
                    f"Organization: {org.name} (ID: {client.state.organization_id})"
                )
            except Exception:
                logger.info(f"Organization ID: {client.state.organization_id}")
        else:
            logger.info("Organization: Not set")

        # Show team info if set
        if client.state.team_id:
            try:
                team = client.teams.get(client.state.team_id)
                logger.info(f"Team: {team.name} (ID: {client.state.team_id})")
            except Exception:
                logger.info(f"Team ID: {client.state.team_id}")
        else:
            logger.info("Team: Not set")

        # Show project info if set
        if client.state.project_id:
            try:
                project = client.projects.get(client.state.project_id)
                logger.info(f"Project: {project.name} (ID: {client.state.project_id})")
            except Exception:
                logger.info(f"Project ID: {client.state.project_id}")
        else:
            logger.info("Project: Not set")

    except ConfigError as e:
        logger.error(f"Configuration error: {e}")
    except Exception as e:
        logger.error(f"Failed to show state: {e}")


def handle_set_project(args):
    """Handle set-project command."""
    client = get_client()

    try:
        # Validate that project exists
        project = client.projects.get(args.project_id)

        # Update state
        client.set_current_project(project.id)

        logger.info(f"Current project set to {project.name} (ID: {project.id})")

    except Exception as e:
        logger.error(f"Failed to set project: {e}")


def handle_set_organization(args):
    """Handle set-organization command."""
    client = get_client()

    try:
        # Validate that organization exists
        org = client.organizations.get(args.organization_id)

        # Update state
        client.set_current_organization(org.id)

        logger.info(f"Current organization set to {org.name} (ID: {org.id})")

    except Exception as e:
        logger.error(f"Failed to set organization: {e}")


def handle_set_team(args):
    """Handle set-team command."""
    client = get_client()

    try:
        # Validate that team exists
        team = client.teams.get(args.team_id)

        # Update state
        client.set_current_team(team.id)

        logger.info(f"Current team set to {team.name} (ID: {team.id})")

    except Exception as e:
        logger.error(f"Failed to set team: {e}")


def handle_projects_list(args):
    """Handle projects list command."""
    client = get_client()

    try:
        if args.team_id:
            projects = client.projects.list(team_id=args.team_id)
        else:
            # Try to use current team ID from state
            if client.state.team_id:
                projects = client.projects.list(team_id=client.state.team_id)
            else:
                logger.error(
                    "No team ID provided. Please specify --team-id or set a current team."
                )
                return

        if not projects:
            logger.info("No projects found")
            return

        # Print projects table
        print(f"{'ID':<36} | {'Name':<30} | {'Description':<50}")
        print("-" * 120)

        for project in projects:
            description = project.description or ""
            if len(description) > 47:
                description = description[:47] + "..."

            print(f"{project.id:<36} | {project.name:<30} | {description:<50}")

    except Exception as e:
        logger.error(f"Failed to list projects: {e}")


def handle_project_create(args):
    """Handle project create command."""
    client = get_client()

    try:
        if not args.team_id and not client.state.team_id:
            logger.error(
                "No team ID provided. Please specify --team-id or set a current team."
            )
            return

        team_id = args.team_id or client.state.team_id

        project = client.projects.create(
            name=args.name, team_id=team_id, description=args.description
        )

        logger.info(f"Project created successfully!")
        logger.info(f"ID: {project.id}")
        logger.info(f"Name: {project.name}")
        if project.description:
            logger.info(f"Description: {project.description}")

    except Exception as e:
        logger.error(f"Failed to create project: {e}")


def handle_datasource_create(args):
    """Handle datasource create command."""
    client = get_client()

    try:
        if not args.project_id and not client.state.project_id:
            logger.error(
                "No project ID provided. Please specify --project-id or set a current project."
            )
            return

        project_id = args.project_id or client.state.project_id

        datasource = client.datasources.create(
            name=args.name, project_id=project_id, type=args.type, uri=args.uri
        )

        logger.info(f"Datasource created successfully!")
        logger.info(f"ID: {datasource.id}")
        logger.info(f"Name: {datasource.name}")
        logger.info(f"Type: {datasource.type}")
        if datasource.uri:
            logger.info(f"URI: {datasource.uri}")

    except Exception as e:
        logger.error(f"Failed to create datasource: {e}")


def handle_datasources_list(args):
    """Handle datasources list command."""
    client = get_client()

    try:
        if not args.project_id and not client.state.project_id:
            logger.error(
                "No project ID provided. Please specify --project-id or set a current project."
            )
            return

        project_id = args.project_id or client.state.project_id

        datasources = client.datasources.list(project_id=project_id)

        if not datasources:
            logger.info("No datasources found")
            return

        # Print datasources table
        print(f"{'ID':<36} | {'Name':<30} | {'Type':<15} | {'URI':<50}")
        print("-" * 135)

        for ds in datasources:
            uri = ds.uri or ""
            if len(uri) > 47:
                uri = uri[:47] + "..."

            print(f"{ds.id:<36} | {ds.name:<30} | {ds.type or '':<15} | {uri:<50}")

    except Exception as e:
        logger.error(f"Failed to list datasources: {e}")


def handle_datalines_list(args):
    """Handle datalines list command."""
    client = get_client()

    try:
        if not args.project_id and not client.state.project_id:
            logger.error(
                "No project ID provided. Please specify --project-id or set a current project."
            )
            return

        project_id = args.project_id or client.state.project_id

        datalines = client.datalines.list(project_id=project_id)

        if not datalines:
            logger.info("No datalines found")
            return

        # Print datalines table
        print(f"{'ID':<36} | {'Name':<50}")
        print("-" * 90)

        for dl in datalines:
            print(f"{dl.id:<36} | {dl.name:<50}")

    except Exception as e:
        logger.error(f"Failed to list datalines: {e}")


def handle_query_programs_list(args):
    """Handle query programs list command."""
    client = get_client()

    try:
        if not args.project_id and not client.state.project_id:
            logger.error(
                "No project ID provided. Please specify --project-id or set a current project."
            )
            return

        project_id = args.project_id or client.state.project_id

        query_programs = client.query_programs.list(
            project_id=project_id, include_deleted=args.include_deleted
        )

        if not query_programs:
            logger.info("No query programs found")
            return

        # Print query programs table
        print(
            f"{'ID':<36} | {'Name':<30} | {'Published':<9} | {'Public':<6} | {'Question':<50}"
        )
        print("-" * 140)

        for qp in query_programs:
            question = qp.question or ""
            if len(question) > 47:
                question = question[:47] + "..."

            published = "Yes" if qp.published else "No"
            public = "Yes" if qp.public else "No"

            print(
                f"{qp.id:<36} | {qp.name or '':<30} | {published:<9} | {public:<6} | {question:<50}"
            )

    except Exception as e:
        logger.error(f"Failed to list query programs: {e}")


def handle_query_run(args):
    """Handle query run command."""
    client = get_client()

    try:
        result = client.query_programs.evaluate(args.query_id)

        logger.info(f"Query executed successfully!")

        # Try to format the result nicely
        if isinstance(result, dict) and "data" in result:
            data = result["data"]
            if isinstance(data, list) and data:
                # Create table headers
                headers = list(data[0].keys())
                col_widths = [
                    max(len(str(row.get(h, ""))) for row in data) for h in headers
                ]
                col_widths = [max(len(h), w) + 2 for h, w in zip(headers, col_widths)]

                # Print table header
                header_line = (
                    "| "
                    + " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
                    + " |"
                )
                print(header_line)
                print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

                # Print rows
                for row in data:
                    row_line = (
                        "| "
                        + " | ".join(
                            str(row.get(h, "")).ljust(w)
                            for h, w in zip(headers, col_widths)
                        )
                        + " |"
                    )
                    print(row_line)
            else:
                print(json.dumps(data, indent=2))
        else:
            print(json.dumps(result, indent=2))

    except Exception as e:
        logger.error(f"Failed to run query: {e}")


def handle_query_publish(args):
    """Handle query publish command."""
    client = get_client()

    try:
        query_program = client.query_programs.publish(
            args.query_id, group_slots=args.group_slots
        )

        logger.info(f"Query program published successfully!")
        logger.info(f"ID: {query_program.id}")
        logger.info(f"Name: {query_program.name}")
        logger.info(f"Published: {query_program.published}")
        logger.info(f"Public: {query_program.public}")

    except Exception as e:
        logger.error(f"Failed to publish query program: {e}")


def handle_query_unpublish(args):
    """Handle query unpublish command."""
    client = get_client()

    try:
        query_program = client.query_programs.unpublish(args.query_id)

        logger.info(f"Query program unpublished successfully!")
        logger.info(f"ID: {query_program.id}")
        logger.info(f"Name: {query_program.name}")
        logger.info(f"Published: {query_program.published}")

    except Exception as e:
        logger.error(f"Failed to unpublish query program: {e}")


def handle_endpoints_list(args):
    """Handle endpoints list command."""
    client = get_client()

    try:
        if not args.project_id and not client.state.project_id:
            logger.error(
                "No project ID provided. Please specify --project-id or set a current project."
            )
            return

        project_id = args.project_id or client.state.project_id

        # This is a placeholder as the actual API call would depend on the specific implementation
        # In a real implementation, you would call something like:
        # endpoints = client.endpoints.list(project_id=project_id)

        # Mock data for example:
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
            {
                "id": "ep-789ghi",
                "name": "Customer Stats",
                "url": "/v1/live/customer-stats/v1/data",
                "method": "GET",
            },
        ]

        if not endpoints:
            logger.info("No endpoints found")
            return

        # Print endpoints table
        print(f"{'Endpoint ID':<13} | {'Name':<17} | {'URL':<34} | {'Method':<8}")
        print("-" * 80)

        for ep in endpoints:
            print(
                f"{ep['id']:<13} | {ep['name']:<17} | {ep['url']:<34} | {ep['method']:<8}"
            )

    except Exception as e:
        logger.error(f"Failed to list endpoints: {e}")


def handle_endpoints_curl(args):
    """Handle endpoints curl-example command."""
    client = get_client()

    try:
        # This is a placeholder as the actual API call would depend on the specific implementation
        # In a real implementation, you would call something like:
        # endpoint = client.endpoints.get(args.endpoint_id)

        # Mock data for example:
        endpoint = {
            "id": "ep-123abc",
            "name": "Monthly Sales",
            "url": "/v1/live/monthly-sales/v1/data",
            "method": "GET",
        }

        base_url = "https://i7y.dev"
        full_url = f"{base_url}{endpoint['url']}"

        print(f"CURL example for endpoint {endpoint['id']}:\n")
        print(f'curl -X {endpoint["method"]} "{full_url}" \\')
        print('  -H "Authorization: Bearer YOUR_API_KEY" \\')
        print('  -H "Content-Type: application/json"')

    except Exception as e:
        logger.error(f"Failed to generate curl example: {e}")


def handle_jobs_subscribe(args):
    """Handle jobs subscribe command."""
    client = get_client()

    try:
        # This is a placeholder as the actual API call would depend on the specific implementation
        # In a real implementation, you would call something like:
        # client.jobs.subscribe(datasource_id=args.datasource_id)

        logger.info(f"Subscribing to jobs for datasource {args.datasource_id}...")

        # Mock data for example:
        print(
            "[2025-03-25 14:30:21] Job j-123456 started: Connecting to PostgreSQL database"
        )
        print(
            "[2025-03-25 14:30:22] Job j-123456 progress: Successfully connected to database"
        )
        print("[2025-03-25 14:30:25] Job j-123456 progress: Analyzing table structure")
        print(
            "[2025-03-25 14:30:30] Job j-123456 progress: Found 12 tables with 450,000 rows total"
        )
        print(
            "[2025-03-25 14:30:45] Job j-123456 completed: Database connection established and schema analyzed"
        )

        # In a real implementation, this would be a continuous stream of logs

    except Exception as e:
        logger.error(f"Failed to subscribe to jobs: {e}")


def handle_query_generate(args):
    """Handle query generate command."""
    client = get_client()

    try:
        # This is a placeholder as the actual API call would depend on the specific implementation
        # In a real implementation, you would call something like:
        # query_program = client.query_programs.generate(dataline_id=args.dataline_id, name=args.name)

        logger.info("Query program generation started...")
        logger.info("Analyzing data structure...")
        logger.info("Generating query program...")

        # Mock data for example:
        query_id = "qp-789ghi"
        name = args.name

        logger.info(f"Query program created successfully!")
        logger.info(f"ID: {query_id}")
        logger.info(f"Name: {name}")

    except Exception as e:
        logger.error(f"Failed to generate query program: {e}")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Infactory Command Line Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """
            Examples:
              nf login                                        # Login with API key
              nf projects list --team-id <team-id>            # List projects for a team
              nf datasource create --name "My DB" --type postgres  # Create a datasource
              nf query run <query-id>                         # Run a query program
              nf query publish <query-id>                     # Publish a query program
        """
        ),
    )

    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Login command
    login_parser = subparsers.add_parser("login", help="Login with API key")
    login_parser.set_defaults(func=handle_login)

    # Set current project command
    set_project_parser = subparsers.add_parser(
        "set-project", help="Set current project"
    )
    set_project_parser.add_argument("project_id", help="Project ID")
    set_project_parser.set_defaults(func=handle_set_project)

    # Set current organization command
    set_org_parser = subparsers.add_parser(
        "set-organization", help="Set current organization"
    )
    set_org_parser.add_argument("organization_id", help="Organization ID")
    set_org_parser.set_defaults(func=handle_set_organization)

    # Set current team command
    set_team_parser = subparsers.add_parser("set-team", help="Set current team")
    set_team_parser.add_argument("team_id", help="Team ID")
    set_team_parser.set_defaults(func=handle_set_team)

    # Projects commands
    projects_parser = subparsers.add_parser("projects", help="Manage projects")
    projects_subparsers = projects_parser.add_subparsers(
        dest="subcommand", help="Projects subcommands"
    )

    # Projects list command
    projects_list_parser = projects_subparsers.add_parser("list", help="List projects")
    projects_list_parser.add_argument("--team-id", help="Team ID to list projects for")
    projects_list_parser.set_defaults(func=handle_projects_list)

    # Projects create command
    projects_create_parser = projects_subparsers.add_parser(
        "create", help="Create a new project"
    )
    projects_create_parser.add_argument("name", help="Project name")
    projects_create_parser.add_argument(
        "--team-id", help="Team ID to create project in"
    )
    projects_create_parser.add_argument("--description", help="Project description")
    projects_create_parser.set_defaults(func=handle_project_create)

    # Datasources commands
    datasources_parser = subparsers.add_parser("datasources", help="Manage datasources")
    datasources_subparsers = datasources_parser.add_subparsers(
        dest="subcommand", help="Datasources subcommands"
    )

    # Datasources list command
    datasources_list_parser = datasources_subparsers.add_parser(
        "list", help="List datasources"
    )
    datasources_list_parser.add_argument(
        "--project-id", help="Project ID to list datasources for"
    )
    datasources_list_parser.set_defaults(func=handle_datasources_list)

    # Datasources create command
    datasources_create_parser = datasources_subparsers.add_parser(
        "create", help="Create a new datasource"
    )
    datasources_create_parser.add_argument("name", help="Datasource name")
    datasources_create_parser.add_argument(
        "--project-id", help="Project ID to create datasource in"
    )
    datasources_create_parser.add_argument(
        "--type", required=True, help="Datasource type (e.g. postgres, mysql)"
    )
    datasources_create_parser.add_argument("--uri", help="Datasource URI")
    datasources_create_parser.set_defaults(func=handle_datasource_create)

    # Datalines commands
    datalines_parser = subparsers.add_parser("datalines", help="Manage datalines")
    datalines_subparsers = datalines_parser.add_subparsers(
        dest="subcommand", help="Datalines subcommands"
    )

    # Datalines list command
    datalines_list_parser = datalines_subparsers.add_parser(
        "list", help="List datalines"
    )
    datalines_list_parser.add_argument(
        "--project-id", help="Project ID to list datalines for"
    )
    datalines_list_parser.set_defaults(func=handle_datalines_list)

    # Query programs commands
    query_parser = subparsers.add_parser("query", help="Manage query programs")
    query_subparsers = query_parser.add_subparsers(
        dest="subcommand", help="Query subcommands"
    )

    # Query programs list command
    query_list_parser = query_subparsers.add_parser("list", help="List query programs")
    query_list_parser.add_argument(
        "--project-id", help="Project ID to list query programs for"
    )
    query_list_parser.add_argument(
        "--include-deleted", action="store_true", help="Include deleted query programs"
    )
    query_list_parser.set_defaults(func=handle_query_programs_list)

    # Query run command
    query_run_parser = query_subparsers.add_parser("run", help="Run a query program")
    query_run_parser.add_argument("query_id", help="Query program ID to run")
    query_run_parser.set_defaults(func=handle_query_run)

    # Query publish command
    query_publish_parser = query_subparsers.add_parser(
        "publish", help="Publish a query program"
    )
    query_publish_parser.add_argument("query_id", help="Query program ID to publish")
    query_publish_parser.add_argument(
        "--group-slots", type=int, help="Number of group slots"
    )
    query_publish_parser.set_defaults(func=handle_query_publish)

    # Query unpublish command
    query_unpublish_parser = query_subparsers.add_parser(
        "unpublish", help="Unpublish a query program"
    )
    query_unpublish_parser.add_argument(
        "query_id", help="Query program ID to unpublish"
    )
    query_unpublish_parser.set_defaults(func=handle_query_unpublish)

    # Query generate command
    query_generate_parser = query_subparsers.add_parser(
        "generate", help="Generate a query program"
    )
    query_generate_parser.add_argument(
        "dataline_id", help="Dataline ID to generate query for"
    )
    query_generate_parser.add_argument(
        "--name", help="Name for the generated query program"
    )
    query_generate_parser.set_defaults(func=handle_query_generate)

    # Endpoints commands
    endpoints_parser = subparsers.add_parser("endpoints", help="Manage endpoints")
    endpoints_subparsers = endpoints_parser.add_subparsers(
        dest="subcommand", help="Endpoints subcommands"
    )

    # Endpoints list command
    endpoints_list_parser = endpoints_subparsers.add_parser(
        "list", help="List endpoints"
    )
    endpoints_list_parser.add_argument(
        "--project-id", help="Project ID to list endpoints for"
    )
    endpoints_list_parser.set_defaults(func=handle_endpoints_list)

    # Endpoints curl-example command
    endpoints_curl_parser = endpoints_subparsers.add_parser(
        "curl-example", help="Show curl example for endpoint"
    )
    endpoints_curl_parser.add_argument(
        "endpoint_id", help="Endpoint ID to show curl example for"
    )
    endpoints_curl_parser.set_defaults(func=handle_endpoints_curl)

    # Jobs commands
    jobs_parser = subparsers.add_parser("jobs", help="Manage jobs")
    jobs_subparsers = jobs_parser.add_subparsers(
        dest="subcommand", help="Jobs subcommands"
    )

    # Jobs subscribe command
    jobs_subscribe_parser = jobs_subparsers.add_parser(
        "subscribe", help="Subscribe to job updates"
    )
    jobs_subscribe_parser.add_argument(
        "datasource_id", help="Datasource ID to subscribe to"
    )
    jobs_subscribe_parser.set_defaults(func=handle_jobs_subscribe)

    # Parse arguments and call appropriate function
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        args.func(args)
    except ConfigError as e:
        logger.error(str(e))
        sys.exit(1)
    except AuthenticationError as e:
        logger.error(f"Authentication failed: {e}")
        sys.exit(1)
    except APIError as e:
        logger.error(f"API error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
