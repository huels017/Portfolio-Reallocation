import unittest
from reallocate.initialize_objects import initializeObjects
from reallocate.utilities import accountsTotal, findAccountsWithType, fundAccount, condenseAccounts

class TestUtilities(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        currentAccounts, fundingRequests, desiredAllocation = initializeObjects('test_funding.xlsx', assets_list_start_column, assets_list_end_column)
        self.accounts = currentAccounts
        self.fundingRequests = fundingRequests
        self.desiredAllocation = desiredAllocation

    def test_accounts_total(self):
        accountsList = ['A1', 'A2', 'A3', 'A4']
        total_accounts_value = accountsTotal(self.accounts, accountsList)
        expected_value = 200
        self.assertEqual(total_accounts_value, expected_value)


    def test_find_accounts_with_type(self):
        accounts_with_type = findAccountsWithType(self.accounts, 'Cash')
        self.assertEqual(accounts_with_type, [self.accounts['A1'], self.accounts['A4']])


    def test_fund_account_withdraw(self):
        fund_value = 5
        fundAccount(self.accounts['A1'], self.accounts['A4'], fund_value)
        expected_value = 15
        self.assertEqual(self.accounts['A4'].get_category_value('Cash/MMKT'), expected_value)

    def test_fund_account_fund(self):
        fund_value = 10
        fundAccount(self.accounts['A1'], self.accounts['A4'], 10)
        expected_value = 60
        self.assertEqual(self.accounts['A1'].get_category_value('Cash/MMKT'), expected_value)

    def test_condense_accounts_fill(self):
        accounts_to_empty = [self.accounts['A2'], self.accounts['A3'], self.accounts['A4']]
        condenseAccounts(self.accounts['A1'], accounts_to_empty)
        expected_value = 200
        self.assertEqual(self.accounts['A1'].get_category_value('Cash/MMKT'), expected_value)

    def test_condense_accounts_empty(self):
        accounts_to_empty = [self.accounts['A2'], self.accounts['A3'], self.accounts['A4']]
        condenseAccounts(self.accounts['A1'], accounts_to_empty)
        expected_value = 0
        self.assertEqual(self.accounts['A3'].get_category_value('Cash/MMKT'), expected_value)

if __name__ == '__main__':
    unittest.main()
