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

from infactory_client.models.platform_create import PlatformCreate

class TestPlatformCreate(unittest.TestCase):
    """PlatformCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformCreate:
        """Test PlatformCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformCreate`
        """
        model = PlatformCreate()
        if include_optional:
            return PlatformCreate(
                name = '',
                description = '',
                metadata = None
            )
        else:
            return PlatformCreate(
        )
        """

    def testPlatformCreate(self):
        """Test PlatformCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
