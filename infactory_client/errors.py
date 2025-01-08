
import httpx

class APIError(Exception):
    """Base exception for API-related errors"""
    def __init__(self, message: str, status_code: int | None = None, response: httpx.Response | None = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)

class AuthenticationError(APIError):
    """Exception raised for authentication errors (401)"""
    pass

class AuthorizationError(APIError):
    """Exception raised for authorization errors (403)"""
    pass

class NotFoundError(APIError):
    """Exception raised when a resource is not found (404)"""
    pass

class ValidationError(APIError):
    """Exception raised for validation errors (422)"""
    pass

class RateLimitError(APIError):
    """Exception raised when API rate limit is exceeded (429)"""
    pass

class ServerError(APIError):
    """Exception raised for server-side errors (5xx)"""
    pass

class TimeoutError(APIError):
    """Exception raised when API request times out"""
    pass

class JWTError(Exception):
    """Base exception for JWT-related errors"""
    pass

class JWTFormatError(JWTError):
    """Exception raised when JWT token format is invalid"""
    pass

class JWTDecodeError(JWTError): 
    """Exception raised when JWT token parts cannot be decoded"""
    pass

class JWTExpiredError(JWTError):
    """Exception raised when JWT token has expired"""
    pass
