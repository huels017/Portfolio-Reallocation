import excel_import
import data_container as dc

"""
An example of how to use the excel_import module and the DataContainer class.
"""


#### Import and parse the Excel file: ####
##########################################

# ".." means go to the folder outside the current one. So if we are in /app/source_code, then ".."
# brings us into /app.
EXCEL_FILE_NAME = "../import_test.xlsx"
EXCEL_HEADER_ROW_INDEX = 1 # This is the row number that has the names of the asset classes (cash, bonds, stock, etc.)
dataframes = excel_import.importExcel(EXCEL_FILE_NAME, EXCEL_HEADER_ROW_INDEX) # Read the Excel file


#### Print out certain data: ####
#################################

ACCOUNTS_SHEET_NAME = "Accounts"

# Show all of the data in the Accounts worksheet
print dataframes[ACCOUNTS_SHEET_NAME]

accounts = dc.DataContainer(dataframes[ACCOUNTS_SHEET_NAME]) # Create a DataContainer for the 'accounts' worksheet

ACCOUNT_NAME = "A1"
ASSET_TYPE = "Cash/MMKT"
cashForA1Account = accounts.getValue(ACCOUNT_NAME, ASSET_TYPE) # Get the amount of cash in the A1 account
# print cashForA1Account

CASH_ASSET_TYPE = "Cash/MMKT"
BONDS_ASSET_TYPE = "Muni Bonds"
cashAndBonds = accounts.getColumns([CASH_ASSET_TYPE, BONDS_ASSET_TYPE]) # Get each account's amount in Cash and Bonds
#print cashAndBonds

assetClassNames = accounts.getHeaderNames() # List all of the asset class types
# print assetClassNames

accountNames = accounts.getRowNames() # List all of the account names
# print accountNames

# Get the number of rows and columns and save it in variable 'dimensions' as a tuple
dimensions = accounts.numberOfRows(), accounts.numberOfColumns()
# print dimensions