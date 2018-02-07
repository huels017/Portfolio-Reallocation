import excel_import
import data_container as dc

"""
Functions to determine tax rules, special rules, desired allocation, and general calculations
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

def catTotal(CATEGORY):
    '''
    Returns the original total value for a single category
    '''
    ACCOUNT_NAME = "Total (Portfolio)"
    ASSET_TYPE = CATEGORY
    return accounts.getValue(ACCOUNT_NAME,  ASSET_TYPE)




def desiredVsRealCatValue(CATEGORY):
    '''
    returns the difference between the desired category value
    and the real category getValue

    '''
    return desiredCatTotal(CATEGORY) - catTotal(CATEGORY)




def listOfAccounts():
    '''
    Returns a list of Accounts (excludes Total(Portfolio) row)
    '''
    return accounts.getRowNames()[0:-1]


def listOfCategories():
    '''
    Returns a list of categories (excludes Owner, Institution, and Account Type Columns)
    '''
    return accounts.getHeaderNames()[3:-1]

def catValuesList(CAT_NAME):
    '''
    Returns a list of values for each category in an account execpt for the 'Total (pPortfolio)' row
    '''
    return accounts.getColumns(CAT_NAME)[0:-1]



def specialRules():
    '''
    Returns list of special rule variables (Max Taxed Sales, Needed Qualified Contribution, HSA Cash Min)
    '''
    COLUMN = "Value"
    return specialRulesSheet.getColumns(COLUMN)
