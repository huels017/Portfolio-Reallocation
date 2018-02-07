from main_functions import listOfAccounts, listOfCategories, catValuesList, findAcctsWithRule, desiredCatTotal, specialRules

import pandas as pd

def reallocate():
    '''
    The Reallocate function will move through a sequence of steps to reallocate
    the portfoilo to the desired allocation.
    '''

    #create dataframe which will store all reallocation changes
    CAT_LIST = listOfCategories()
    ACCOUNT_LIST = listOfAccounts()
    reallocation = pd.DataFrame(index=ACCOUNT_LIST, columns=CAT_LIST)

    for cat in CAT_LIST:
        CAT_VALUES_LIST = catValuesList(cat)
        for account in ACCOUNT_LIST:
            reallocation.set_value(account,  cat, CAT_VALUES_LIST[account])




    ### Cash on Hand ###
    ####################
    CASH_CAT = "Cash/MMKT"
    CASH_RULE = "CASH"
    CASH_ON_HAND_ACCOUNTS = findAcctsWithRule(CASH_RULE)

    cashOnHandValue = 0
    for account in CASH_ON_HAND_ACCOUNTS:
        cashOnHandValue += reallocation.get_value(account, CASH_CAT)

    desiredCash = desiredCatTotal(CASH_CAT)


    #Special rule variables defined#
    maxTaxedSales, qualifiedContr, minHSACash = specialRules()



    #Special rule#
    #use cash on hand to fund 'Needed Qualified Contribution'



    #Special rule#
    #if cash on hand is greater then desired cash, fund a NQ accountType
    if cashOnHandValue > desiredCash:
        cashDiff = cashOnHandValue - desiredCash
        print type(cashDiff)
        print 'Move $' + str(float(cashDiff)) + ' of cash/MMKT to NQ account from Cash On Hand'



    ### Reallocate ###
    ##################

    ###Exempt accounts###
    #Special rule: 'HSA Cash Min'


    ###Deffered accounts###



    ###Cash On Hand###



    ###Non-Qualified accounts###
    #special rule: 'Max Taxed Sales'











    return
reallocate()
