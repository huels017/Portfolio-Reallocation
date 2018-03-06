import unittest
#import sys    # Chris will use this when testing
#sys.path.insert(0, '/home/chris/Desktop/git-repos/Portfolio-Reallocation')   # Chris will use this when testing
from reallocate.utilities import sellFirstCategories
from reallocate.initialize_objects import initializeObjects


class TestReallocateFunctions(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        excelFileLocation = 'test_reallocate.xlsx'
        #excelFileLocation = 'test/test_reallocate.xlsx'    # Chris will use this when testing
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

    '''
    def test_difference_current_desired_allocation(self):
        #list of categories and diff value per category


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
