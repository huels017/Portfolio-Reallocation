


def accountsTotal(accounts, accountsList):
    '''
    Returns the total value of accounts in accountsList
    '''
    totalAccountsValue = 0
    for account in accountsList:
        totalAccountsValue += accounts[account].get_total_value()
    return totalAccountsValue



def findAccountsWithType(accounts, accountType):
    '''
    Returns account names with a desired account type
    '''
    accountsWithType = []

    for account in accounts:
        if accounts[account].account_type == accountType:
            accountsWithType.append(account)
    return accountsWithType



def fundAccount(accounts, accountToFund, accountToWithdraw, fundAmount):
    '''
    Moves funds from accountToWithdraw to accountToFund
    '''
    accounts[accountToFund].fund_account('Cash/MMKT', fundAmount)
    accounts[accountToWithdraw].withdraw_account('Cash/MMKT', fundAmount)




def condenseAccounts(accounts, accountToFill, accountsToEmpty):
    ''' Moves all funds from multiple accounts into one accountType as cash
    '''

    for account in accountsToEmpty:
        for category in accounts[account].assets:

            accounts[accountToFill].fund_account('Cash/MMKT', accounts[account].get_category_value(category))
            accounts[account].withdraw_account(category, accounts[account].get_category_value(category))
