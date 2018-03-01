from utilities import accountsTotal, findAccountsWithType, fundAccount, condenseAccounts


def fulfillFundingRequests(fundAccounts, fundingRequest, desiredAllocation):
    '''
    Uses cash from cash on hand to fulfill desired funding requests
    '''
    desiredCashValue = desiredAllocation['Cash/MMKT'] * accountsTotal(fundAccounts, fundAccounts)
    cashOnHandAccounts = findAccountsWithType(fundAccounts, 'Cash')

    #Move all Cash on Hand into one account
    firstCashAccount = 0
    condenseAccounts(fundAccounts, cashOnHandAccounts[firstCashAccount], cashOnHandAccounts[firstCashAccount + 1:])


    #fullfill funding requests
    for request in fundingRequest:
        totalCash = accountsTotal(fundAccounts, cashOnHandAccounts)#need a way to scan through accounts minimun cash value using rules class
        excessCash = totalCash - desiredCashValue
        requestedValue = request.fundingValue
        fundAccount(fundAccounts, request.account, cashOnHandAccounts[0], min(requestedValue, excessCash))

        if fundingRequest[-1] == request and requestedValue > excessCash:
            print('Not enough funds for last funding request: ' + str(request.account) + ' (' + str(fundAccounts[request.account].account_type) + ') account')

        elif requestedValue > excessCash:
            print('Not enough funds for ' + str(request.account) + ' (' + str(fundAccounts[request.account].account_type) + ') account funding request')
