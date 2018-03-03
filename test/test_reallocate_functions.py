import unittest

from reallocate.initialize_objects import initializeObjects


class TestReallocateFunctions(unittest.TestCase):

    def setUp(self):
        assets_list_start_column = 3 # categories start at the 4th column in excel template
        assets_list_end_column = -1 #don't include the 'total' column
        accounts, fundingRequests, desiredAllocation = initializeObjects('test_reallocate.xlsx', assets_list_start_column, assets_list_end_column)
        self.Accounts = accounts
        self.desiredAllocation = desiredAllocation


    def buySellCategories(self):

        

    def test_difference_current_desired_allocation(self):

    #crypto as commodity
    #Balanced as 50/50 tax bonds/ large cap blend






    def test_find_rules(self):

    #no municiple bonds in Qualified account
    #crypto not bought or sold
    #no Balanced category
    #HSA minHSACash
    #CRIA min



    def test_account_sells(self):
    #if balanced present, sell first
    #if muni bonds in qualified account, sell second
    #else sell per sellCateogies
    #dampening factor
    #maxTaxedSales





    def test_account_buys(self):








if __name__ == '__main__':
    unittest.main()
