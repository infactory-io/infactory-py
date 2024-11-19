# coding: utf-8

"""
    Find the knowledge in your data

    <h2><img src='/logo.svg' alt='Infactory' height='50'></h2><p><ul><li><a href='/er.svg'>Entity-Relationship Diagram</a></li><li><a href='/er.md'>Documentation</a></li></ul></p>

    The version of the OpenAPI document: 0.5.0
    Contact: support@infactory.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.data_sources_api import DataSourcesApi


class TestDataSourcesApi(unittest.TestCase):
    """DataSourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataSourcesApi()

    def tearDown(self) -> None:
        pass

    def test_create_datasource_endpoint_v1_datasources_project_id_post(self) -> None:
        """Test case for create_datasource_endpoint_v1_datasources_project_id_post

        Create Datasource Endpoint
        """
        pass

    def test_delete_datasource_endpoint_v1_datasources_datasource_id_delete(self) -> None:
        """Test case for delete_datasource_endpoint_v1_datasources_datasource_id_delete

        Delete Datasource Endpoint
        """
        pass

    def test_get_datasource_endpoint_v1_datasources_datasource_id_get(self) -> None:
        """Test case for get_datasource_endpoint_v1_datasources_datasource_id_get

        Get Datasource Endpoint
        """
        pass

    def test_get_datasources_endpoint_v1_datasources_project_project_id_get(self) -> None:
        """Test case for get_datasources_endpoint_v1_datasources_project_project_id_get

        Get Datasources Endpoint
        """
        pass

    def test_update_datasource_endpoint_v1_datasources_datasource_id_patch(self) -> None:
        """Test case for update_datasource_endpoint_v1_datasources_datasource_id_patch

        Update Datasource Endpoint
        """
        pass

    def test_upload_source_v1_datasources_datasource_id_upload_post(self) -> None:
        """Test case for upload_source_v1_datasources_datasource_id_upload_post

        Upload a data source file
        """
        pass


if __name__ == '__main__':
    unittest.main()
