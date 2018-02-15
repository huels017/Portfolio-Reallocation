from main_functions import desiredCategoryTotal, listOfCategories, findAccountsWithRule, categoryPriorityList, listOfAccounts, cashOnHand, findAccountType


'''
Functions used in the reallocate function
'''


'''
def categoryValuesList(accounts, category):
    ''
    Returns a list of values for each category in an account execpt for the 'Total (pPortfolio)' row
    ''
    return accounts.getColumns(category)[0:-1]
'''


def categoryValuesList(accounts, category):
    '''
    Returns a list of values for each account in a specific category
    Does not inculde 'Total (Portfolio)' row
    '''
    accountsList = listOfAccounts()
    listOfCategoryValues = []

    for account in accountsList:
        listOfCategoryValues.append(accounts.getValue(account,category))

    return listOfCategoryValues




def categoryValueTotal(accounts, category):
    '''
    Returns the total value of a single category across all accounts
    '''
    listOfCategoryValues = categoryValuesList(accounts, category)
    categoryTotalValue = 0
    for category in listOfCategoryValues:
        categoryTotalValue += category

    return categoryTotalValue



def desiredVsRealCategoryValue(accounts, category):
    '''
    returns the difference between the desired category value
    and the real category getValue
    Positive values mean that the category should be sold
    Negitive values mean that the category should be bought
    The +/- will be used in 'buySellCategories' to split categories into buy and sell groups
    '''
    return categoryValueTotal(accounts, category) - desiredCategoryTotal(category)



def buySellCategories(accounts):
    '''
    Returns two lists/dicts,
    1) list/dict of categories to buy and value needed to buy to reach desired allocation
    2) list/dict of categoies to sell and value needed to sell to reach desired allocation
    Note: May want to use +0.01 and -0.01 to split buys and sell to avoid grouping categries with near 0 but not excatly 0 values. ie 0.0000000000000001234234
    '''
    buyCategories = []
    sellCategories = []

    categoryList = listOfCategories()

    for category in categoryList:
        sellValue = desiredVsRealCategoryValue(accounts, category)
        if sellValue > 0:
            sellCategories.append([category, sellValue])
        elif sellValue <0:
            buyCategories.append([category, -sellValue])

    return sellCategories, buyCategories



def accountSales(accounts, account):  #, rule, SpecialRules):
    '''
    Sells funds within given account based off buySellCategories
    ***Still needed***
        -track total non-cash sales,
        -special rule, stop sales if non-cash sales > max taxed sales, and Rule = "NQ"
        -special rule, if HSA account, stop cash/MMKT sale when cash/MMKT = HSA min
    '''
    sellCategories, buyCategories = buySellCategories(accounts)
    sales = 0


    for category in sellCategories:
        NAME = 0
        SELL_VALUE = 1
        smallerSale = min(category[SELL_VALUE], accounts.getValue(account, category[NAME]))
        accountCategoryValue = accounts.getValue(account, category[NAME]) - smallerSale
        accounts.setValue(account, category[NAME], accountCategoryValue)
        sales += smallerSale
    return sales



def accountBuys(accounts, account, sales):
    '''
    Buys funds within given account based off buySellCategories
    '''
    sellCategories, buyCategories = buySellCategories(accounts)
    #variable below this line shouldn't change, Should I make it into a fixed variable outside this function? on this .py file? or global? CATEGORY_LISTED_BY_PRIOTITY
    categoryListedByPriority = categoryPriorityList()

    for category in categoryListedByPriority:
        for buyCategory  in buyCategories:
            if category == buyCategory [0]:
                smallerBuy  = min(buyCategory [1], sales)
                accountCategoryValue = accounts.getValue(account, buyCategory [0]) + smallerBuy
                accounts.setValue(account, buyCategory [0], accountCategoryValue)
                sales -= smallerBuy




def reallocateRuleGroup(accounts, rule):  #, SpecialRules):
    '''
    Reallocates all accounts within one rule group by mondifying the accounts_copy DataContainer
    '''
    accountsInRuleGroup = findAccountsWithRule(rule)

    for account in accountsInRuleGroup:
        sales = 0
        sales += accountSales(accounts, account)
        accountBuys(accounts, account, sales)




def interAccountTransfer(accounts, accountFrom, categoryFrom, accountTo, categoryTo, transferValue):
    '''
    Transfers a value from a category in one account to a category in a second account
    '''
    fromAccountValue = accounts.getValue(accountFrom, categoryFrom)
    toAccountValue = accounts.getValue(accountTo, categoryTo)

    if fromAccountValue < transferValue:
        return "Not enough funds to complete Transfer between accounts"

    accounts.setValue(accountFrom, categoryFrom, (fromAccountValue - transferValue))
    accounts.setValue(accountTo, categoryTo, (toAccountValue + transferValue))



def fundAccount(accounts, accountType, contributionValue):
    '''
    Determine if account funding is needed for special cases: IRA funding
    Determine if CashOnHand is able to fund needed Contribution
    Make account transfer is needed and able
    Currently funds the first account in the list with the correct account Type
    '''
    FIRST_IN_LIST = 0
    CASH_RULE = "CASH"

    cashOnHandValue = cashOnHand()
    cashOnHandAccounts = findAccountsWithRule(CASH_RULE)
    firstCashOnHandAccount = cashOnHandAccounts[FIRST_IN_LIST]

    accountsWithType = findAccountType(accounts, accountType)
    firstAccountWithtype = accountsWithType[FIRST_IN_LIST]


    if cashOnHandValue >= contributionValue:
        if accounts.getValue(firstCashOnHandAccount, 'Cash/MMKT') >= contributionValue:
            interAccountTransfer(accounts, firstCashOnHandAccount, 'Cash/MMKT', firstAccountWithtype, 'Cash/MMKT', contributionValue)
            print('Funded $' + str(contributionValue) + ' into ' + firstAccountWithtype)
        else:
            print('Not enough cash in first cash on hand account to cover contribution')
    else:
        print('Not enough cash on hand to cover contribution')
