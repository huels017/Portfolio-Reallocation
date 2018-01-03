import openpyxl
from pull_functions import number_of_rows, create_list, check_column_names



def pull_allocation_data(excel_name):
    """
    Will load excel workbook
    Find worksheets for account data, desired allocation, and IRA funding statues
    verify that (account_data, desired_allocation, ira_statues) are formated correctly
    assign worksheet data to variables(account_data, desired_allocation, ira_statues)

    return (account_data, desired_allocation, ira_statues)
    #need account names, values per category, desired allocation, ira funding statues

    """

    

    ######################
    #    Pull in Data    #
    ######################

    #load workbook

    #doc = openpyxl.load_workbook('example.xlsx')
    doc = openpyxl.load_workbook(excel_name)
    ###output Error:__ excel file not found if workbook not found.



    #load sheets/tabs

    account_tab = doc.get_sheet_by_name('Accounts')
    desired_allocation_tab = doc.get_sheet_by_name('Desired_Allocation')
    ira_tab = doc.get_sheet_by_name('IRS_Statues')
    ###output Error:__ tab not found if any of 3 tabs are not found.





    ####################
    #    Check Data    #
    ####################

    #confirm account data is formatted correctly 
    # -confirm row of categories is correct
    category_names = [u'Accounts', u'Cash/MMKT', u'Tax Bonds', u'Muni Bonds', u'LC Value', u'LC Growth', u'LC Blend', u'International', u'Emg Mkts', u'Sm/Mid Value', u'Sm/Mid Growth', u'Sm/Mid Blend', u'Commodities', u'REIT', u'Balanced', u'Total']
  
    column_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


    check_column_names(category_names, account_tab, column_labels)

    # -confirm accounts are correct & find # of accounts
    number_of_accounts = number_of_rows(account_tab)

    #################



    #confirm desired allocation is formatted correctly
    # -category names are correct
    


    # -total equals 100%
    number_of_categories = number_of_rows(desired_allocation_tab)


    ##################

    #confirm IRS statues is formatted correctly 
    # -accounts match account_data account names
    # -total does not exceed 5500 per person
    number_of_ira_accounts = number_of_rows(ira_tab)

    ##############################
    #    Assign Data to Lists    #
    ##############################




    #pull data from tabs and assign to lists or variables

    category_labels = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    current_account_values = create_list(number_of_accounts, account_tab, category_labels)




    allocation_labels = ['B']
    desired_allocation = create_list(number_of_categories, desired_allocation_tab, allocation_labels)  


    ira_statues = create_list(number_of_ira_accounts, ira_tab, allocation_labels)


    #max_taxed_sales - need to pull
    max_taxed_sales = 2500


    
    return current_account_values, desired_allocation, ira_statues, max_taxed_sales

#print(pull_allocation_data('Allocation.xlsx')






