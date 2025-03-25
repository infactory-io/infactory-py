import os
import json
import logging
import pathlib
import httpx
import tenacity
from typing import Dict, List, Optional, Union, Any
from pydantic import BaseModel

from infactory_client.errors import (
    APIError, AuthenticationError, AuthorizationError, 
    NotFoundError, ValidationError, RateLimitError, 
    ServerError, TimeoutError
)


class ClientState(BaseModel):
    """Represents the state of the client."""
    user_id: Optional[str] = None
    user_email: Optional[str] = None
    user_name: Optional[str] = None
    user_created_at: Optional[str] = None
    organization_id: Optional[str] = None
    team_id: Optional[str] = None
    project_id: Optional[str] = None
    api_key: Optional[str] = None
    base_url: Optional[str] = None


class InfactoryClient:
    """
    The main client for interacting with the Infactory API.
    
    Attributes:
        api_key (str): The API key for authentication
        base_url (str): The base URL for the API
        state (ClientState): The client state
    """
    
    def __init__(self, api_key: str = None, base_url: str = None):
        """
        Initialize the client with optional API key and base URL.
        
        Args:
            api_key: The API key for authentication (optional, will use NF_API_KEY env var if not provided)
            base_url: The base URL for the API (optional, will use NF_BASE_URL env var or default to https://api.infactory.ai/v1)
        """
        self.api_key = api_key or os.getenv("NF_API_KEY")
        self.base_url = base_url or os.getenv("NF_BASE_URL") or "https://api.infactory.ai"
        self.state = ClientState(
            api_key=self.api_key,
            base_url=self.base_url
        )
        self._http_client = None
        self._logger = logging.getLogger(__name__)
        self._config_dir = self._get_config_dir()
        
        # Load state from file if exists
        self._load_state()
        
        # Services will be initialized when needed
        self._services = {}

    def _get_config_dir(self) -> pathlib.Path:
        """Get the configuration directory path."""
        config_dir = os.getenv("NF_HOME") or os.path.expanduser("~/.infactory-client/")
        path = pathlib.Path(config_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _load_state(self):
        """Load client state from file."""
        state_file = self._config_dir / "state.json"
        if state_file.exists():
            try:
                with open(state_file, "r") as f:
                    state_data = json.load(f)
                    
                # Only update missing values in state
                for key, value in state_data.items():
                    if getattr(self.state, key) is None:
                        setattr(self.state, key, value)
                
                # If api_key is in the saved state but not provided in initialization, use it
                if self.api_key is None and self.state.api_key is not None:
                    self.api_key = self.state.api_key
                    
            except Exception as e:
                self._logger.warning(f"Failed to load state from {state_file}: {e}")

    def _save_state(self):
        """Save client state to file."""
        state_file = self._config_dir / "state.json"
        try:
            with open(state_file, "w") as f:
                json.dump(self.state.dict(exclude_none=True), f)
        except Exception as e:
            self._logger.warning(f"Failed to save state to {state_file}: {e}")

    @property
    def http_client(self):
        """Get or create the HTTP client."""
        if self._http_client is None:
            self._http_client = httpx.Client(
                base_url=self.base_url,
                timeout=30.0,
                follow_redirects=True
            )
        return self._http_client
    
    def _set_auth_header(self):
        """Set the authorization header for the HTTP client."""
        if self.api_key:
            self.http_client.headers["Authorization"] = f"Bearer {self.api_key}"
        else:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
    
    def _init_services(self):
        """Initialize service clients."""
        from infactory_client.services import (
            ProjectsService, DataSourcesService, DataLinesService,
            TeamsService, OrganizationsService, UsersService,
            QueryProgramsService, SecretsService
        )
        
        self._services = {
            "projects": ProjectsService(self),
            "datasources": DataSourcesService(self),
            "datalines": DataLinesService(self),
            "teams": TeamsService(self),
            "organizations": OrganizationsService(self),
            "users": UsersService(self),
            "query_programs": QueryProgramsService(self),
            "secrets": SecretsService(self),
        }

    def set_current_project(self, project_id: str):
        """
        Set the current project.
        
        Args:
            project_id: The project ID to set as current
        """
        self.state.project_id = project_id
        self._save_state()
    
    def set_current_organization(self, organization_id: str):
        """
        Set the current organization.
        
        Args:
            organization_id: The organization ID to set as current
        """
        self.state.organization_id = organization_id
        self._save_state()
        
    def set_current_team(self, team_id: str):
        """
        Set the current team.
        
        Args:
            team_id: The team ID to set as current
        """
        self.state.team_id = team_id
        self._save_state()
    
    def connect(self):
        """
        Initialize the connection to the Infactory API.
        
        Validates the API key and fetches the user ID.
        
        Returns:
            self: For method chaining
            
        Raises:
            AuthenticationError: If the API key is invalid
        """
        if not self.api_key:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
        
        # Test connection by getting current user
        try:
            user_info = self._get("v1/authentication/me")
            self._logger.debug(f"User info: {user_info}")
            is_clerk_user = user_info.get("clerk_user_id") or False
            self.state.user_id = user_info.get("id")
            self.state.user_email = user_info.get("email") or ("in CLERK" if is_clerk_user else "---")  
            self.state.user_name = user_info.get("name") or ("in CLERK" if is_clerk_user else "---")
            self.state.user_created_at = user_info.get("created_at")
            self._save_state()
        except Exception as e:
            raise AuthenticationError(f"Failed to connect with the provided API key: {e}")
        
        return self
    
    def disconnect(self):
        """Disconnect from the Infactory API."""
        if self._http_client:
            self._http_client.close()
            self._http_client = None
    
    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _get(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: The API endpoint to call
            params: Query parameters
            
        Returns:
            The JSON response
            
        Raises:
            AuthenticationError: If not authenticated
            RateLimitError: If rate limited
            ServerError: If server error
            TimeoutError: If request times out
            APIError: For other API errors
        """
        if not self.api_key:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
        
        self._set_auth_header()
        
        # Add API key to query params if provided
        params = params or {}
        if self.api_key:
            params["nf_api_key"] = self.api_key
        
        try:
            response = self.http_client.get(
                f"{self.base_url}/{endpoint.lstrip('/')}",
                params=params,
            )
            
            return self._handle_response(response)
                
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {str(e)}") from e
        except httpx.RequestError as e:
            raise APIError(f"Request failed: {str(e)}") from e
    
    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _post(self, endpoint: str, data: dict = None, params: dict = None) -> dict:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters
            
        Returns:
            The JSON response
            
        Raises:
            AuthenticationError: If not authenticated
            RateLimitError: If rate limited
            ServerError: If server error
            TimeoutError: If request times out
            APIError: For other API errors
        """
        if not self.api_key:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
        
        self._set_auth_header()
        
        # Add API key to query params if provided
        params = params or {}
        if self.api_key:
            params["nf_api_key"] = self.api_key
        
        try:
            response = self.http_client.post(
                f"{self.base_url}/{endpoint.lstrip('/')}",
                json=data,
                params=params,
            )
            
            return self._handle_response(response)
                
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {str(e)}") from e
        except httpx.RequestError as e:
            raise APIError(f"Request failed: {str(e)}") from e
    
    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _patch(self, endpoint: str, data: dict = None, params: dict = None) -> dict:
        """
        Make a PATCH request to the API.
        
        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters
            
        Returns:
            The JSON response
            
        Raises:
            AuthenticationError: If not authenticated
            RateLimitError: If rate limited
            ServerError: If server error
            TimeoutError: If request times out
            APIError: For other API errors
        """
        if not self.api_key:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
        
        self._set_auth_header()
        
        # Add API key to query params if provided
        params = params or {}
        if self.api_key:
            params["nf_api_key"] = self.api_key
        
        try:
            response = self.http_client.patch(
                f"{self.base_url}/{endpoint.lstrip('/')}",
                json=data,
                params=params,
            )
            
            return self._handle_response(response)
                
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {str(e)}") from e
        except httpx.RequestError as e:
            raise APIError(f"Request failed: {str(e)}") from e
    
    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _delete(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint: The API endpoint to call
            params: Query parameters
            
        Returns:
            The JSON response
            
        Raises:
            AuthenticationError: If not authenticated
            RateLimitError: If rate limited
            ServerError: If server error
            TimeoutError: If request times out
            APIError: For other API errors
        """
        if not self.api_key:
            raise AuthenticationError("No API key provided. Please set NF_API_KEY environment variable or provide api_key parameter.")
        
        self._set_auth_header()
        
        # Add API key to query params if provided
        params = params or {}
        if self.api_key:
            params["nf_api_key"] = self.api_key
        
        try:
            response = self.http_client.delete(
                f"{self.base_url}/{endpoint.lstrip('/')}",
                params=params,
            )
            
            return self._handle_response(response)
                
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {str(e)}") from e
        except httpx.RequestError as e:
            raise APIError(f"Request failed: {str(e)}") from e
    
    def _handle_response(self, response: httpx.Response) -> dict:
        """
        Handle the API response.
        
        Args:
            response: The HTTP response
            
        Returns:
            The JSON response
            
        Raises:
            RateLimitError: If rate limited
            ServerError: If server error
            AuthenticationError: If authentication failed
            AuthorizationError: If authorization failed
            NotFoundError: If resource not found
            APIError: For other API errors
        """
        if response.status_code == 429:
            raise RateLimitError(f"Rate limit exceeded: {response.text}", response.status_code, response)
        elif response.status_code >= 500:
            raise ServerError(f"Server error: {response.text}", response.status_code, response)
        elif response.status_code == 401:
            raise AuthenticationError(f"Authentication failed: {response.text}", response.status_code, response)
        elif response.status_code == 403:
            raise AuthorizationError(f"Authorization failed: {response.text}", response.status_code, response)
        elif response.status_code == 404:
            raise NotFoundError(f"Resource not found: {response.text}", response.status_code, response)
        elif response.status_code >= 400:
            raise APIError(f"API request failed: {response.text}", response.status_code, response)
        
        try:
            return response.json()
        except json.JSONDecodeError as e:
            raise APIError(f"Failed to parse JSON response: {response.text}", response.status_code, response) from e
    
    # Service property accessors
    
    @property
    def projects(self):
        if "projects" not in self._services:
            self._init_services()
        return self._services["projects"]
    
    @property
    def datasources(self):
        if "datasources" not in self._services:
            self._init_services()
        return self._services["datasources"]
    
    @property
    def datalines(self):
        if "datalines" not in self._services:
            self._init_services()
        return self._services["datalines"]
    
    @property
    def teams(self):
        if "teams" not in self._services:
            self._init_services()
        return self._services["teams"]
    
    @property
    def organizations(self):
        if "organizations" not in self._services:
            self._init_services()
        return self._services["organizations"]
    
    @property
    def users(self):
        if "users" not in self._services:
            self._init_services()
        return self._services["users"]
    
    @property
    def query_programs(self):
        if "query_programs" not in self._services:
            self._init_services()
        return self._services["query_programs"]
    
    @property
    def secrets(self):
        if "secrets" not in self._services:
            self._init_services()
        return self._services["secrets"]
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()

# Shorthand for InfactoryClient
Client = InfactoryClient
