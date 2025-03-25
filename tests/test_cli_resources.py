import json
import os
import shutil
import unittest
import uuid
from pathlib import Path

from typer.testing import CliRunner

from infactory_client.cli import app


class TestCLIResources(unittest.TestCase):
    """Test CLI resource management commands (organizations, teams, projects)"""

    def setUp(self):
        """Set up test environment"""
        # Create CLI runner
        self.runner = CliRunner()

        # Store original NF_HOME if it exists
        self.original_nf_home = os.environ.get("NF_HOME")
        # Create a temporary NF_HOME for testing
        self.test_nf_home = Path("/tmp/test_infactory_home")
        self.test_nf_home.mkdir(parents=True, exist_ok=True)
        os.environ["NF_HOME"] = str(self.test_nf_home)

        # Store original NF_API_KEY if it exists
        self.original_api_key = os.environ.get("NF_API_KEY")
        if self.original_api_key:
            del os.environ["NF_API_KEY"]

        # Copy test api key to NF_API_KEY if it exists
        if "NF_TEST_API_KEY" in os.environ:
            os.environ["NF_API_KEY"] = os.environ["NF_TEST_API_KEY"]

        # Login before running tests
        result = self.runner.invoke(app, ["login"])
        self.assertEqual(result.exit_code, 0)

    def tearDown(self):
        """Clean up test environment"""
        # Logout after tests
        self.runner.invoke(app, ["logout"])

        # Remove test NF_HOME
        if self.test_nf_home.exists():
            shutil.rmtree(self.test_nf_home)

        # Restore original NF_HOME
        if self.original_nf_home:
            os.environ["NF_HOME"] = self.original_nf_home
        elif "NF_HOME" in os.environ:
            del os.environ["NF_HOME"]

        # Restore original API key
        if self.original_api_key:
            os.environ["NF_API_KEY"] = self.original_api_key
        elif "NF_API_KEY" in os.environ:
            del os.environ["NF_API_KEY"]

    def test_organizations_list(self):
        """Test organization listing"""
        # Test JSON output
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)
        self.assertIsInstance(orgs_data, list)
        if orgs_data:  # If there are organizations
            self.assertIn("id", orgs_data[0])
            self.assertIn("name", orgs_data[0])
            self.assertIn("is_current", orgs_data[0])

        # Test table output
        result = self.runner.invoke(app, ["orgs", "list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)
        self.assertIn("Current", result.stdout)

    def test_organizations_select(self):
        """Test organization selection"""
        # First list organizations to get one
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if orgs_data:  # If there are organizations
            # Test direct selection using set-organization
            org_id = orgs_data[0]["id"]
            result = self.runner.invoke(app, ["orgs", "set", org_id])
            self.assertEqual(result.exit_code, 0)
            self.assertIn("Current organization set to", result.stdout)

            # Verify selection in show command
            result = self.runner.invoke(app, ["show", "--json"])
            self.assertEqual(result.exit_code, 0)
            show_data = json.loads(result.stdout)
            self.assertEqual(show_data["organization"]["id"], org_id)

    def test_teams_list(self):
        """Test team listing"""
        # First select an organization
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Test JSON output
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)
        self.assertIsInstance(teams_data, list)
        if teams_data:  # If there are teams
            self.assertIn("id", teams_data[0])
            self.assertIn("name", teams_data[0])
            self.assertIn("is_current", teams_data[0])

        # Test table output
        result = self.runner.invoke(app, ["teams", "list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)
        self.assertIn("Current", result.stdout)

    def test_teams_select(self):
        """Test team selection"""
        # First select an organization
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # List teams to get one
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        # Test direct selection using set-team
        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Current team set to", result.stdout)

        # Verify selection in show command
        result = self.runner.invoke(app, ["show", "--json"])
        self.assertEqual(result.exit_code, 0)
        show_data = json.loads(result.stdout)
        self.assertEqual(show_data["team"]["id"], team_id)

    def test_projects_list(self):
        """Test project listing"""
        # First select an organization and team
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Test JSON output
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)
        self.assertIsInstance(projects_data, list)
        if projects_data:  # If there are projects
            self.assertIn("id", projects_data[0])
            self.assertIn("name", projects_data[0])
            self.assertIn("description", projects_data[0])
            self.assertIn("is_current", projects_data[0])

        # Test table output
        result = self.runner.invoke(app, ["projects", "list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)
        self.assertIn("Description", result.stdout)
        self.assertIn("Current", result.stdout)

    def test_projects_select(self):
        """Test project selection"""
        # First select an organization and team
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # List projects to get one
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        # Test direct selection using set-project
        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Current project set to", result.stdout)

        # Verify selection in show command
        result = self.runner.invoke(app, ["show", "--json"])
        self.assertEqual(result.exit_code, 0)
        show_data = json.loads(result.stdout)
        self.assertEqual(show_data["project"]["id"], project_id)

    def test_datasources_list(self):
        """Test datasource listing"""
        # First select an organization and team
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set project
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)

        # Test datasources list without project ID (using current project)
        result = self.runner.invoke(app, ["datasources", "list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)
        self.assertIn("Type", result.stdout)
        self.assertIn("URI", result.stdout)

        # Test datasources list with explicit project ID
        result = self.runner.invoke(
            app, ["datasources", "list", "--project-id", project_id]
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)
        self.assertIn("Type", result.stdout)
        self.assertIn("URI", result.stdout)

    def test_datasource_create(self):
        """Test datasource creation"""
        # First select an organization and team
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set project
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)

        # Test datasource creation without project ID (using current project)
        datasource_name = "test-ds-" + str(uuid.uuid4())[:8]
        result = self.runner.invoke(
            app,
            [
                "datasources",
                "create",
                datasource_name,
                "--type",
                "postgres",
                "--uri",
                "postgresql://user:pass@localhost:5432/db",
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Datasource created successfully!", result.stdout)
        self.assertIn("ID:", result.stdout)
        self.assertIn("Name: " + datasource_name, result.stdout)
        self.assertIn("Type: postgres", result.stdout)
        self.assertIn("URI:", result.stdout)

        # Test datasource creation with explicit project ID
        datasource_name2 = "test-ds-" + str(uuid.uuid4())[:8]
        result = self.runner.invoke(
            app,
            [
                "datasources",
                "create",
                datasource_name2,
                "--type",
                "mysql",
                "--uri",
                "mysql://user:pass@localhost:3306/db",
                "--project-id",
                project_id,
            ],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Datasource created successfully!", result.stdout)
        self.assertIn("ID:", result.stdout)
        self.assertIn("Name: " + datasource_name2, result.stdout)
        self.assertIn("Type: mysql", result.stdout)
        self.assertIn("URI:", result.stdout)

    def test_datalines_list(self):
        """Test dataline listing"""
        # First select an organization, team, and project
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set project
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)

        # Test datalines list without project ID (using current project)
        result = self.runner.invoke(app, ["datalines", "list"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)

        # Test datalines list with explicit project ID
        result = self.runner.invoke(
            app, ["datalines", "list", "--project-id", project_id]
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ID", result.stdout)
        self.assertIn("Name", result.stdout)

        # Test JSON output
        result = self.runner.invoke(app, ["datalines", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        if "No datalines found" not in result.stdout:
            datalines_data = json.loads(result.stdout)
            self.assertIsInstance(datalines_data, list)
            if datalines_data:  # If there are datalines
                self.assertIn("id", datalines_data[0])
                self.assertIn("name", datalines_data[0])

        # Test JSON output with explicit project ID
        result = self.runner.invoke(
            app, ["datalines", "list", "--json", "--project-id", project_id]
        )
        self.assertEqual(result.exit_code, 0)
        if "No datalines found" not in result.stdout:
            datalines_data = json.loads(result.stdout)
            self.assertIsInstance(datalines_data, list)
            if datalines_data:  # If there are datalines
                self.assertIn("id", datalines_data[0])
                self.assertIn("name", datalines_data[0])

    def test_datalines_get(self):
        """Test getting a dataline by ID"""
        # First select an organization, team, and project
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set project
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)

        # First get a list of datalines
        result = self.runner.invoke(app, ["datalines", "list", "--json"])
        self.assertEqual(result.exit_code, 0)

        datalines = json.loads(result.stdout)

        # If we have datalines, test get command
        if len(datalines) > 0:
            # Get the first dataline ID from the output
            dataline_id = datalines[0]["id"]

            # Test basic get
            result = self.runner.invoke(app, ["datalines", "get", dataline_id])
            self.assertEqual(result.exit_code, 0)
            self.assertIn(dataline_id, result.stdout)

            # Test get with --model flag
            result = self.runner.invoke(
                app, ["datalines", "get", dataline_id, "--model"]
            )
            self.assertEqual(result.exit_code, 0)
            # Note: We can't guarantee valid JSON output as it depends on the data

            # Test get with --code flag
            result = self.runner.invoke(
                app, ["datalines", "get", dataline_id, "--code"]
            )
            self.assertEqual(result.exit_code, 0)
            # Note: We can't guarantee schema code exists

            # Test error case: model and code flags together
            result = self.runner.invoke(
                app, ["datalines", "get", dataline_id, "--model", "--code"]
            )
            self.assertEqual(result.exit_code, 1)
            self.assertIn(
                "Error: --model and --code cannot be used together", result.stdout
            )

            # Test error case: invalid ID
            result = self.runner.invoke(app, ["datalines", "get", "invalid-id"])
            self.assertNotEqual(result.exit_code, 0)
        else:
            self.skipTest("No datalines available for testing")

    def test_datalines_select(self):
        """Test interactive dataline selection"""
        # First select an organization, team, and project
        result = self.runner.invoke(app, ["orgs", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        orgs_data = json.loads(result.stdout)

        if not orgs_data:
            self.skipTest("No organizations available for testing")

        # Set organization
        org_id = orgs_data[0]["id"]
        result = self.runner.invoke(app, ["orgs", "set", org_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set team
        result = self.runner.invoke(app, ["teams", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        teams_data = json.loads(result.stdout)

        if not teams_data:
            self.skipTest("No teams available for testing")

        team_id = teams_data[0]["id"]
        result = self.runner.invoke(app, ["teams", "set", team_id])
        self.assertEqual(result.exit_code, 0)

        # Get and set project
        result = self.runner.invoke(app, ["projects", "list", "--json"])
        self.assertEqual(result.exit_code, 0)
        projects_data = json.loads(result.stdout)

        if not projects_data:
            self.skipTest("No projects available for testing")

        project_id = projects_data[0]["id"]
        result = self.runner.invoke(app, ["projects", "set", project_id])
        self.assertEqual(result.exit_code, 0)

        # Test error case: model and code flags together
        result = self.runner.invoke(app, ["datalines", "select", "--model", "--code"])
        self.assertEqual(result.exit_code, 1)
        self.assertIn(
            "Error: --model and --code cannot be used together", result.stdout
        )

        # Test basic select command (will show prompt but not proceed due to no input)
        result = self.runner.invoke(app, ["datalines", "select"])
        if "No datalines found" in result.stdout:
            self.skipTest("No datalines available for testing")
        self.assertIn("Select dataline number", result.stdout)


if __name__ == "__main__":
    unittest.main()
