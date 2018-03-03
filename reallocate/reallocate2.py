from utilities import accountsTotal



def reallocate2(reallocateAccounts, desiredAllocation):
    ''' Reallocates portfoilo one tax group at a time

    Args:
        fundAccount (dict): A dictionary of account objects representing entire portfolio
        desiredAllocation (dict): A dictionary of accounts with the desried percent allocation.
    '''
