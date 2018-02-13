import xlwt
from main_functions import listOfCategories, listOfAccounts


def exportToExcel(accounts):
    '''
    Creates a excel file saves the accounts data into file, which is one directory above this file
    '''
    BOOK = xlwt.Workbook(encoding="utf-8")
    SHEET1 = BOOK.add_sheet("reallocationAccounts")

    categoryList = listOfCategories()
    accountList = listOfAccounts()

    ROW = 0  #Account
    COLUMN = 0  #Category

    SHEET1.write(ROW, COLUMN, "Account")
    i = 1
    for category in categoryList:
        SHEET1.write(ROW, i, category)
        i +=1

    i = 1
    for account in accountList:
        SHEET1.write(i, COLUMN, account)
        ii = 1
        for category in categoryList:
            SHEET1.write(i, ii, accounts.getValue(account, category))
            ii += 1
        i += 1

    BOOK.save("../Reallocation_Results.xls")
    return
