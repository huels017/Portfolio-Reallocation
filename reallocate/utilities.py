

#### General Functions ####
###########################

def accountsTotal(accounts, accountsList):
    '''Returns the total value of accounts in accountsList

    Args:
        accounts (dict): A dictionary of account objects representing entire portfolio
        accountsList (list): A list of accounts that will be included in the total value
        totalAccountsValue (int): The sum of the total value of all accounts in accountsList
    '''
    totalAccountsValue = 0
    for account in accountsList:
        totalAccountsValue += accounts[account].get_total_value()
    return totalAccountsValue



def findAccountsWithType(accounts, accountType):
    '''Returns account names with a desired account type

    Args:
        accounts (dict): A dictionary of account objects representing entire portfolio
        accountType (str): Represents the type of the account
        accountsWithType (list): A list of accounts in which type == accountType
    '''
    accountsWithType = []

    for account in accounts:
        if accounts[account].account_type == accountType:
            accountsWithType.append(accounts[account])
    return accountsWithType


#### Funding Accounts ####
##########################

def fundAccount(accountToFund, accountToWithdraw, fundAmount):
    '''Moves funds from accountToWithdraw to accountToFund

    Args:
        accountToFund (object): An Account object which should be funded
        accountToWithdraw (object): An Account object which should be withdrawn
        fundAmount (int): The value that should be moved between accounts
    '''
    try:
        accountToWithdraw.withdraw_account('Cash/MMKT', fundAmount)
    except:
        print('Failed to withdraw account in fundAccount function')

    try:
        accountToFund.fund_account('Cash/MMKT', fundAmount)
    except:
        print('Failed to fund account in fundAccount function')



def condenseAccounts(accountToFill, accountsToEmpty):
    ''' Moves all funds from multiple accounts into one accountType as cash

    Args:
        accountToFill (object): An Account object that will receive all funds from accountsToEmpty
        accountsToEmpty (list): A list of Account objects which will all be liquidated into accountToFill
    '''
    for account in accountsToEmpty:

        for category in account.assets:
            categoryValueToMove = account.get_category_value(category)

            try:
                account.withdraw_account(category, categoryValueToMove)
            except:
                print('Failed to withdraw account in condenseAccounts function')

            try:
                accountToFill.fund_account('Cash/MMKT', categoryValueToMove)
            except:
                print('Failed to fund account in condenseAccounts function')



#### Reallocate Functions ####
##############################


def differenceCurrentDesiredAccounts(reallocateAccounts, desiredAllocation):
    '''Returns two lists. One of values per catogeries to sell. One of values per cateogry to buy.

    Args:
        fundAccount (dict): A dictionary of account objects representing entire portfolio
        desiredAllocation (dict): A dictionary of accounts with the desried percent allocation.
    '''




def findRules(reallocateAccounts, buyCategories, sellCategories):
    '''Does this need to be called by function above?
    '''


def sellAccount(account, sell, dampening, maxTaxedSales):

def buyAccount(account, buy, totalSales):
