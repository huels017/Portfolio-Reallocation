from utilities import sellFirstCategories, differenceCurrentDesiredAccounts

def reallocate2(reallocateAccounts, desiredAllocation, categoryRules, taxGroups):
    '''The Reallocate function will move through a sequence of steps to reallocate
    the portfoilo to the desired allocation.

    Args:
        reallocateAccounts (dict): A dictionary of account objects representing entire portfolio
        desiredAllocation (dict): A dictionary of categories with the desired percent allocation
        categoryRules (dict): A dictionary of rules for categories.
        taxGroups (list): A list of the 3 different tax groups.
    '''
    taxedSalesLeft = 100000 #need to pull from excel

    #### 'Sell first' Category ####
    sellFirstCategories(reallocateAccounts, categoryRules, taxedSalesLeft)

    #### Reallocate Accounts ####
    differenceCurrentDesiredAccounts(reallocateAccounts, desiredAllocation)
