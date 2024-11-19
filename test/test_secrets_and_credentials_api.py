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

from openapi_client.api.secrets_and_credentials_api import SecretsAndCredentialsApi


class TestSecretsAndCredentialsApi(unittest.TestCase):
    """SecretsAndCredentialsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecretsAndCredentialsApi()

    def tearDown(self) -> None:
        pass

    def test_create_credential_v1_credentials_post(self) -> None:
        """Test case for create_credential_v1_credentials_post

        Create Credential
        """
        pass

    def test_create_secret_endpoint_v1_secrets_team_id_post(self) -> None:
        """Test case for create_secret_endpoint_v1_secrets_team_id_post

        Create Secret Endpoint
        """
        pass

    def test_delete_all_team_secrets_endpoint_v1_secrets_team_id_delete(self) -> None:
        """Test case for delete_all_team_secrets_endpoint_v1_secrets_team_id_delete

        Delete All Team Secrets Endpoint
        """
        pass

    def test_delete_credential_v1_credentials_credential_id_delete(self) -> None:
        """Test case for delete_credential_v1_credentials_credential_id_delete

        Delete Credential
        """
        pass

    def test_delete_secret_endpoint_v1_secrets_team_id_key_delete(self) -> None:
        """Test case for delete_secret_endpoint_v1_secrets_team_id_key_delete

        Delete Secret Endpoint
        """
        pass

    def test_delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete(self) -> None:
        """Test case for delete_secrets_by_type_endpoint_v1_secrets_team_id_type_type_delete

        Delete Secrets By Type Endpoint
        """
        pass

    def test_get_credential_v1_credentials_credential_id_get(self) -> None:
        """Test case for get_credential_v1_credentials_credential_id_get

        Get Credential
        """
        pass

    def test_get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get(self) -> None:
        """Test case for get_credentials_by_datasource_v1_credentials_datasource_datasource_id_get

        Get Credentials By Datasource
        """
        pass

    def test_get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get(self) -> None:
        """Test case for get_credentials_by_infrastructure_v1_credentials_infrastructure_infrastructure_id_get

        Get Credentials By Infrastructure
        """
        pass

    def test_get_credentials_by_organization_v1_credentials_organization_organization_id_get(self) -> None:
        """Test case for get_credentials_by_organization_v1_credentials_organization_organization_id_get

        Get Credentials By Organization
        """
        pass

    def test_get_credentials_by_team_v1_credentials_team_team_id_get(self) -> None:
        """Test case for get_credentials_by_team_v1_credentials_team_team_id_get

        Get Credentials By Team
        """
        pass

    def test_get_secret_endpoint_v1_secrets_team_id_key_get(self) -> None:
        """Test case for get_secret_endpoint_v1_secrets_team_id_key_get

        Get Secret Endpoint
        """
        pass

    def test_get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get(self) -> None:
        """Test case for get_secrets_by_credential_endpoint_v1_secrets_credentials_credentials_id_get

        Get Secrets By Credential Endpoint
        """
        pass

    def test_get_secrets_by_type_endpoint_v1_secrets_team_id_get(self) -> None:
        """Test case for get_secrets_by_type_endpoint_v1_secrets_team_id_get

        Get Secrets By Type Endpoint
        """
        pass

    def test_import_secrets_endpoint_v1_secrets_team_id_import_post(self) -> None:
        """Test case for import_secrets_endpoint_v1_secrets_team_id_import_post

        Import Secrets Endpoint
        """
        pass

    def test_rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post(self) -> None:
        """Test case for rotate_secret_endpoint_v1_secrets_team_id_key_rotate_post

        Rotate Secret Endpoint
        """
        pass

    def test_update_credential_v1_credentials_credential_id_patch(self) -> None:
        """Test case for update_credential_v1_credentials_credential_id_patch

        Update Credential
        """
        pass

    def test_update_secret_endpoint_v1_secrets_team_id_key_patch(self) -> None:
        """Test case for update_secret_endpoint_v1_secrets_team_id_key_patch

        Update Secret Endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
