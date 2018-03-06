import unittest
import sys
sys.path.append('./')

from reallocate.utilities import sellFirstCategories, categoryTotal, portfolioTotalValue, differenceCurrentDesiredAccounts, categoryCountAs
from reallocate.initialize_objects import initializeObjects


class TestReallocateFunctions(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        excelFileLocation = 'test/test_reallocate.xlsx'
        accounts, fundingRequests, desiredAllocation, categoryRules = initializeObjects(excelFileLocation, assets_list_start_column, assets_list_end_column)
        self.accounts = accounts
        self.desiredAllocation = desiredAllocation
        self.categoryRules = categoryRules


    def test_sell_first_category_sales(self):
        taxedSalesLeft = 5000
        sellFirstCategories(self.accounts, self.categoryRules, taxedSalesLeft)
        self.assertEqual(self.accounts['A10'].get_category_value('Balanced'), 0)


    def test_sell_first_category_cash_funding(self):
        taxedSalesLeft = 5000
        sellFirstCategories(self.accounts, self.categoryRules, taxedSalesLeft)
        self.assertEqual(self.accounts['A10'].get_category_value('Cash/MMKT'), 15000)


    def test_sell_first_category_taxed_sales(self):
        taxedSalesLeft = 5000
        sellFirstCategories(self.accounts, self.categoryRules, taxedSalesLeft)
        self.assertEqual(taxedSalesLeft, 0)


    def test_sell_first_category_taxed_sales_left(self):
        taxedSalesLeft = 6000
        sellFirstCategories(self.accounts, self.categoryRules, taxedSalesLeft)
        self.assertEqual(self.accounts['A13'].get_category_value('Balanced'), 4000)

        #scans through all accounts in group for category with 'sell first' rule, if present sell all of that category.
        #Balanced as 'sell first' and counts as 50/50 tax bonds/ large cap blend( all category diffs go to 0, balanced catorgy = balanced value  )

    def test_category_total(self):
        self.assertEqual(categoryTotal(self.accounts, 'Cash/MMKT'), 112657)

    def test_portfolio_total_value(self):
        self.assertEqual(portfolioTotalValue(self.accounts), 752755.22)

    def test_difference_current_desired_allocation(self):
        expectedDictionary = {u'REIT': 2157.432200000001, u'Muni Bonds': 3443.024899999993, u'Emg Mkts': 46393.18639999999, u'Cryptocurrency': -10000.0, u'Cash/MMKT': -67491.6868, u'Commodities': 1456.4422000000004, u'Sm/Mid Growth': 1887.2531999999992, u'LC Value': 44294.884000000005, u'Tax Bonds': 31047.504899999996, u'LC Growth': -59572.89799999999, u'Balanced': -45000.0, u'International': 85424.29959999998, u'LC Blend': -27601.43800000001, u'Sm/Mid Value': 1162.7927000000018, u'Sm/Mid Blend': -7600.797299999995}
        actualDictionary = differenceCurrentDesiredAccounts(self.accounts, self.desiredAllocation)
        self.assertEqual(actualDictionary, expectedDictionary)
        #list of categories and diff value per category

    def test_category_count_as(self):
        buySellCategories = differenceCurrentDesiredAccounts(self.accounts, self.desiredAllocation)
        categoryCountAs(self.accounts, buySellCategories, self.categoryRules)
        expectedAnswer = {u'REIT': 2157.432200000001, u'Muni Bonds': 3443.024899999993, u'Emg Mkts': 46393.18639999999, u'Cryptocurrency': 0, u'Cash/MMKT': -67491.6868, u'Commodities': 11456.442200000001, u'Sm/Mid Growth': 1887.2531999999992, u'LC Value': 44294.884000000005, u'Tax Bonds': 53547.5049, u'LC Growth': -59572.89799999999, u'Balanced': 0, u'International': 85424.29959999998, u'LC Blend': -5101.438000000009, u'Sm/Mid Value': 1162.7927000000018, u'Sm/Mid Blend': -7600.797299999995}
        self.assertEqual(buySellCategories, expectedAnswer)

    '''
    def test_category_rules(self):
        #crypto as fixed and counts as commodity(crypto category diff = 0, commodity diff -= crypto value )
        #Balanced as 'sell first' and counts as 50/50 tax bonds/ large cap blend( all category diffs go to 0, balanced catorgy = balanced value  )


    def test_account_rules(self):
        #no municiple bonds in Qualified account
        #crypto not bought or sold
        #no Balanced category
        #HSA minHSACash
        #CRIA min


    def buySellCategories(self):


    def test_account_sells(self):
        #if balanced present, sell first
        #if muni bonds in qualified account, sell second
        #else sell per sellCateogies
        #dampening factor
        #maxTaxedSales


    def test_account_buys(self):


    def test_reallocate_accounts(self):


    def test_reallocate_group_accounts(self):
    '''



if __name__ == '__main__':
    unittest.main()
