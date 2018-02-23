from main_functions import desiredCategoryTotal, specialRules, accountsCopy, cashOnHand
from reallocate_functions import reallocateRuleGroup, accountSales, interAccountTransfer, fundAccount


def reallocate():
    '''
    The Reallocate function will move through a sequence of steps to reallocate
    the portfoilo to the desired allocation.
    '''

    #Create copy of accounts DataContainer
    reallocatedAccounts = accountsCopy()



    ### Define Special Rule Variables ###
    #####################################
    cashOnHandValue = cashOnHand()

    CASH_CATEGORY = "Cash/MMKT"
    desiredCash = desiredCategoryTotal(CASH_CATEGORY)

    maxTaxedSales, minHSACash, IRAContribution = specialRules()



    ### Cash on Hand: Special Rules ###
    ###################################

    #use cash on hand to fund IRA Contribution
    accountType = 'Roth IRA'
    fundAccount(reallocatedAccounts, accountType, IRAContribution)



    #if cash on hand is greater then desired cash, fund a NQ accountType
    #Currently does not consider HSA cash min, or other cash sources
    cashOnHandValue = cashOnHand()
    if cashOnHandValue > desiredCash:
        extraCash = cashOnHandValue - desiredCash
        accountType = 'Brokerage'
        fundAccount(reallocatedAccounts, accountType, extraCash)


    ### Reallocate ###
    ##################

    ### fund qualified account with cash on hand###

    #Special rule: 'HSA Cash Min'
    RULE = 'HSA'
    reallocateRuleGroup(reallocatedAccounts, RULE)


    ###Exempt accounts###
    RULE = "EXEMPT"
    reallocateRuleGroup(reallocatedAccounts, RULE)



    ###Deffered accounts###
    RULE = "DEF"
    reallocateRuleGroup(reallocatedAccounts, RULE)



    ###Non-Qualified accounts###
    #special rule: 'Max Taxed Sales'
    RULE = "NQ"
    reallocateRuleGroup(reallocatedAccounts, RULE)




    return reallocatedAccounts
#reallocate()
