from typing import Any, Generic, TypeVar

T = TypeVar("T")


class BaseService:
    """
    Base class for all service implementations.

    Args:
        client: The InfactoryClient instance
    """

    def __init__(self, client):
        """Initialize the service with a client instance."""
        self.client = client

    def _get(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        """
        Make a GET request to the API.

        Args:
            endpoint: The API endpoint to call
            params: Query parameters

        Returns:
            The JSON response
        """
        return self.client.get(endpoint, params=params if params is not None else {})

    def _post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """
        Make a POST request to the API.

        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters

        Returns:
            The JSON response
        """
        return self.client.post(
            endpoint,
            data=data if data is not None else {},
            params=params if params is not None else {},
        )

    def _patch(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """
        Make a PATCH request to the API.

        Args:
            endpoint: The API endpoint to call
            data: The request body
            params: Query parameters

        Returns:
            The JSON response
        """
        return self.client.patch(
            endpoint,
            data=data if data is not None else {},
            params=params if params is not None else {},
        )

    def _delete(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        """
        Make a DELETE request to the API.

        Args:
            endpoint: The API endpoint to call
            params: Query parameters

        Returns:
            The JSON response
        """
        return self.client.delete(endpoint, params=params if params is not None else {})


class ModelFactory(Generic[T]):
    """
    Factory for creating model instances from API responses.

    Args:
        model_class: The model class to instantiate
    """

    def __init__(self, model_class):
        """Initialize the factory with a model class."""
        self.model_class = model_class

    def create(self, data: dict[str, Any]) -> T:
        """
        Create an instance of the model from a dictionary.

        Args:
            data: Dictionary of model data

        Returns:
            An instance of the model
        """
        return self.model_class(**data)

    def create_list(self, data_list: list[dict[str, Any]]) -> list[T]:
        """
        Create a list of model instances from a list of dictionaries.

        Args:
            data_list: List of dictionaries containing model data

        Returns:
            A list of model instances
        """
        return [self.create(item) for item in data_list]
