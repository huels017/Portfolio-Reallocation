import openpyxl
from pull_functions_2 import pull_all_tabs, tabs_to_dict, count_rows_in_tab, count_columns_in_tab, create_account_dict
#delete from import below when replaced
from pull_functions_2 import number_of_rows, create_list, check_column_names


expected_tabs = [['Accounts'], ['Categories'], ['IRA_Statues'], ['Tax_Statues'], ['Other_inputs']]

account_info = ['Account_number', 'Owner', 'Institution', 'Account Type', 'tax status', 'Def/Exempt', 'Changes To']
#inside pull_functions_2/def account_info_to_dict, it is hardcoded for first 4 items in account_info
#tax statues and rules groups are hard coded in pull_functions_2/def account_tax_info_to_dict
#category locations hard coded in pull_functions_2.pu/account_data_to_dict

category_names = [u'Accounts', u'Cash/MMKT', u'Tax Bonds', u'Muni Bonds', u'LC Value', u'LC Growth', u'LC Blend', u'International', u'Emg Mkts', u'Sm/Mid Value', u'Sm/Mid Growth', u'Sm/Mid Blend', u'Commodities', u'REIT', u'Balanced', u'Total']
#need to scan for these or fix excel template


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
    while True:
        try: 

            workbook = openpyxl.load_workbook(excel_name)
            print('Workbook loaded succesfully.')
            break
        except (IOError):
            print('File not found. Check file name.')
            return


    #load sheets/tabs from workbook
    while True:
        try:
            pull_all_tabs(workbook, expected_tabs)
            print('Tabs found and loaded')
            break
        except (KeyError):
            print('Tabs not found. Check tab names.')
            return

    
    #assign tabs to dictionarys
    tabs_to_dict(expected_tabs)

    



    ##################
    ####Start Here####          ########################################
    ##################





    ####################
    #    Check Data    #
    ####################

    #verify column names for all sheets
    #-need lists of expected column names for all tabs


    #verify row names for all sheets
    #-need lists of expected row names for all tabs







    #######################################
    ##Old Delete all below when replaced###
    #######################################
    #check_column_names(category_names, account_tab, column_labels)

    # -confirm accounts are correct & find # of accounts
    #number_of_accounts = number_of_rows(account_tab)

    #################

    #confirm desired allocation is formatted correctly
    # -category names are correct
    


    # -total equals 100%
    #number_of_categories = number_of_rows(desired_allocation_tab)
    number_of_categories = 14

    ##################

    #confirm IRS statues is formatted correctly 
    # -accounts match account_data account names
    # -total does not exceed 5500 per person
    ira_tab = expected_tabs[2][1]
    number_of_ira_accounts = number_of_rows(ira_tab)
    #######################################
    ##Old Delete all above when replaced###
    #######################################









    ##############################
    #    Assign Data to Lists    #
    ##############################

    # populate 'current_accounts' dict with relevant data 

    current_accounts = create_account_dict(expected_tabs, account_info, category_names)
    #print(current_accounts)


    #IRA info



    #Max taxed transaction info



    #desired allocation info


    #######################################
    ##Old Delete all below when replaced###
    #######################################
    #pull data from tabs and assign to lists or variables

    #category_labels = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    #current_account_values = create_list(number_of_accounts, account_tab, category_labels)



    category_tab = expected_tabs[1][1]
    allocation_labels = ['B']
    desired_allocation = create_list(number_of_categories, category_tab, allocation_labels)  


    #ira_statues = create_list(number_of_ira_accounts, ira_tab, allocation_labels)
    ira_statues = create_list(number_of_ira_accounts, ira_tab, allocation_labels)

    #max_taxed_sales - need to pull
    max_taxed_sales = 2500
    #######################################
    ##Old Delete all above when replaced###
    #######################################
    
    
    return current_accounts, desired_allocation, ira_statues, max_taxed_sales

#print(pull_allocation_data('Allocation.xlsx')






