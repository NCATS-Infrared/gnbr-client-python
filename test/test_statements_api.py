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
from gnbr_beacon.api.statements_api import StatementsApi  # noqa: E501
from gnbr_beacon.rest import ApiException


class TestStatementsApi(unittest.TestCase):
    """StatementsApi unit test stubs"""

    def setUp(self):
        self.api = gnbr_beacon.api.statements_api.StatementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_statement_details(self):
        """Test case for get_statement_details

        """
        pass

    def test_get_statements(self):
        """Test case for get_statements

        """
        pass


if __name__ == '__main__':
    unittest.main()
