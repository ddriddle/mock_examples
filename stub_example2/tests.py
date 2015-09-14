from unittest import TestCase
from cool import foo

##################### Stub vaild_sam_account_name #####################
import utils
vaild_sam_account_names = ['testnetid1', 'testnetid2']
def validate_sam_account_name(sam_account_name):
    """
    Overide validate_sam_account_name so that our tests to not make
    calls to AD.
    """
    if sam_account_name in vaild_sam_account_names:
        return True
    else:
        return False

utils.validate_sam_account_name = validate_sam_account_name
#######################################################################

class FooTestCase(TestCase):

    def test_foo_valid_netid(self):
        self.assertTrue(foo("testnetid1"))

    def test_foo_invalid_netid(self):
        self.assertFalse(foo("foo"))
