

class FundingRequest(object):
    ''' Represents a request to fund an account.
    '''

    def __init__(self, account, fundingValue):
        ''' Create a funding request

        Args:
            account (string): The account to receive funding
            fundingValue (int): The value to be funded
        '''
        self.account = account
        self.fundingValue = fundingValue
