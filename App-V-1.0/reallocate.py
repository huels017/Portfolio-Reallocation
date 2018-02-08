from main_functions import findAcctsWithRule, desiredCatTotal, specialRules, accountsCopy, cashOnHand
from reallocate_functions import reallocateRuleGroup, accountSales, buySellCats


def reallocate():
    '''
    The Reallocate function will move through a sequence of steps to reallocate
    the portfoilo to the desired allocation.
    '''

    #Create copy of accounts DataContainer
    accounts_copy = accountsCopy()
    ACCOUNTS = accounts_copy


    ### Define Special Rule Variables ###
    #####################################
    cashOnHandValue = cashOnHand()

    CASH_CAT = "Cash/MMKT"
    desiredCash = desiredCatTotal(CASH_CAT)

    maxTaxedSales, qualifiedContrValue, minHSACash = specialRules()



    ### Cash on Hand: Special Rules ###
    ###################################

    #use cash on hand to fund 'Needed Qualified Contribution'
    if cashOnHandValue >= qualifiedContrValue:
        cashOnHandValue -= qualifiedContrValue
        qualifiedContr = True
        print 'Move $' + str(qualifiedContrValue) + ' of cash/MMKT to Qualified account from Cash On Hand'
    else:
        qualifiedContr = False
        print 'Not enough Cash On Hand to fund Qualified account(s)'



    #if cash on hand is greater then desired cash, fund a NQ accountType
    if cashOnHandValue > desiredCash:
        cashDiff = cashOnHandValue - desiredCash
        #print type(cashDiff)
        print 'Move $' + str(cashDiff) + ' of cash/MMKT to NQ account from Cash On Hand'



    ### Reallocate ###
    ##################

    ### fund qualified account with cash on hand###



    ###Exempt accounts###
    #Special rule: 'HSA Cash Min'
    RULE = "EXEMPT"
    reallocateRuleGroup(ACCOUNTS, RULE)



    ###Deffered accounts###
    RULE = "DEF"
    reallocateRuleGroup(ACCOUNTS, RULE)


    ###Cash On Hand###
    RULE = "CASH"
    reallocateRuleGroup(ACCOUNTS, RULE)


    ###Non-Qualified accounts###
    #special rule: 'Max Taxed Sales'
    RULE = "NQ"
    reallocateRuleGroup(ACCOUNTS, RULE)




    return accounts_copy
reallocate()
