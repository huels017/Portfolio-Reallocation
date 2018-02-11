import excel_import
import data_container as dc

"""
Functions to determine tax rules, special rules, desired allocation, and general calculations
These should remain static through the reallocation process
Any values that might change should go into the reallocate_functions.py file
Note: depending on how we deal with category special rules, this might need to be futher seperated.
    -the functions might need to be run on accounts_copy instead of accounts if we start grouping categories
"""


#### Import and parse the Excel file: ####
##########################################


EXCEL_FILE_NAME = "../Allocation_Template.xlsx"
EXCEL_HEADER_ROW_INDEX = 0 # This is the row number that has the names of the asset classes (cash, bonds, stock, etc.)
dataframes = excel_import.importExcel(EXCEL_FILE_NAME, EXCEL_HEADER_ROW_INDEX) # Read the Excel file


#### Create DataContainers for Sheets ####
######################################################################

ACCOUNTS_SHEET_NAME = "Accounts"
accounts = dc.DataContainer(dataframes[ACCOUNTS_SHEET_NAME]) # Create a DataContainer for the 'accounts' worksheet


TAX_SHEET = "Tax_Status"
taxSheet = dc.DataContainer(dataframes[TAX_SHEET]) # Create a DataContainer for the 'Tax_Status' worksheet


SPECIAL_RULES_SHEET = "Other_inputs"
specialRulesSheet = dc.DataContainer(dataframes[SPECIAL_RULES_SHEET])


DESIRED_ALLOCATION_SHEET_NAME = "Desired_Allocation"
desiredAllocation = dc.DataContainer(dataframes[DESIRED_ALLOCATION_SHEET_NAME])


def accountsCopy():
    '''
    Return a copy of accounts DataContainer
    The copy will be used to store reallocation changes
    '''
    return dc.DataContainer(dataframes[ACCOUNTS_SHEET_NAME])


#### Functions for Rules and Calculations ####
##############################################

def rulePerAccountType(accountType):
    '''
    Looks at 'Tax_Status' Tab to determine tax rule of an account type
    '''
    CHANGES_COLUMN = "Changes To"
    NQ_COLUMN = "Tax Status"
    DEF_COLUMN = "Def/Exempt"

    if  str(accountType) == "nan":
        return "none"

    if  accountType == "Cash":
        return "CASH"

    elif taxSheet.getValue(accountType, CHANGES_COLUMN) == "N":
        return "FIXED"

    elif taxSheet.getValue(accountType, NQ_COLUMN) == "NQ":
        return "NQ"

    elif taxSheet.getValue(accountType, DEF_COLUMN) == "Exempt":
        return "EXEMPT"

    elif taxSheet.getValue(accountType, DEF_COLUMN) == "Def":
        return "DEF"

    print "Unknown Account Type Found: " + str(accountType)
    return None



def findAccountsWithRule(rule):
    '''
    Returns account names with a desired rule (Exp&Def, Def, Cash, NQ, Fixed)
    '''
    COLUMN_NAME = "Account Type"
    accountNames = accounts.getRowNames()

    ruleAccountList = []

    for account in accountNames:
        accountType = accounts.getValue(account, COLUMN_NAME)

        if rulePerAccountType(str(accountType)) == rule:
            ruleAccountList.append(account)

    return ruleAccountList



def totalPortfolioValue():
    '''
    Returns the value of the entire portfolio
    Note: This assumes the imported excel file calculations are correct.
    This does not confirm the calculation is correct
    '''
    ROW_NAME = "Total (Portfolio)"
    COLUMN_NAME = "Total"
    return accounts.getValue(ROW_NAME,  COLUMN_NAME)



def desiredCategoryTotal(category):
    '''
    Returns the desired total value for a single category
    '''
    COLUMN = "Desired Percent"
    categoryPercent = desiredAllocation.getValue(category,  COLUMN)
    categoryDesiredValue = totalPortfolioValue() * categoryPercent
    return categoryDesiredValue



def specialRules():
    '''
    Returns list of special rule variables (Max Taxed Sales, Needed Qualified Contribution, HSA Cash Min)
    '''
    COLUMN = "Value"
    return specialRulesSheet.getColumns(COLUMN)


#this is static- might need a dynamic category totalizer for reallocate functions
def cashOnHand():
    '''
    Returns the total value of all Cash On Hand accounts
    '''
    COLUMN = "Cash/MMKT"
    CASH_RULE = "CASH"
    cashOnHandAccounts = findAccountsWithRule(CASH_RULE)

    cashOnHandValue = 0
    for account in cashOnHandAccounts:
        cashOnHandValue += accounts.getValue(account, COLUMN)
    return cashOnHandValue



def listOfCategories():
    '''
    Returns a list of categories (excludes Owner, Institution, and Account Type Columns)
    '''
    return accounts.getHeaderNames()[3:-1]



def categoryPriorityList():
    '''
    Returns a list of categories in order of which category benifits most
    from being in a qualified account
    '''
    categoryList = listOfCategories()
    COLUMN = "Ranking starting with best in tax exempt "
    categoryPriorityList = []

    for category in categoryList:
        categoryPriorityList.append('')

    for category in categoryList:
        categoryPriority = desiredAllocation.getValue(category,  COLUMN)
        categoryPriorityList[int(categoryPriority)-1] = category

    return categoryPriorityList



def listOfAccounts():
    '''
    Returns a list of Accounts (excludes Total(Portfolio) row)
    Should I instead have it look for 'total' in the text name? I could pull the full 'accounts.getRowNames()', then iterate through each name to check if 'total' is found. If total is found then I wont include it in the returned list.
    '''
    return accounts.getRowNames()[0:-1]
