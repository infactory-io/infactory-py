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

from openapi_client.api.status_api import StatusApi


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatusApi()

    def tearDown(self) -> None:
        pass

    def test_health_check_health_check_get(self) -> None:
        """Test case for health_check_health_check_get

        Health Check
        """
        pass


if __name__ == '__main__':
    unittest.main()
