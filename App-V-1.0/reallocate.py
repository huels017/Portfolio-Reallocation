from main_functions import desiredCategoryTotal, specialRules, accountsCopy, cashOnHand
from reallocate_functions import reallocateRuleGroup, accountSales, interAccountTransfer


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

    maxTaxedSales, qualifiedContrabutionValue, minHSACash = specialRules()



    ### Cash on Hand: Special Rules ###
    ###################################

    #use cash on hand to fund 'Needed Qualified Contribution'
    if cashOnHandValue >= qualifiedContrabutionValue:
        cashOnHandValue -= qualifiedContrabutionValue
        qualifiedContrabution = True
        print 'Move $' + str(qualifiedContrabutionValue) + ' of cash/MMKT to Qualified account from Cash On Hand'
    else:
        qualifiedContrabution = False
        print 'Not enough Cash On Hand to fund Qualified account(s)'





    #if cash on hand is greater then desired cash, fund a NQ accountType
    if cashOnHandValue > desiredCash:
        extraCash = cashOnHandValue - desiredCash
        print 'Move $' + str(extraCash) + ' of cash/MMKT to NQ account from Cash On Hand'



    ### Reallocate ###
    ##################

    ### fund qualified account with cash on hand###



    ###Exempt accounts###
    #Special rule: 'HSA Cash Min'
    RULE = "EXEMPT"
    reallocateRuleGroup(reallocatedAccounts, RULE)



    ###Deffered accounts###
    RULE = "DEF"
    reallocateRuleGroup(reallocatedAccounts, RULE)


    ###Cash On Hand###
    RULE = "CASH"
    reallocateRuleGroup(reallocatedAccounts, RULE)


    ###Non-Qualified accounts###
    #special rule: 'Max Taxed Sales'
    RULE = "NQ"
    reallocateRuleGroup(reallocatedAccounts, RULE)




    return reallocatedAccounts
#reallocate()
