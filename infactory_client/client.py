import json
import logging
import os
import pathlib
from collections.abc import Callable
from enum import Enum
from typing import Any, TypeVar

import httpx
import tenacity
from pydantic import BaseModel, ConfigDict, Field

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("infactory-client")

# Type definitions
T = TypeVar("T")
ResponseType = dict[str, Any]


class APIErrorCode(Enum):
    """Error codes for API responses."""

    AUTHENTICATION = 401
    AUTHORIZATION = 403
    NOT_FOUND = 404
    VALIDATION = 422
    RATE_LIMIT = 429
    SERVER = 500


class APIError(Exception):
    """Base exception for all API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response: httpx.Response | None = None,
    ):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class ClientState(BaseModel):
    """Client state with improved field documentation and defaults."""

    user_id: str | None = Field(default=None, description="User ID from authentication")
    user_email: str | None = Field(default=None, description="User email")
    user_name: str | None = Field(default=None, description="User display name")
    user_created_at: str | None = Field(
        default=None, description="User creation timestamp"
    )
    organization_id: str | None = Field(
        default=None, description="Current organization ID"
    )
    team_id: str | None = Field(default=None, description="Current team ID")
    project_id: str | None = Field(default=None, description="Current project ID")
    api_key: str | None = Field(default=None, description="API key for authentication")
    base_url: str | None = Field(default=None, description="Base URL for API endpoints")

    model_config = ConfigDict(extra="ignore")


class InfactoryClient:
    """
    Client for interacting with the Infactory API.

    Simplified and improved client with better error handling, caching,
    and cleaner service initialization.
    """

    DEFAULT_BASE_URL = "https://api.infactory.ai"
    CONFIG_DIR_ENV_VAR = "NF_HOME"
    API_KEY_ENV_VAR = "NF_API_KEY"
    BASE_URL_ENV_VAR = "NF_BASE_URL"

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
    ):
        """
        Initialize the client with improved configuration options.

        Args:
            api_key: API key for authentication (optional)
            base_url: Base URL for API endpoints (optional)
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts for failed requests
        """
        # Setup configuration
        self.config_dir = self._get_config_dir()
        self.base_url = self._resolve_base_url(base_url)
        self.api_key = self._resolve_api_key(api_key)
        self.timeout = timeout
        self.max_retries = max_retries

        # Initialize state and HTTP client
        self.state = self._load_state()
        self._http_client = None
        self._services = {}

        # Update state with current configuration
        self.state.api_key = self.api_key
        self.state.base_url = self.base_url

    @property
    def http_client(self) -> httpx.Client:
        """Lazy-loaded HTTP client."""
        if self._http_client is None:
            self._http_client = httpx.Client(
                base_url=self.base_url, timeout=self.timeout, follow_redirects=True
            )
            # Set authorization header if API key is available
            if self.api_key:
                self._http_client.headers["Authorization"] = f"Bearer {self.api_key}"
        return self._http_client

    def _get_config_dir(self) -> pathlib.Path:
        """Get or create configuration directory."""
        config_dir = os.getenv(self.CONFIG_DIR_ENV_VAR) or os.path.expanduser(
            "~/.infactory-client/"
        )
        path = pathlib.Path(config_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _resolve_base_url(self, base_url: str | None) -> str:
        """Resolve base URL from parameters or environment variables."""
        resolved_url = (
            base_url or os.getenv(self.BASE_URL_ENV_VAR) or self.DEFAULT_BASE_URL
        )
        return resolved_url.rstrip("/")  # Ensure no trailing slash

    def _resolve_api_key(self, api_key: str | None) -> str | None:
        """Resolve API key from parameters, environment variables, or config file."""
        if api_key:
            return api_key

        if env_key := os.getenv(self.API_KEY_ENV_VAR):
            return env_key

        return self._load_api_key_from_file()

    def _load_api_key_from_file(self) -> str | None:
        """Load API key from configuration file."""
        api_key_file = self.config_dir / "api_key"
        if api_key_file.exists():
            try:
                return api_key_file.read_text().strip()
            except Exception as e:
                logger.warning(f"Failed to load API key from {api_key_file}: {e}")
        return None

    def save_api_key(self, api_key: str) -> None:
        """Save API key to configuration file with proper permissions."""
        api_key_file = self.config_dir / "api_key"
        try:
            api_key_file.write_text(api_key)
            api_key_file.chmod(0o600)  # Secure file permissions
            self.api_key = api_key
            self.state.api_key = api_key
            # Update HTTP client headers if it exists
            if self._http_client:
                self._http_client.headers["Authorization"] = f"Bearer {api_key}"
        except Exception as e:
            logger.error(f"Failed to save API key to {api_key_file}: {e}")
            raise OSError(f"Failed to save API key: {e}")

    def _load_state(self) -> ClientState:
        """Load client state from file, with fallback to empty state."""
        state_file = self.config_dir / "state.json"
        if state_file.exists():
            try:
                state_data = json.loads(state_file.read_text())
                return ClientState(**state_data)
            except Exception as e:
                logger.warning(f"Failed to load state from {state_file}: {e}")
        return ClientState()

    def save_state(self) -> None:
        """Save current client state to file."""
        state_file = self.config_dir / "state.json"
        try:
            state_file.write_text(self.state.model_dump_json(exclude_none=True))
        except Exception as e:
            logger.warning(f"Failed to save state to {state_file}: {e}")

    def connect(self) -> "InfactoryClient":
        """
        Validate connection and authenticate with the API.

        Returns:
            The client instance for method chaining

        Raises:
            APIError: If authentication fails
        """
        if not self.api_key:
            raise APIError(
                "No API key provided. Set via NF_API_KEY environment variable or provide api_key parameter."
            )

        # Test connection by getting current user info
        try:
            user_info = self.get("v1/authentication/me")

            # Update state with user information
            self.state.user_id = user_info.get("id")
            self.state.user_email = user_info.get("email")
            self.state.user_name = user_info.get("name")
            self.state.user_created_at = user_info.get("created_at")
            self.save_state()

            logger.info("Connected to Infactory")
        except Exception as e:
            raise APIError(f"Failed to connect with the provided API key: {e}")

        return self

    def disconnect(self) -> None:
        """Close HTTP client and clean up resources."""
        if self._http_client:
            self._http_client.close()
            self._http_client = None

    def _create_request_retry_decorator(self) -> Callable:
        """Create request retry decorator with configured settings."""
        return tenacity.retry(
            stop=tenacity.stop_after_attempt(self.max_retries),
            wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
            retry=tenacity.retry_if_exception_type(APIError),
            reraise=True,
        )

    def _handle_response(self, response: httpx.Response) -> dict[str, Any] | str:
        """
        Process API response and handle errors with appropriate exceptions.

        Args:
            response: HTTP response from API

        Returns:
            Parsed JSON response

        Raises:
            APIError: With appropriate subtype based on status code
        """
        if response.is_success:
            try:
                # First try to json decode the response
                try:
                    return response.json()
                except json.JSONDecodeError:
                    pass

                # Then try to parse the response as an SSE response
                content = response.text
                lines = []
                data = {}
                for line in content.splitlines():
                    lines.append(line)
                    if line.startswith("data: "):
                        value = line[6:].strip()
                        try:
                            value = json.loads(value)
                        except json.JSONDecodeError:
                            pass
                        data["data"] = value
                    elif line.startswith("event: "):
                        data["event"] = line[6:].strip()
                    else:
                        pass
                if data:
                    return data
                return response.text
            except json.JSONDecodeError:
                raise APIError(
                    f"Failed to parse JSON response: {response.text}",
                    response.status_code,
                    response,
                )

        # Handle error responses based on status code
        error_message = f"API request failed ({response.status_code}): {response.text}"

        if response.status_code == APIErrorCode.RATE_LIMIT.value:
            error_message = f"Rate limit exceeded: {response.text}"
        elif response.status_code == APIErrorCode.AUTHENTICATION.value:
            error_message = f"Authentication failed: {response.text}"
        elif response.status_code == APIErrorCode.AUTHORIZATION.value:
            error_message = f"Authorization failed: {response.text}"
        elif response.status_code == APIErrorCode.NOT_FOUND.value:
            error_message = f"Resource not found: {response.text}"
        elif response.status_code >= 500:
            error_message = f"Server error: {response.text}"

        raise APIError(error_message, response.status_code, response)

    def request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Make a request to the API with automatic retry and error handling.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request body data for POST/PATCH requests
            params: Query parameters

        Returns:
            Parsed JSON response

        Raises:
            APIError: If the request fails
        """
        if not self.api_key:
            raise APIError("No API key provided")

        # Ensure endpoint is properly formatted
        endpoint = endpoint.lstrip("/")

        # Add API key to query params if provided
        params = params or {}
        if self.api_key:
            params["nf_api_key"] = self.api_key

        retry_decorator = self._create_request_retry_decorator()

        @retry_decorator
        def make_request():
            try:
                response = self.http_client.request(
                    method=method.upper(),
                    url=endpoint,
                    json=data if method.upper() in ("POST", "PATCH", "PUT") else None,
                    params=params,
                )
                return self._handle_response(response)
            except httpx.TimeoutException as e:
                raise APIError(f"Request timed out: {str(e)}")
            except httpx.RequestError as e:
                raise APIError(f"Request failed: {str(e)}")

        return make_request()

    # Convenience methods for common HTTP verbs
    def get(
        self, endpoint: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Make a GET request to the API."""
        return self.request("GET", endpoint, params=params)

    def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a POST request to the API."""
        return self.request("POST", endpoint, data=data, params=params)

    def patch(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a PATCH request to the API."""
        return self.request("PATCH", endpoint, data=data, params=params)

    def delete(
        self, endpoint: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Make a DELETE request to the API."""
        return self.request("DELETE", endpoint, params=params)

    # Context management methods
    def __enter__(self) -> "InfactoryClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit with proper cleanup."""
        self.disconnect()

    # Service property with lazy loading
    def _get_service(self, name: str) -> Any:
        """Get a service by name, initializing it if necessary."""
        if name not in self._services:
            self._init_services()
        return self._services[name]

    def _init_services(self) -> None:
        """Initialize service clients as needed."""
        from infactory_client.services import (
            DataLinesService,
            DataSourcesService,
            JobsService,
            OrganizationsService,
            ProjectsService,
            QueryProgramsService,
            TeamsService,
            UsersService,
        )

        self._services = {
            "projects": ProjectsService(self),
            "datasources": DataSourcesService(self),
            "datalines": DataLinesService(self),
            "teams": TeamsService(self),
            "organizations": OrganizationsService(self),
            "users": UsersService(self),
            "query_programs": QueryProgramsService(self),
            "jobs": JobsService(self),
            # Add more services as needed
        }

    # Service properties through proxy
    @property
    def projects(self):
        return self._get_service("projects")

    @property
    def datasources(self):
        return self._get_service("datasources")

    @property
    def datalines(self):
        return self._get_service("datalines")

    @property
    def teams(self):
        return self._get_service("teams")

    @property
    def organizations(self):
        return self._get_service("organizations")

    @property
    def users(self):
        return self._get_service("users")

    @property
    def query_programs(self):
        return self._get_service("query_programs")

    @property
    def jobs(self):
        return self._get_service("jobs")

    # Helper methods for setting current context
    def set_current_project(self, project_id: str) -> None:
        """Set the current project and save state."""
        self.state.project_id = project_id
        self.save_state()

    def set_current_organization(self, organization_id: str) -> None:
        """Set the current organization and save state."""
        self.state.organization_id = organization_id
        self.save_state()

    def set_current_team(self, team_id: str) -> None:
        """Set the current team and save state."""
        self.state.team_id = team_id
        self.save_state()


# Shorthand for InfactoryClient
Client = InfactoryClient
