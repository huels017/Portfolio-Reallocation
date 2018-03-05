import unittest

from reallocate.initialize_objects import initializeObjects


class TestReallocateFunctions(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        accounts, fundingRequests, desiredAllocation = initializeObjects('test_reallocate.xlsx', assets_list_start_column, assets_list_end_column)
        self.Accounts = accounts
        self.desiredAllocation = desiredAllocation



    def test_sell_first_scan(self):
        #scans through all accounts in group for category with 'sell first' rule, if present sell all of that category.
        #Balanced as 'sell first' and counts as 50/50 tax bonds/ large cap blend( all category diffs go to 0, balanced catorgy = balanced value  )


    def test_difference_current_desired_allocation(self):
        #list of categories and diff value per category


    def test_category_rules
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




if __name__ == '__main__':
unittest.main()
