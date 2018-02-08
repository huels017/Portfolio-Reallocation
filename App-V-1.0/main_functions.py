import excel_import
import data_container as dc

"""
Functions to determine tax rules, special rules, desired allocation, and general calculations
These should remain static through the reallocation process
Anything values that might change should go into the reallocate_functions.py file
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

def RulePerAccountType(ACCOUNT_TYPE):
    '''
    Looks at 'Tax_Status' Tab to determine tax rule of an account type
    '''
    CHANGES = "Changes To"
    NQ = "Tax Status"
    DEF = "Def/Exempt"

    if  str(ACCOUNT_TYPE) == "nan":
        return "none"

    if  ACCOUNT_TYPE == "Cash":
        return "CASH"

    elif taxSheet.getValue(ACCOUNT_TYPE, CHANGES) == "N":
        return "FIXED"

    elif taxSheet.getValue(ACCOUNT_TYPE, NQ) == "NQ":
        return "NQ"

    elif taxSheet.getValue(ACCOUNT_TYPE, DEF) == "Exempt":
        return "EXEMPT"

    elif taxSheet.getValue(ACCOUNT_TYPE, DEF) == "Def":
        return "DEF"

    return "Account Type Unknown"



def findAcctsWithRule(RULE):
    '''
    Returns account names with a desired rule (Exp&Def, Def, Cash, NQ, Fixed)
    '''
    ACCOUNT_TYPE = "Account Type"
    accountNames = accounts.getRowNames()

    ruleAccountList = []

    for account in accountNames:
        accountType = accounts.getValue(account, ACCOUNT_TYPE)

        if RulePerAccountType(str(accountType)) == RULE:
            ruleAccountList.append(account)

    return ruleAccountList



def totalPortfolioValue():
    '''
    Returns the value of the entire portfolio
    '''
    ACCOUNT_NAME = "Total (Portfolio)"
    ASSET_TYPE = "Total"
    return accounts.getValue(ACCOUNT_NAME,  ASSET_TYPE)



def desiredCatTotal(CATEGORY):
    '''
    Returns the desired total value for a single category
    '''
    CATEGORY_NAME = CATEGORY
    COLUMN = "Desired Percent"
    catPercent = desiredAllocation.getValue(CATEGORY_NAME,  COLUMN)
    catDesiredValue = totalPortfolioValue() * catPercent
    return catDesiredValue



def specialRules():
    '''
    Returns list of special rule variables (Max Taxed Sales, Needed Qualified Contribution, HSA Cash Min)
    '''
    COLUMN = "Value"
    return specialRulesSheet.getColumns(COLUMN)


#this is static- might need a dynamic category totalizer for reallocate functions
def cashOnHand():
    '''
    Returns the total value of all Cash On Hand acounts
    '''
    CASH_CAT = "Cash/MMKT"
    CASH_RULE = "CASH"
    CASH_ON_HAND_ACCOUNTS = findAcctsWithRule(CASH_RULE)

    cashOnHandValue = 0
    for account in CASH_ON_HAND_ACCOUNTS:
        cashOnHandValue += accounts.getValue(account, CASH_CAT)
    return cashOnHandValue



def listOfCategories():
    '''
    Returns a list of categories (excludes Owner, Institution, and Account Type Columns)
    '''
    return accounts.getHeaderNames()[3:-1]



def catPrioirtyList():
    '''
    Returns a list of categories in order of which category benifits most
    from being in a qualified account
    '''
    CATEGORY_LIST = listOfCategories()
    COLUMN = "Ranking starting with best in tax exempt "
    CAT_PRIORITY_LIST = []

    for cat in CATEGORY_LIST:
        CAT_PRIORITY_LIST.append('')

    for cat in CATEGORY_LIST:
        catPriority = desiredAllocation.getValue(cat,  COLUMN)
        CAT_PRIORITY_LIST[int(catPriority)-1] = cat

    return CAT_PRIORITY_LIST




#### Not sure which of these are even needed now that accounts_copy is available
### CSH made these when creating a dataframe without using the DataContainer
### Will delete anything below that is not referenced after reallocate.py is working


def listOfAccounts():
    '''
    Returns a list of Accounts (excludes Total(Portfolio) row)
    '''
    return accounts.getRowNames()[0:-1]
