import os
import json
import shutil
import unittest
import subprocess
from pathlib import Path

class TestCLIAuth(unittest.TestCase):
    """Test CLI authentication commands"""

    def setUp(self):
        """Set up test environment"""
        # Store original NF_HOME if it exists
        self.original_nf_home = os.environ.get('NF_HOME')
        # Create a temporary NF_HOME for testing
        self.test_nf_home = Path('/tmp/test_infactory_home')
        self.test_nf_home.mkdir(parents=True, exist_ok=True)
        os.environ['NF_HOME'] = str(self.test_nf_home)
        
        # Store original NF_API_KEY if it exists
        self.original_api_key = os.environ.get('NF_API_KEY')
        if self.original_api_key:
            del os.environ['NF_API_KEY']

        # Copy test api key to NF_API_KEY
        os.environ['NF_API_KEY'] = os.environ['NF_TEST_API_KEY']

    def tearDown(self):
        """Clean up test environment"""
        # Remove test NF_HOME
        if self.test_nf_home.exists():
            shutil.rmtree(self.test_nf_home)
        
        # Restore original NF_HOME
        if self.original_nf_home:
            os.environ['NF_HOME'] = self.original_nf_home
        elif 'NF_HOME' in os.environ:
            del os.environ['NF_HOME']
            
        # Restore original API key
        if self.original_api_key:
            os.environ['NF_API_KEY'] = self.original_api_key
        elif 'NF_API_KEY' in os.environ:
            del os.environ['NF_API_KEY']

    def run_cli_command(self, command):
        """Helper method to run CLI commands"""
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True
        )
        return result

    def test_auth_flow(self):
        """Test the complete authentication flow"""
        # Test initial logout (should be graceful when already logged out)
        result = self.run_cli_command('nf logout')
        self.assertEqual(result.returncode, 0)
        self.assertIn('Logout successful', result.stdout)

        # Verify NF_HOME is empty
        api_key_file = self.test_nf_home / 'api_key'
        state_file = self.test_nf_home / 'state.json'
        self.assertFalse(api_key_file.exists())
        self.assertFalse(state_file.exists())

        # Test show command when logged out
        result = self.run_cli_command('nf show')
        self.assertEqual(result.returncode, 0)
        self.assertNotIn('user_id', result.stdout)

        # Test login
        result = self.run_cli_command('nf login')
        self.assertEqual(result.returncode, 0)
        self.assertIn('API key saved successfully', result.stdout)

        # Verify NF_HOME is populated
        api_key_file = self.test_nf_home / 'api_key'
        state_file = self.test_nf_home / 'state.json'
        self.assertTrue(api_key_file.exists())
        self.assertTrue(state_file.exists())


        # Test show command after login
        result = self.run_cli_command('nf show --json')
        self.assertEqual(result.returncode, 0)
        result = json.loads(result.stdout)
        self.assertIsNotNone(result['user']['id'])

        # Test logout
        result = self.run_cli_command('nf logout')
        self.assertEqual(result.returncode, 0)
        self.assertIn('Logout successful', result.stdout)

        # Verify NF_HOME is cleared
        api_key_file = self.test_nf_home / 'api_key'
        state_file = self.test_nf_home / 'state.json'
        self.assertFalse(api_key_file.exists())
        self.assertFalse(state_file.exists())

        # Test show command after logout
        result = self.run_cli_command('nf show')
        self.assertEqual(result.returncode, 0)
        self.assertNotIn('user_id', result.stdout)

if __name__ == '__main__':
    unittest.main() 