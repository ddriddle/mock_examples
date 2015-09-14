from unittest import TestCase
from cool import foo

from mock import patch

class FooTestCase(TestCase):

    @patch('cool.validate_sam_account_name')
    def test_foo_valid_netid(self, mock):
        mock.return_value = True

        self.assertTrue(foo("testnetid1"))

    @patch('cool.validate_sam_account_name')
    def test_foo_invalid_netid(self, mock):
        mock.return_value = False

        self.assertFalse(foo("foo"))
