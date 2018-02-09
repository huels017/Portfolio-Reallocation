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

    SHEET1.write(0, 0, "Account")
    i = 1
    for category in categoryList:
        SHEET1.write(0, i, category)
        i +=1

    i = 1
    for account in accountList:
        SHEET1.write(i, 0, account)
        ii = 1
        for category in categoryList:
            SHEET1.write(i, ii, accounts.getValue(account, category))
            ii += 1
        i += 1

    BOOK.save("../Reallocation_Results.xls")
    return
