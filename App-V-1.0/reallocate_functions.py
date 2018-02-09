from main_functions import desiredCategoryTotal, listOfCategories, findAccountsWithRule, categoryPriorityList


'''
Functions used in the reallocate function
'''



def categoyValuesList(accounts, catergory):
    '''
    Returns a list of values for each category in an account execpt for the 'Total (pPortfolio)' row
    '''
    return accounts.getColumns(catergory)[0:-1]



def categoryValueTotal(accounts, catergory):
    '''
    Returns the total value of a single catergory across all accounts
    '''
    categoryValuesList = categoyValuesList(accounts, catergory)
    categoryTotalValue = 0
    for category in categoryValuesList:
        categoryTotalValue += category

    return categoryTotalValue



def desiredVsRealCategoryValue(accounts, catergory):
    '''
    returns the difference between the desired category value
    and the real category getValue
    Positive values mean that the category should be sold
    Negitive values mean that the category should be bought
    The +/- will be used in 'buySellCategories' to split categories into buy and sell groups
    '''
    return categoryValueTotal(accounts, catergory) - desiredCategoryTotal(catergory)



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

    for catergory in sellCategories:
        smallerSale = min(catergory[1], accounts.getValue(account, catergory[0]))
        accountCategoryValue = accounts.getValue(account, catergory[0]) - smallerSale
        accounts.setValue(account, catergory[0], accountCategoryValue)
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
    return



def reallocateRuleGroup(accounts, rule):  #, SpecialRules):
    '''
    Reallocates all accounts within one rule group by mondifying the accounts_copy DataContainer
    '''
    accountsInRuleGroup = findAccountsWithRule(rule)

    for account in accountsInRuleGroup:
        sales = 0
        sales += accountSales(accounts, account)
        accountBuys(accounts, account, sales)
    return
