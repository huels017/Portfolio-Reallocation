
import openpyxl



def pull_all_tabs(workbook, tabs):
    '''
    Pulls sheet/tabs from workbook for all tabs in tabs list.
    Sheets are appended to sheet name in globel 'expected_tabs' (list of lists). 
    '''
    i = 0
    for tab in tabs:
        tabs[i].append(workbook.get_sheet_by_name(tab[0]))    
        i += 1
    return 



def count_rows_in_tab(tab):
    '''
    counting the number of rows between the column title and total or first blank space 
    returns number of rows
    max of 200 rows can be found
    '''
    count = 0
    while True:
        count +=1
        if count == 203:
            print('Error: More than 200 rows found')
            return
        elif (tab[('A' + str(count))].value == 'Total') or (tab[('A' + str(count))].value == None) or (tab[('A' + str(count))].value == 'Total (Portfolio)'):
            number_of_rows = count - 3 #1 for header, 1 for column labels, 1 for row total label
            print(str(tab['A2'].value) + ' rows found: ' + str(number_of_rows))
            
            break
 
    return number_of_rows



def count_columns_in_tab(tab):
    '''
    counting the number of columns between the first column and total or first blank space 
    returns number of columns
    max of 25 rows can be found
    '''
    column_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    count = -1
    while count <= 25:
        count +=1

        if count == 26:
            print('Error: More than 25 columns found')
            return

        elif (tab[(column_labels[count] + str(2))].value == 'Total') or (tab[(column_labels[count] + str(2))].value == None):
            print(str(tab['A2'].value) + ' columns found: ' + str(count))
            number_of_columns = count #1 for header, 1 for column labels, 1 for row total label
            break

    return number_of_columns



def tabs_to_dict(tabs):
    '''
    Create dictionarys of data pulled from tabs withing the expected_tab dictionary of tabs
    '''
    dict = []
    column_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for tab in tabs:
        num_columns = count_columns_in_tab(tab[1])
        num_rows = count_rows_in_tab(tab[1])
        tab.append([])
        i = 0
        while i < num_rows:
            tab[2].append([])
            count = 0
            while count < num_columns:
                tab[2][-1].append(tab[1][column_labels[count] + str(i+3)].value)
                count += 1
            i += 1
        #print(tab)

    print('All tabs data loaded into expected_tabs dictionaries')
    return dict 


def account_info_to_dict(account_list):
    '''
    Hard coded where to find first 4 items of account_lifo list. 
    '''
    return account_list[0], account_list[1], account_list[2], account_list[3]


def account_tax_info_to_dict(account_list):
    '''
    Hard coded- matches account type with tax statues and rules. 
    '''
    account_type = account_list[3]

    if (account_type == 'Roth 401(k)') or (account_type == 'Roth IRA') or (account_type == 'H.S.A'):
        return 'Q', 'Exempt', 'Y' 
   
    elif (account_type == '401(k)') or (account_type == '403(b)') or (account_type == 'Trad IRA') or (account_type == 'Non-Ded IRA') or (account_type == 'Roll IRA') or (account_type == 'SIMPLE IRA') or (account_type == 'SEP IRA') or (account_type == 'Solo(k)') or (account_type == 'Def Comp') or (account_type == 'Def Cont. Plan') or (account_type == 'Var. Life') or (account_type == 'Var. Annuity'):
            return 'Q', 'Def', 'Y'

    elif (account_type == 'Pension') or (account_type == 'Cash Bal. Plan') or (account_type == 'Cash Value') or (account_type == 'Fix Annuity'):
           return 'Q', 'Def', 'N'

    elif (account_type == 'Brokerage') or (account_type == 'Cash'):
         return 'NQ', 'N/A', 'Y'

    elif (account_type == "RSU's") or (account_type == 'Pref. Equity') or (account_type == 'Real Estate') or (account_type == 'Ltd Ptnr'):
         return 'NQ', 'N/A', 'N'

    print('Account type not found for: #' + str(account_list[0]))
    return 





def account_data_to_dict(account):
    '''
    returns category values from account list
    '''
    return account[4:] ###here was a change!!!!!! [4:-1] Seems ok at the moment


def create_account_dict(expected_tabs,account_info, category_names):
    '''
    pull account values per category
    pull rules and tax information per account
    
    '''
    current_accounts = []
  
    #populate account info into current_accounts
    for account in expected_tabs[0][2]:
        spot1, spot2, spot3, spot4 = account_info_to_dict(account)
        spot5, spot6, spot7 = account_tax_info_to_dict(account)
        current_accounts.append([[spot1, spot2, spot3, spot4, spot5, spot6, spot7]])
    
    #populate account data into current accounts

    i = 0
    for account in expected_tabs[0][2]:
        current_accounts[i].append(account_data_to_dict(account))
        #print(account)
        #print(current_accounts[i])
        i += 1
        
    print('Accounts data loaded into organized dictionary')
    return current_accounts 





##################
####Start Here####
##################





# this dictionary will record changes per reallocation suggestions 

'''


def find_column_names(dict_name)
    return list

def find_row_names(dict_name)
    return list

def verify_list_names(true_list, list_name)
    return True/False

#verify
# - tabs, columns for all tabs, rows for all tabs, 
# return errors to find issue

def count_list_items(list)




create a mutable dictionary that doesn't change orginail- call current_accounts

def find_rules_for_accounts(account_dict, tax_dict):
    return
'''


#######################################
##Old Delete all below when replaced###
#######################################

def number_of_rows(tab):
    '''
    counting the number of rows between the column title and total 
    returns number of rows
    '''
    count = 0
    while count <= 203:
        count +=1
        if tab[('A' + str(count))].value == '':
            print('Error: blank space found were account name is expected')

        elif count == 203:
            print('Error: Total not found or more than 200 accounts or asset categories')

        elif tab[('A' + str(count))].value == 'Total':
            print('Total found.', (count-3),  tab['A2'].value)
            number_of_accounts = count - 3 #1 for header, 1 for column labels, 1 for row total label
            break
 
    return count-3



def create_list(number_of,tab,column_labels):
    '''
    #can be used for both accounts and categories
    '''

    portfolio = []
    count = 0
    while count < number_of:
        portfolio.append([[tab[('A' + str(count+3))].value]])
        portfolio[-1].append([])

        for category in column_labels:
            portfolio[-1][1].append(tab[(category + str(count+3))].value)    
        count += 1

    return portfolio



def check_column_names(column_real_names, tab, labels):
    '''

    '''

    column_names = []

    for letter in labels:
        column_names.append(tab[letter + str(2)].value)

    if column_real_names == column_names:
        print('column names correct')
    else:
        print('Error: column names are not correct')

    return

