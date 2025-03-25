import httpx


class APIError(Exception):
    """Base class for all API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response: httpx.Response | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response

    def __str__(self):
        if self.status_code:
            return f"{self.message} (Status: {self.status_code})"
        return self.message


class AuthenticationError(APIError):
    """Raised when authentication fails."""

    pass


class AuthorizationError(APIError):
    """Raised when the user doesn't have permission to access a resource."""

    pass


class NotFoundError(APIError):
    """Raised when a resource is not found."""

    pass


class ValidationError(APIError):
    """Raised when request validation fails."""

    pass


class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""

    pass


class ServerError(APIError):
    """Raised when the server returns a 5xx error."""

    pass


class TimeoutError(APIError):
    """Raised when a request times out."""

    pass


class ConfigError(Exception):
    """Raised when there is an issue with the configuration."""

    pass
