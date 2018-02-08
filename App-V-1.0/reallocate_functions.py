from main_functions import desiredCatTotal, listOfCategories, findAcctsWithRule, catPrioirtyList


'''
Functions used in the reallocate function
'''



def catValuesList(ACCOUNTS, CAT_NAME):
    '''
    Returns a list of values for each category in an account execpt for the 'Total (pPortfolio)' row
    '''
    return ACCOUNTS.getColumns(CAT_NAME)[0:-1]



def catValueTotal(ACCOUNTS, CAT_NAME):
    '''
    Returns the total value of a single catergory across all accounts
    '''
    cat_values_list = catValuesList(ACCOUNTS, CAT_NAME)
    cat_total_value = 0
    for cat in cat_values_list:
        cat_total_value += cat

    return cat_total_value



def desiredVsRealCatValue(ACCOUNTS, CAT_NAME):
    '''
    returns the difference between the desired category value
    and the real category getValue
    Positive values mean that category should be sold
    '''
    return catValueTotal(ACCOUNTS, CAT_NAME) - desiredCatTotal(CAT_NAME)



def buySellCats(ACCOUNTS):
    '''
    Returns two lists/dicts,
    1) list/dict of categories to buy and value needed to buy to reach desired allocation
    2) list/dict of categoies to sell and value needed to sell to reach desired allocation
    '''
    buy_categories = []
    sell_categories = []

    cat_list = listOfCategories()

    for cat in cat_list:
        sellValue = desiredVsRealCatValue(ACCOUNTS, cat)
        if sellValue > 0:
            sell_categories.append([cat, sellValue])
        elif sellValue <0:
            buy_categories.append([cat, -sellValue])

    return sell_categories, buy_categories



def accountSales(ACCOUNTS, account):  #, RULE, SpecialRules):
    '''
    Sells funds within given account based off buySellCats
    ***Still needed***
        -track total non-cash sales,
        -special rule, stop sales if non-cash sales > max taxed sales, and Rule = "NQ"
        -special rule, if HSA account, stop cash/MMKT sale when cash/MMKT = HSA min
    '''
    sell_categories, buy_categories = buySellCats(ACCOUNTS)
    sales = 0

    for cat in sell_categories:
        smaller_sale = min(cat[1], ACCOUNTS.getValue(account, cat[0]))
        account_cat_value = ACCOUNTS.getValue(account, cat[0]) - smaller_sale
        ACCOUNTS.setValue(account, cat[0], account_cat_value)
        sales += smaller_sale
    return sales



def accountBuys(ACCOUNTS, account, sales):
    '''
    Buys funds within given account based off buySellCats
    '''
    sell_categories, buy_categories = buySellCats(ACCOUNTS)
    cat_priority_list = catPrioirtyList()

    for cat in cat_priority_list:
        for buy_cat in buy_categories:
            if cat == buy_cat[0]:
                smaller_buy = min(buy_cat[1], sales)
                account_cat_value = ACCOUNTS.getValue(account, buy_cat[0]) + smaller_buy
                ACCOUNTS.setValue(account, buy_cat[0], account_cat_value)
                sales -= smaller_buy
    return



def reallocateRuleGroup(ACCOUNTS, RULE):  #, SpecialRules):
    '''
    Reallocates all accounts within one rule group by mondifying the accounts_copy DataContainer
    '''
    accounts_in_rule_group = findAcctsWithRule(RULE)

    for account in accounts_in_rule_group:
        sales = 0
        sales += accountSales(ACCOUNTS, account)
        accountBuys(ACCOUNTS, account, sales)
    return
