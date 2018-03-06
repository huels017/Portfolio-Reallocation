


def accountsTotal(accounts, accountsList):
    '''Returns the total value of accounts in accountsList

    Args:
        accounts (dict): A dictionary of account objects representing entire portfolio
        accountsList (list) or (dict): A list or dict of accounts that will be included in the total value
        totalAccountsValue (int): The sum of the total value of all accounts in accountsList
    '''
    totalAccountsValue = 0
    for account in accountsList:
        if str(type(account)) == "<type 'unicode'>":
            totalAccountsValue += accounts[account].get_total_value()
        else:
            totalAccountsValue += account.get_total_value()
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


#### Reallocation Functions ####


def sellFirstCategories(reallocateAccounts, categoryRules, taxedSalesLeft):
    ''' Scans the categoryRules for any category(s) that is prioritized to sell first

    Args:
        reallocateAccounts (dict): A dictionary of account objects representing entire portfolio
        categoryRules (dict): A dictionary of rules for categories.
    '''

    for rule in categoryRules:
        if categoryRules[rule]['rule'] == 'Sell First':
            for account in reallocateAccounts:
                #need accountType merged before this can function properly
                if reallocateAccounts[account].accountType == 'Fixed':
                    continue
                elif reallocateAccounts[account].accountType == 'NQ':
                    transferValue = min(taxedSalesLeft), reallocateAccounts[account].get_category_value(categoryRules[rule]['category'])
                    taxedSalesLeft -= transferValue
                else:
                    transferValue = reallocateAccounts[account].get_category_value(categoryRules[rule]['category'])

                try:
                    reallocateAccounts[account].withdraw_account(categoryRules[rule]['category'], transferValue)
                except:
                    print('Failed to withdraw account in fundAccount function')

                try:
                    reallocateAccounts[account].fund_account('Cash/MMKT', transferValue)
                except:
                    print('Failed to fund account in fundAccount function')


def categoryTotal(accounts, category):
    '''Returns the total value of a single category across all accounts

    Args:
        accounts (dict): A dictionary of account objects representing entire portfolio
        category (str): A string representing the category to totalize.
        categoryTotal (int): A integer representing the total value of a single category across all accounts.
    '''
    categoryTotal = 0
    for account in accounts:
        categoryTotal += accounts[account].get_category_value(category)
    return categoryTotal


def portfolioTotalValue(accounts):
    ''' Returns the total value of a portfolio

    Args:
        accounts (dict): A dictionary of account objects representing entire portfolio
        portfolioTotal (int): A integer representing the total value of a portfolio.
    '''
    portfolioTotal = 0
    for account in accounts:
        portfolioTotal += accounts[account].get_total_value()
    return portfolioTotal


def differenceCurrentDesiredAccounts(reallocateAccounts, desiredAllocation):
    ''' Returns the difference per category between the current and the desired allocation. Positive numbers mean that category should be sold.

    Args:
        reallocateAccounts (dict): A dictionary of account objects representing entire portfolio
        desiredAllocation (dict): A dictionary of categories with the desired percent allocation
        buySellCategories (dict): A dictionary of categories with the value to be sold to reach desired allocation. (negitive numbers mean it should be bought)
    '''
    buySellCategories = {}
    for category in desiredAllocation:
        desiredValue = desiredAllocation[category] * portfolioTotalValue(reallocateAccounts)
        currentValue = categoryTotal(reallocateAccounts, category)
        buySellCategories[category] = desiredValue - currentValue
    return buySellCategories
