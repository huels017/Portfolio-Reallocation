import xlwt



def output_results(reallocation_values):
    '''

    '''

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("reallocation")

    
    category_names = [u'Accounts', u'Cash/MMKT', u'Tax Bonds', u'Muni Bonds', u'LC Value', u'LC Growth', u'LC Blend', u'International', u'Emg Mkts', u'Sm/Mid Value', u'Sm/Mid Growth', u'Sm/Mid Blend', u'Commodities', u'REIT', u'Balanced']
    i = 0
    for cat in category_names:
        sheet1.write(1, i, cat)
        i += 1



    acc_num = 2

    for account in reallocation_values:

        sheet1.write(acc_num, 0, account[0][0])        

        cat_num = 1
        for category_value in account[1]:
            sheet1.write(acc_num, cat_num, category_value)
            cat_num += 1
        acc_num += 1





    book.save("Reallocation.xls")


    return
