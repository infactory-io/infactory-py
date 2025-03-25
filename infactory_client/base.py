from typing import Any, Dict, List, Optional, Union, TypeVar, Generic
from pydantic import BaseModel

T = TypeVar('T')

class BaseService:
    """
    Base class for all service implementations.
    
    Args:
        client: The InfactoryClient instance
    """
    
    def __init__(self, client):
        """Initialize the service with a client instance."""
        self.client = client
    
    def _get(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: The API endpoint to call
            params: Query parameters
            
        Returns:
            The JSON response
        """
        return self.client._get(endpoint, params)
    
    def _post(self, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Any:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters
            
        Returns:
            The JSON response
        """
        return self.client._post(endpoint, data, params)
    
    def _patch(self, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Any:
        """
        Make a PATCH request to the API.
        
        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters
            
        Returns:
            The JSON response
        """
        return self.client._patch(endpoint, data, params)
    
    def _delete(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint: The API endpoint to call
            params: Query parameters
            
        Returns:
            The JSON response
        """
        return self.client._delete(endpoint, params)


class ModelFactory(Generic[T]):
    """
    Factory for creating model instances from API responses.
    
    Args:
        model_class: The model class to instantiate
    """
    
    def __init__(self, model_class):
        """Initialize the factory with a model class."""
        self.model_class = model_class
    
    def create(self, data: Dict[str, Any]) -> T:
        """
        Create an instance of the model from a dictionary.
        
        Args:
            data: Dictionary of model data
            
        Returns:
            An instance of the model
        """
        return self.model_class(**data)
    
    def create_list(self, data_list: List[Dict[str, Any]]) -> List[T]:
        """
        Create a list of model instances from a list of dictionaries.
        
        Args:
            data_list: List of dictionaries containing model data
            
        Returns:
            A list of model instances
        """
        return [self.create(item) for item in data_list]
