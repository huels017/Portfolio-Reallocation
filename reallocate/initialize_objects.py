import excel_import
import data_container as dc
import account as ac
import funding_request as fr

'''
Functions to initialize all objects.
'''
def initializeObjects(excelFileName, assets_list_start_column, assets_list_end_column):
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

    FUNDING_REQUEST_SHEET_NAME = "Fund_Accounts"
    fundingRequestSheet = dc.DataContainer(dataframes[FUNDING_REQUEST_SHEET_NAME])

    TAX_SHEET = "Tax_Status"
    taxSheet = dc.DataContainer(dataframes[TAX_SHEET]) # Create a DataContainer for the 'Tax_Status' worksheet

    SPECIAL_RULES_SHEET = "Other_inputs"
    specialRulesSheet = dc.DataContainer(dataframes[SPECIAL_RULES_SHEET])

    DESIRED_ALLOCATION_SHEET_NAME = "Desired_Allocation"
    desiredAllocation = dc.DataContainer(dataframes[DESIRED_ALLOCATION_SHEET_NAME])



    #### Create Account class Objects for currentAccounts Object ####
    ######################################################################
    categoryList = currentAccounts.getHeaderNames()[assets_list_start_column:assets_list_end_column]
    accounts = {}

    for account in currentAccounts.getRowNames():
        owner = currentAccounts.getValue(account, 'Owner')
        institution = currentAccounts.getValue(account, 'Institution')
        account_type = currentAccounts.getValue(account, 'Account Type')
        assets = {}
        for category in categoryList:
            assets[category] = currentAccounts.getValue(account, category)
        accounts[account] = ac.Account(owner, institution, account_type, assets)



    #### Create a List of Funding Request Objects ###
    #################################################
    fundingRequest = []

    for row in fundingRequestSheet.getRowNames():
        fundingRequest.append(fr.FundingRequest(fundingRequestSheet.getValue(row, 'Account to Fund'), fundingRequestSheet.getValue(row, 'Amount to Fund')))



    return accounts, fundingRequest
