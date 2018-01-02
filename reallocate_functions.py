




def category_totalizer(current_accounts):
    '''

    '''
    category_names = [u'Cash/MMKT', u'Tax Bonds', u'Muni Bonds', u'LC Value', u'LC Growth', u'LC Blend', u'International', u'Emg Mkts', u'Sm/Mid Value', u'Sm/Mid Growth', u'Sm/Mid Blend', u'Commodities', u'REIT', u'Balanced']

    total_category_values = []
    category_number = 0

    for category in category_names:
        total_category_values.append(0)
        for account in current_accounts:
            total_category_values[category_number] += account[1][category_number]
            #print(account[1][category_number])
        category_number += 1



    #print(total_category_values)
    total = 0
    for category_value in total_category_values:
        total += category_value


    return total_category_values, total



def desired_category_totals(total_wealth, desired_allocation):
    '''

    '''
    desired_category_values = []
   
    for category in desired_allocation:
        desired_category_values.append(category[1][0]*total_wealth)






    return desired_category_values



def list_difference(desired_list, current_list):
    '''
    
    '''
    i = 0
    diff_list = []
    for value in desired_list:
        diff_list.append(value - current_list[i])
        i += 1
    

    return diff_list



def accounts_rule_scan(accounts_list):
    '''
        #determine which rules to apply

	#Fund IRA first (need to pull that info in)
	#move money in tax exempt accounts first(401, 401k, ira, roth, trad, rollover, IRAs, 403b, roll, def comp)
	#use cash in brokarage accounts before 'cash on hand' accounts
	#lastly make changes to taxed accounts
	#
	#whole life policies and annuities cann't be changed:
		#(whole life cash value, fixed annuity, variable annuity, pension(unless not employeed there anymore))
	#Real estate accounts cann't be changed (real estate)
	#stock purchase plan accounts cann't be changed (ESOP, ESPP)
    scan accounts for "whole life cash value, fixed annuity, variable annuity, pension, real estate, ESOP, ESPP" - these cann't be changed 
    
    
    '''
    accounts = []
    i = -1
    for account in accounts_list:
        i += 1
        accounts.append([account[0][0].upper()])

        if (str(accounts[i][0]).find('WHOLE LIFE CASH VALUE') > -1) or (str(accounts[i][0]).find('FIXED ANNUITY') > -1) or (str(accounts[i][0]).find('VARIABLE ANNUITY') > -1) or (str(accounts[i][0]).find('PENSION') > -1) or (str(accounts[i][0]).find('REAL ESTATE') > -1) or (str(accounts[i][0]).find('ESOP') > -1) or (str(accounts[i][0]).find('ESPP') > -1):
            accounts[i].append('fixed')
        


        elif (str(accounts[i][0]).find('IRA') > -1) or (str(accounts[i][0]).find('ROTH') > -1) or (str(accounts[i][0]).find('403B') > -1):
            accounts[i].append('tax_exempt')

        elif (str(accounts[i][0]).find('401') > -1) or (str(accounts[i][0]).find('DEF COMP') > -1) or (str(accounts[i][0]).find('SIMPLE') > -1) or (str(accounts[i][0]).find('TRAD') > -1) or (str(accounts[i][0]).find('ROLL') > -1):
            accounts[i].append('tax_deferred')

        elif (str(accounts[i][0]).find('SEP IRA') > -1):
            accounts[i][1] ='tax_deferred'

        elif (str(accounts[i][0]).find('CASH ON HAND') > -1):
            accounts[i].append('cash')


        else:
            accounts[i].append('taxed')

    return accounts  




def fixed_accounts_vs_desired_allocation(desired, current, rules):
    '''
    find all fixed accounts
    add all fixed accounts together per category
    check if fixed accounts per category is greater than desired allocation in any category
    '''
    i = -1
    fixed_account_totals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #find accounts with fixed as rule
    for rule in rules:
        i += 1
         
        if str(rule[1]) == 'fixed':
            count = 0

            #add fixed accounts to fixed_account_totals
            for category in current[i][1]:
                fixed_account_totals[count] += category
                count += 1
        
    #print(fixed_account_totals)
    count = -1
    for category in desired:
        count += 1
        if fixed_account_totals[count] > category:
            
            print('Error: Fixed accounts outside desired allocation range.')
            return 

    print('Fixed accounts within desired allocation range.')
    return 




def fixed_taxed_vs_desired_allocation(desired, current, rules):
    '''
    find all fixed and taxed accounts
    add all fixed and taxed accounts together per category
    check if fixed and taxed accounts per category is greater than desired allocation in any category
    '''
    i = -1
    fixed_taxed_account_totals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #find accounts with fixed as rule
    for rule in rules:
        i += 1
         
        if str(rule[1]) == 'fixed' or str(rule[1]) == 'taxed':
            count = 0

            #add fixed accounts to fixed_account_totals
            for category in current[i][1]:
                fixed_taxed_account_totals[count] += category
                count += 1
        
    #print(fixed_account_totals)
    count = -1
    for category in desired:
        count += 1
        if fixed_taxed_account_totals[count] > category:
            
            print('Fixed and taxed accounts outside desired allocation range.')
            return 

    print('Fixed accounts within desired allocation range.')
    return 



def reallocate(needed_change, current_account_values, account_rules, group_rule):
    '''
    add- select max amount of taxed value to move around


    #Most benifit from tax exempt statues ###priority categories from list below####
    Emerg Mkts
    Sm/Mid Growth
    REIT
    International
    Sm/Mid Value
    Commodities
    Sm/Mid Blend
    LC Growth
    LC Value
    LC Blend
    Balanced
    Tax Bonds
    Muni Bonds
    Cash/MMKT
    #least benfit from tax exempt statues 
    '''
    priority_categories = [7, 9, 12, 6, 8, 11, 10, 4, 3, 5, 13, 1, 2, 0]

    buy_categories = []
    sell_categories = []
    accounts_with_rule = []

    #label categories as buy or sell
    i = 0
    for category_value in needed_change:
        if category_value >= 0:
            buy_categories.append(i)
        else:
            sell_categories.append(i)
        i += 1

    



    #find accounts with rule
    i = 0
    for rule in account_rules:
        if rule[1] == group_rule:
            accounts_with_rule.append(i)
        i += 1
    

    #reallocate one account at a time 
    for account in accounts_with_rule:
        

        sales = 0
        for sell in sell_categories:
            smaller = min(abs(needed_change[sell]), current_account_values[account][1][sell])
            current_account_values[account][1][sell] -= smaller
            needed_change[sell] += smaller
            sales += smaller
            #print(smaller)
            
        for cat in priority_categories:
            if cat in buy_categories:
                small_buy = min(needed_change[cat], sales)
                current_account_values[account][1][cat] += small_buy
                needed_change[cat] -= small_buy            
                sales -= small_buy
                #print(smaller)





    return current_account_values 




def absolute_change_needed(change_list):
    total = 0
    abs_total = 0

    for value in change_list:
        abs_total += abs(value)

   
    for value in change_list:
        total += (value)

    return abs_total, total





