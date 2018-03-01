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

    ACCOUNT_MIN_MAX_SHEET_NAME = "Account_Min_Max"
    accountMinMax = dc.DataContainer(dataframes[ACCOUNT_MIN_MAX_SHEET_NAME])

    #TAX_SHEET = "Tax_Status"
    #taxSheet = dc.DataContainer(dataframes[TAX_SHEET]) # Create a DataContainer for the 'Tax_Status' worksheet

    #SPECIAL_RULES_SHEET = "Other_inputs"
    #specialRulesSheet = dc.DataContainer(dataframes[SPECIAL_RULES_SHEET])

    DESIRED_ALLOCATION_SHEET_NAME = "Desired_Allocation"
    desiredAllocationsheet = dc.DataContainer(dataframes[DESIRED_ALLOCATION_SHEET_NAME])



    #### Create a dictionary of Rules ####
    ######################################
    rules = {}
    for account in currentAccounts.getRowNames():
        rules[account] = {}

    for account in accountMinMax.getRowNames():
        for rule in accountMinMax.getHeaderNames()[1:5]:
            if str(accountMinMax.getValue(account, rule)) != 'nan':
                rules[account][rule] = {'category': accountMinMax.getValue(account, accountMinMax.getHeaderNames()[0]), 'value': accountMinMax.getValue(account, rule)}



    #### Create Account class Objects for currentAccounts Object ####
    ######################################################################
    categoryList = currentAccounts.getHeaderNames()[assets_list_start_column:assets_list_end_column]
    accounts = {}

    for account in currentAccounts.getRowNames():
        if account == 'Total (Portfolio)':
            continue
        owner = currentAccounts.getValue(account, 'Owner')
        institution = currentAccounts.getValue(account, 'Institution')
        account_type = currentAccounts.getValue(account, 'Account Type')
        assets = {}
        for category in categoryList:
            assets[category] = currentAccounts.getValue(account, category)
        accounts[account] = ac.Account(owner, institution, account_type, assets, rules[account])





    #### Create a List of Funding Request Dictionaries ###
    #################################################
    fundingRequests = []
    lastRowInList = -1
    for row in fundingRequestSheet.getRowNames():
        fundingRequests.append({})
        fundingRequests[lastRowInList][row] = {'account_name': fundingRequestSheet.getValue(row, 'Account to Fund'), 'funding_value': fundingRequestSheet.getValue(row, 'Amount to Fund')}



    #### Create a Dictionary of Desired Allocations per Category ####
    #################################################################
    desiredAllocation = {}

    for category in categoryList:
        desiredAllocation[category] = desiredAllocationsheet.getValue(category, 'Desired Percent')



    return accounts, fundingRequests, desiredAllocation
