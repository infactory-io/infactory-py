import json
import os
import shutil
import unittest
from pathlib import Path

from typer.testing import CliRunner

from infactory_client.cli import app


class TestCLIAuth(unittest.TestCase):
    """Test CLI authentication commands"""

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

    def tearDown(self):
        """Clean up test environment"""
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

    def test_auth_flow(self):
        """Test the complete authentication flow"""
        # Test initial logout (should be graceful when already logged out)
        result = self.runner.invoke(app, ["logout"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Logout successful", result.stdout)

        # Verify NF_HOME is empty
        api_key_file = self.test_nf_home / "api_key"
        state_file = self.test_nf_home / "state.json"
        self.assertFalse(api_key_file.exists())
        self.assertFalse(state_file.exists())

        # Test login
        result = self.runner.invoke(app, ["login"])
        self.assertEqual(result.exit_code, 0)
        # self.assertIn('API key saved successfully', result.stdout)

        # Verify NF_HOME is populated
        api_key_file = self.test_nf_home / "api_key"
        state_file = self.test_nf_home / "state.json"
        self.assertTrue(api_key_file.exists())
        self.assertTrue(state_file.exists())

        # Test show command after login
        result = self.runner.invoke(app, ["show", "--json"])
        self.assertEqual(result.exit_code, 0)
        result_data = json.loads(result.stdout)
        self.assertIsNotNone(result_data["user"]["id"])

        # Test logout
        result = self.runner.invoke(app, ["logout"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Logout successful", result.stdout)

        # Verify NF_HOME is cleared
        api_key_file = self.test_nf_home / "api_key"
        state_file = self.test_nf_home / "state.json"
        self.assertFalse(api_key_file.exists())
        self.assertFalse(state_file.exists())


if __name__ == "__main__":
    unittest.main()
