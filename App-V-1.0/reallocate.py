from main_functions import findAcctsWithRule, desiredCatTotal, specialRules, accountsCopy, cashOnHand



def reallocate():
    '''
    The Reallocate function will move through a sequence of steps to reallocate
    the portfoilo to the desired allocation.
    '''

    #Create copy of accounts DataContainer
    accounts_copy = accountsCopy()



    ### Define Special Rule Variables ###
    #####################################
    cashOnHandValue = cashOnHand()

    CASH_CAT = "Cash/MMKT"
    desiredCash = desiredCatTotal(CASH_CAT)

    maxTaxedSales, qualifiedContr, minHSACash = specialRules()



    ### Cash on Hand: Special Rules ###
    ###################################

    #use cash on hand to fund 'Needed Qualified Contribution'
    if cashOnHandValue >= qualifiedContr:
        cashOnHandValue -= qualifiedContr
        print 'Move $' + str(qualifiedContr) + ' of cash/MMKT to Qualified account from Cash On Hand'
    else:
        print 'Not enough Cash On Hand to fund Qualified account(s)'



    #if cash on hand is greater then desired cash, fund a NQ accountType
    if cashOnHandValue > desiredCash:
        cashDiff = cashOnHandValue - desiredCash
        #print type(cashDiff)
        print 'Move $' + str(cashDiff) + ' of cash/MMKT to NQ account from Cash On Hand'



    ### Reallocate ###
    ##################

    ### fund qualified accout with cash on hand###



    ###Exempt accounts###
    #Special rule: 'HSA Cash Min'


    ###Deffered accounts###



    ###Cash On Hand###



    ###Non-Qualified accounts###
    #special rule: 'Max Taxed Sales'











    return
reallocate()
