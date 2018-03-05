import unittest

from reallocate.initialize_objects import initializeObjects
from reallocate.funding import fulfillFundingRequests

class TestFunding(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        currentAccounts, fundingRequests, desiredAllocation, categoryRules = initializeObjects('test_funding.xlsx', assets_list_start_column, assets_list_end_column)
        self.fundAccounts = currentAccounts
        self.fundingRequests = fundingRequests
        self.desiredAllocation = desiredAllocation

    def test_A1_total_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A1_total_value = self.fundAccounts['A1'].get_total_value()
        expected_value = 12
        self.assertEqual(A1_total_value, expected_value)

    def test_A2_total_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A2_total_value = self.fundAccounts['A2'].get_total_value()
        expected_value = 153
        self.assertEqual(A2_total_value, expected_value)

    def test_A3_total_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A3_total_value = self.fundAccounts['A3'].get_total_value()
        expected_value = 35
        self.assertEqual(A3_total_value, expected_value)

    def test_A4_total_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A4_total_value = self.fundAccounts['A4'].get_total_value()
        expected_value = 0
        self.assertEqual(A4_total_value, expected_value)

    def test_A1_cash_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A1_cash_value = self.fundAccounts['A1'].get_category_value('Cash/MMKT')
        expected_value = 12
        self.assertEqual(A1_cash_value, expected_value)

    def test_A2_cash_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A2_cash_value = self.fundAccounts['A2'].get_category_value('Cash/MMKT')
        expected_value = 58
        self.assertEqual(A2_cash_value, expected_value)

    def test_A3_cash_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A3_cash_value = self.fundAccounts['A3'].get_category_value('Cash/MMKT')
        expected_value = 15
        self.assertEqual(A3_cash_value, expected_value)

    def test_A4_cash_value(self):
        fulfillFundingRequests(self.fundAccounts, self.fundingRequests, self.desiredAllocation)
        A4_cash_value = self.fundAccounts['A4'].get_category_value('Cash/MMKT')
        expected_value = 0
        self.assertEqual(A4_cash_value, expected_value)


if __name__ == '__main__':
    unittest.main()
