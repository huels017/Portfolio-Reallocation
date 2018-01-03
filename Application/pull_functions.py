




def number_of_rows(tab):
    '''
    counting the number of rows between the column title and total 
    returns number of rows
    '''
    count = 0
    while count <= 203:
        count +=1
        if tab[('A' + str(count))].value == '':
            print('Error: blank space found were account name is expected')

        elif count == 203:
            print('Error: Total not found or more than 200 accounts or asset categories')

        elif tab[('A' + str(count))].value == 'Total':
            print('Total found.', (count-3),  tab['A2'].value)
            number_of_accounts = count - 3 #1 for header, 1 for column labels, 1 for row total label
            break
 
    return count-3



def create_list(number_of,tab,column_labels):
    '''
    can be used for both accounts and categories
    '''

    portfolio = []

    count = 0
    

    while count < number_of:
        portfolio.append([[tab[('A' + str(count+3))].value]])
        portfolio[-1].append([])

        for category in column_labels:
            portfolio[-1][1].append(tab[(category + str(count+3))].value)    

        count += 1

    return portfolio



def check_column_names(column_real_names, tab, labels):
    '''

    '''

    column_names = []

    for letter in labels:
        column_names.append(tab[letter + str(2)].value)

    if column_real_names == column_names:
        print('column names correct')
    else:
        print('Error: column names are not correct')

    return






