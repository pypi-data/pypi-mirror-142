"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.124
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.ui_nodes import UiNodes
from ory_client.model.ui_texts import UiTexts
globals()['UiNodes'] = UiNodes
globals()['UiTexts'] = UiTexts
from ory_client.model.ui_container import UiContainer


class TestUiContainer(unittest.TestCase):
    """UiContainer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUiContainer(self):
        """Test UiContainer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UiContainer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
