from utilities import accountsTotal, findAccountsWithType, fundAccount, condenseAccounts


def fulfillFundingRequests(fundAccounts, fundingRequests, desiredAllocation):
    '''
    Uses cash from cash on hand to fulfill desired funding requests
    '''
    desiredCashValue = desiredAllocation['Cash/MMKT'] * accountsTotal(fundAccounts, fundAccounts)
    cashOnHandAccounts = findAccountsWithType(fundAccounts, 'Cash')

    #Move all Cash on Hand into one account
    firstCashAccount = 0
    condenseAccounts(fundAccounts, cashOnHandAccounts[firstCashAccount], cashOnHandAccounts[firstCashAccount + 1:])


    #fullfill funding requests
    requestNumber = 1
    for request in fundingRequests:

        minimumCashPerRules = 0
        for account in fundAccounts:
            minimumCashPerRules += min(fundAccounts[account].minimum_category_value("Cash/MMKT"), fundAccounts[account].get_category_value("Cash/MMKT"))
        totalCash = accountsTotal(fundAccounts, cashOnHandAccounts) + minimumCashPerRules
        excessCash = totalCash - desiredCashValue
        requestedValue = request[requestNumber]['funding_value']
        fundAccount(fundAccounts, request[requestNumber]['account_name'], cashOnHandAccounts[0], min(requestedValue, excessCash))

        if fundingRequests[-1] == request and requestedValue > excessCash:
            print('Not enough funds for last funding request: ' + str(request[requestNumber]['account_name']) + ' (' + str(fundAccounts[request[requestNumber]['account_name']].account_type) + ') account')

        elif requestedValue > excessCash:
            print('Not enough funds for ' + str(request[requestNumber]['account_name']) + ' (' + str(fundAccounts[request[requestNumber]['account_name']].account_type) + ') account funding request')
        requestNumber += 1
