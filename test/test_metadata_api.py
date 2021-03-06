# coding: utf-8

"""
    GNBR Knowledge Beacon API

    This is the GNBR Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: srensi@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import gnbr_beacon
from gnbr_beacon.api.metadata_api import MetadataApi  # noqa: E501
from gnbr_beacon.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = gnbr_beacon.api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_concept_categories(self):
        """Test case for get_concept_categories

        """
        pass

    def test_get_knowledge_map(self):
        """Test case for get_knowledge_map

        """
        pass

    def test_get_predicates(self):
        """Test case for get_predicates

        """
        pass


if __name__ == '__main__':
    unittest.main()
