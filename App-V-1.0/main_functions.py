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


#### Create DataContainers for Sheets that will be referenced >1: #### 
######################################################################

ACCOUNTS_SHEET_NAME = "Accounts"
accounts = dc.DataContainer(dataframes[ACCOUNTS_SHEET_NAME]) # Create a DataContainer for the 'accounts' worksheet




#### Functions for Rules and Calculations ####
##############################################

def RulePerAccountType(ACCOUNT_TYPE):
    '''
    Looks at 'Tax_Status' Tab to determine tax rule of an account type
    '''
    TAX_SHEET = "Tax_Status"
    taxSheet = dc.DataContainer(dataframes[TAX_SHEET]) # Create a DataContainer for the 'Tax_Status' worksheet
    
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





























