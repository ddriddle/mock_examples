from mock import patch
from unittest import TestCase

from cool import add, add2

class AddTestCase(TestCase):

    @patch('cool.logging', autospec=True)
    def test_add2_one_plus_one_equals_two(self, mock):
        self.assertEqual(add2(1, 1), 2)

        assert not mock.warning.called

    @patch('cool.logging', autospec=True)
    def test_add_one_plus_one_equals_two(self, mock):
        self.assertEqual(add(1, 1), 2)

        mock.warning.assert_called_once_with('x + y = 2')
