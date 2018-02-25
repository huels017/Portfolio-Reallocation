import excel_import
import data_container as dc
import account as ac

'''
Functions to initialize all objects.
'''
def initializeObjects(excelFileName):
    '''
    Returns all objects needed for reallocation program
    '''

    #### Import and parse the Excel file: ####
    ##########################################


    EXCEL_FILE_NAME = excelFileName
    EXCEL_HEADER_ROW_INDEX = 0 # This is the row number that has the names of the asset classes (cash, bonds, stock, etc.)
    dataframes = excel_import.importExcel(EXCEL_FILE_NAME, EXCEL_HEADER_ROW_INDEX) # Read the Excel file



    #### Create DataContainers for Sheets ####
    ######################################################################

    ACCOUNTS_SHEET_NAME = "Accounts"
    currentAccounts = dc.DataContainer(dataframes[ACCOUNTS_SHEET_NAME]) # Create a DataContainer for the 'accounts' worksheet
    
    TAX_SHEET = "Tax_Status"
    taxSheet = dc.DataContainer(dataframes[TAX_SHEET]) # Create a DataContainer for the 'Tax_Status' worksheet


    SPECIAL_RULES_SHEET = "Other_inputs"
    specialRulesSheet = dc.DataContainer(dataframes[SPECIAL_RULES_SHEET])

    DESIRED_ALLOCATION_SHEET_NAME = "Desired_Allocation"
    desiredAllocation = dc.DataContainer(dataframes[DESIRED_ALLOCATION_SHEET_NAME])



    #### Create Account class Objects for currentAccounts Object ####
    ######################################################################

    #Need a better way to find category list without hard coding placement
    categoryList = currentAccounts.getHeaderNames()[3:-1]

    currentAccountsDictionary = {}
    accountsList = currentAccounts.getRowNames()

    for account in accountsList:
        owner = currentAccounts.getValue(account, 'Owner')
        institution = currentAccounts.getValue(account, 'Institution')
        account_type = currentAccounts.getValue(account, 'Account Type')
        assets = {}
        for category in categoryList:
            assets[category] = currentAccounts.getValue(account, category)
        accountObject = ac.Account(owner, institution, account_type, assets)
        currentAccountsDictionary[account] = accountObject

    return currentAccountsDictionary
