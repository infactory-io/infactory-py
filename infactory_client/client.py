


import os
import httpx
from pydantic import BaseModel
import time
import json
import base64
import tenacity

from infactory_client.errors import APIError, JWTDecodeError, JWTExpiredError, JWTFormatError, RateLimitError, ServerError


class ClientState(BaseModel):
    org_id: str | None = None
    team_id: str | None = None
    user_id: str | None = None
    role: str | None = None
    project_id: str | None = None
    datasource_id: str | None = None

def validate_jwt(token: str) -> str:
    """
    Validates a JWT token and returns the validated token.
    """
    # Basic validation - ensure token is non-empty string
    if not isinstance(token, str) or not token:
        raise JWTFormatError("Token must be a non-empty string")
    
    # Check token format (header.payload.signature)
    parts = token.split('.')
    if len(parts) != 3:
        raise JWTFormatError("Token must have 3 parts (header.payload.signature)")

    try:
        # Decode header and payload
        header = base64.b64decode(parts[0] + '=' * (-len(parts[0]) % 4))
        payload = base64.b64decode(parts[1] + '=' * (-len(parts[1]) % 4))
        
        # Verify they're valid JSON
        try:
            json.loads(header)
        except json.JSONDecodeError as e:
            raise JWTDecodeError(f"Failed to decode header - {str(e)}")
        try:
            payload_json = json.loads(payload)
        except json.JSONDecodeError as e:
            raise JWTDecodeError(f"Failed to decode payload - {str(e)}")
        
        # Check expiration if present
        if 'exp' in payload_json:
            if payload_json['exp'] < time.time():
                raise JWTExpiredError("Token has expired")
 
    except (JWTFormatError, JWTDecodeError, JWTExpiredError) as e:
        raise e
    except Exception as e:
        raise JWTDecodeError(f"Failed to decode token parts - {str(e)}") from e

    return token

class InfactoryClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None):
        self.api_key = api_key or os.getenv("INFACTORY_API_KEY")
        self.base_url = base_url or os.getenv("INFACTORY_BASE_URL") or "https://i7y.dev/v1"
        self.jwt_token = None
        self.state: ClientState | None = None


    def login(self):
        """
        This will login via the Clerk API and extenstion to set the JWT token.
        """
        raise NotImplementedError("Login via Clerk API not yet implemented")

    def connect(self):
        """
        Sends a request to the Infactory API to establish a connection.
        """
        response_json = self._post(
            "authentication/token",
            params={"username": "api"},
        )
        
        self.jwt_token = validate_jwt(response_json["access_token"])
        # Get user state
        if self.state is None:
            self.state = get_client(**response_json["user_id"])

    def refresh_token(self):
        """
        Refreshes the JWT token.
        """
        response_json = self._post(
            "authentication/refresh",
            params={"username": "api"}
        )
        self.jwt_token = validate_jwt(response_json["access_token"])

    def disconnect(self):
        """
        Sends a request to the Infactory API to disconnect from the connection.
        """
        self.jwt_token = None

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        """
        Makes a GET request to the specified API endpoint.
        
        Args:
            endpoint: The API endpoint to call (without base URL)
            params: Optional query parameters
            
        Returns:
            The JSON response from the API
        """
        if not self.jwt_token:
            raise Exception("Not connected. Call connect() first.")
            
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }
        
        response = httpx.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            headers=headers,
            params=params
        )

        if response.status_code == 429:
            raise RateLimitError(f"Rate limit exceeded: {response.text}")
        elif response.status_code >= 500:
            raise ServerError(f"Server error: {response.text}")
        elif response.status_code == 408:
            raise TimeoutError(f"Request timed out: {response.text}")
        elif response.status_code != 200:
            raise Exception(f"API request failed: {response.text}")

        try:
            return response.json()
        except Exception as e:
            raise APIError(f"Failed to parse JSON response: {response.text}") from e

    @tenacity.retry(
        stop=tenacity.stop_after_attempt(3),
        wait=tenacity.wait_exponential(multiplier=1, min=1, max=5),
        retry=tenacity.retry_if_exception_type((RateLimitError, ServerError, TimeoutError))
    )
    def _post(self, endpoint: str, data: dict | None = None, params: dict | None = None) -> dict:
        """
        Makes a POST request to the specified API endpoint.
        
        Args:
            endpoint: The API endpoint to call (without base URL)
            data: The JSON body to send
            params: Optional query parameters
            
        Returns:
            The JSON response from the API
        """
        if not self.jwt_token:
            raise Exception("Not connected. Call connect() first.")
            
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        
        response = httpx.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            headers=headers,
            json=data,
            params=params
        )

        if response.status_code == 429:
            raise RateLimitError(f"Rate limit exceeded: {response.text}")
        elif response.status_code >= 500:
            raise ServerError(f"Server error: {response.text}")
        elif response.status_code == 408:
            raise TimeoutError(f"Request timed out: {response.text}")
        elif response.status_code != 200:
            raise Exception(f"API request failed: {response.text}")

        try:
            return response.json()
        except Exception as e:
            raise APIError(f"Failed to parse JSON response: {response.text}") from e
