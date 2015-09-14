import utils

# This function takes a valid netid and does something interesting...
def foo(netid):
    if utils.validate_sam_account_name(netid):
        # Do something...

        return True
    else:
        # Nothing to do since the netid is invalid
        return False
