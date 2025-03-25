import os
import json
from pathlib import Path
from unittest import mock

import pytest
from typer.testing import CliRunner

from infactory_client.cli import app
from infactory_client.client import InfactoryClient

runner = CliRunner()

def test_show_does_not_create_state():
    """Test that 'nf show' doesn't create state files after logout."""
    # Get the config directory path
    client = InfactoryClient()
    config_dir = client._get_config_dir()
    state_file = config_dir / "state.json"
    api_key_file = config_dir / "api_key"

    # Store original environment variable value
    original_api_key = os.environ.get("NF_API_KEY")

    try:
        # Clear the environment variable
        if "NF_API_KEY" in os.environ:
            del os.environ["NF_API_KEY"]

        # First ensure we're logged out
        result = runner.invoke(app, ["logout"])
        assert result.exit_code == 0
        print("\nLogout result:", result.stdout)
        
        # Verify files don't exist after logout
        assert not state_file.exists(), "State file should not exist after logout"
        assert not api_key_file.exists(), "API key file should not exist after logout"
        
        # Run show command
        result = runner.invoke(app, ["show"])
        print("\nShow command result:", result.stdout)
        print("Show command exit code:", result.exit_code)
        
        # Should fail with config error about no API key
        assert result.exit_code == 1
        assert "Configuration error: No API key found" in result.stdout
        
        # Verify files still don't exist
        assert not state_file.exists(), "State file should not be created by show command"
        assert not api_key_file.exists(), "API key file should not be created by show command"

    finally:
        # Cleanup - ensure files are removed even if test fails
        if state_file.exists():
            state_file.unlink()
        if api_key_file.exists():
            api_key_file.unlink()
        
        # Restore original environment variable if it existed
        if original_api_key is not None:
            os.environ["NF_API_KEY"] = original_api_key
        elif "NF_API_KEY" in os.environ:
            del os.environ["NF_API_KEY"] 