




def category_totalizer(current_accounts):
    '''
    totalizes the value of each category accross all accounts regardless of tax statues/rules. 
    '''
    category_names = [u'Cash/MMKT', u'Tax Bonds', u'Muni Bonds', u'LC Value', u'LC Growth', u'LC Blend', u'International', u'Emg Mkts', u'Sm/Mid Value', u'Sm/Mid Growth', u'Sm/Mid Blend', u'Commodities', u'REIT', u'Balanced']

    total_category_values = []
    category_number = 0

    for category in category_names:
        total_category_values.append(0)
        for account in current_accounts:
            total_category_values[category_number] += account[1][category_number]
        category_number += 1


    
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



def reallocate(needed_change, current_account_values, account_rules, group_rule, max_taxed_sales = 0):
    '''
    This will move value from account categories that are above desired allocation to account categories that are below desired allocation. 

    This will only reallocate accounts with the same rules(tax exempt, tax deffered, taxxed, ext)


    max_taxed_sales - limits how many taxed assets will be sold if the group_rule is 'taxed' 

    The following list below sets the priority of which accounts to sell first and which to buy first.
    This list is based on the assumption that tax exempt accounts are reallocated first, followed by tax deffered, and taxed accounts. 
    The top of the list is bought first and the bottome is sold first. 
    This consentrates the top of the list in tax exempt accounts and the bottom of the list in taxed accounts. 
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
    total_sales = 0
    
    for account in accounts_with_rule:
        
        
        sales = 0
        for sell in sell_categories:
            to_sell = max_taxed_sales - total_sales
            if group_rule != 'taxed':
                to_sell = current_account_values[account][1][sell] 

            smaller = min(abs(needed_change[sell]), current_account_values[account][1][sell], to_sell)
            current_account_values[account][1][sell] -= smaller
            needed_change[sell] += smaller
            total_sales += smaller
            sales += smaller
            #print(to_sell, total_sales)
            







        for cat in priority_categories:
            if cat in buy_categories:
                small_buy = min(needed_change[cat], sales)
                current_account_values[account][1][cat] += small_buy
                needed_change[cat] -= small_buy            
                sales -= small_buy
                #print(smaller)

    

    if group_rule == 'taxed':
        print('Total taxed sales allowed: $' + str(max_taxed_sales))


    return current_account_values 




def absolute_change_needed(change_list):
    '''
    abs_total -is the summed distance from the desired allocation- This should decrease or stay the same as the 'reallocate' function is called. If it increases than the reallocate function is not working properly. 
 
    total -adds all distances above desired allocation and subtracts all distances below allocation. 
    total should be 0. If it is not 0 then value is not being tracked properly. 
     -Somewhere value is being added to an account category without being subracted from an account category, or visa versa. 
    '''
    total = 0
    abs_total = 0

    for value in change_list:
        abs_total += abs(value)

   
    for value in change_list:
        total += (value)

    return 'Abs dist from desired allocation: $' + str(int(abs_total)) + '. Sum of needed buys and sells: $' + str(int(total))





def fund_ira(needed_change, current_account_values, account_rules, ira_statues):
    '''
    Does IRA need funding? 
        -no- return
        -yes
            -is cash on hand > IRA funding needed?
                -yes, fund with cash on hand to ira account category 'Emerg Mkts'
                -no, sell from taxed accounts based on category priority list, starting with cash
    '''


    #does ira need funding?
    ira_total_needed = 0
    for account in ira_statues:
        ira_total_needed += account[1][0]
    print('$s to fund IRA accounts: ' + str(ira_total_needed))

    if ira_total_needed == 0:
        return

    #What accounts to fund?
    ira_account_lookup = []
    for ira_account in ira_statues:
        i = 0
        for account in current_account_values:
            if account[0][0] == ira_account[0][0]:
                ira_account_lookup.append([i, ira_account[1][0]])
                break
            i += 1
    #print(ira_account_lookup)

 


    #enough cash on hand to fund ira?

    if current_account_values[0][0][0] == 'Cash on Hand':
        if current_account_values[0][1][0] > ira_total_needed:
            print('cash on hand enought to fund ira')
            current_account_values[0][1][0] -= ira_total_needed
            for account in ira_account_lookup:
                current_account_values[account[0]][1][7] += account[1]

            #print(current_account_values)


        else:
            print('Not enough cash on hand to fund ira')
    else:
        print('Looking for Cash on hand in wrong location')
        

   #enough cash in taxed accounts? bonds?  



    return 







