from reallocate_functions_2 import category_totalizer, desired_category_totals, list_difference, accounts_rule_scan, fixed_accounts_vs_desired_allocation, fixed_taxed_vs_desired_allocation, reallocate, absolute_change_needed, fund_ira


def reallocate_accounts(current_account_values, desired_allocation, ira_statues, max_taxed_sales):
    """
    reallocate accounts will take in account data, desired allocation and ira statues.

    It will determine what value of each cateogry needs to be bought or sold.

    It will check if desired allocation can be acheived considering that some accounts cann't be changed

    Using rules it will determine what squence to start making changes to desired_account_data

    It will step through sequence making changes until desired allocation is achieved

    Then it will output desired_account_data which will inform financial advisor which accounts to make changes to and what categories in those accounts change



    """
    ###############
    #    calcs    #
    ###############

    #calculate total category values for current and desired states
    # p#rint(current_account_values[13][13])
    category_totals, total_wealth = category_totalizer(current_account_values)
    
    desired_category_values = desired_category_totals(total_wealth, desired_allocation)


    #This is the ammount that needs to be bought or sold per category to reach desired allocation
    diff_current_vs_desired = list_difference(desired_category_values, category_totals)


   



    #determine which rules to apply
    '''
	#Fund IRA first (need to pull that info in)
        #
	#move money in tax exempt accounts first(401, 401k, ira, roth, trad, rollover, IRAs, 403b, roll, def comp)
        #
	#use cash in brokarage accounts before 'cash on hand' accounts
        #
	#lastly make changes to taxed accounts
	#
	#whole life policies and annuities cann't be changed:
		#(whole life cash value, fixed annuity, variable annuity, pension(unless not employeed there anymore))
	#Real estate accounts cann't be changed (real estate)
	#stock purchase plan accounts cann't be changed (ESOP, ESPP)

    #Most benifit from tax exempt statues
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

    #if tax exempt accounts > 200k, then minimum 10% taxed bonds
    '''

    
    
    account_rules = accounts_rule_scan(current_account_values)
    



    #can each category be brought to desired allocation?
    #- meaning do the fixed accounts push any category over desired allocation

    ###Check if Broken-###  fixed_accounts_vs_desired_allocation(desired_category_values, current_account_values, account_rules)
    #- add error to tell which category is outside allocation range and by how much


    #can each category be brought to desired allocation without touching taxed accounts?
    ###Broken-### -  fixed_taxed_vs_desired_allocation(desired_category_values, current_account_values, account_rules)
    #- add- which categories and by how much is this out of range (when out of range)

    #print(account_rules)


    ###################################################
    #make change to recommened changes based on rules
    ###################################################
    #print(diff_current_vs_desired)



    #IRA Funding#
    #currently looking in fixed location for 'Cash on Hand'
    #currently looking in fixed location for 'Emerg Mkts' 
    # if cash on hand is not high enough, it will not fund ira

    fund_ira(diff_current_vs_desired, current_account_values, account_rules, ira_statues)



    #Tax Exempt#
    #-over threshold? if yes minimun 10% taxed bonds
    #-buy categories that are low in current value compared to desired from top of benifits list, sell categories that are high in current value compared to desired from bottom of benifits list. 

    print(absolute_change_needed(diff_current_vs_desired))
    #print(diff_current_vs_desired)

    reallocate(diff_current_vs_desired, current_account_values, account_rules, 'tax_exempt')
    
    print(absolute_change_needed(diff_current_vs_desired))
    #print(diff_current_vs_desired)


    #Tax Deferred#

    reallocate(diff_current_vs_desired, current_account_values, account_rules, 'tax_deferred')
    print(absolute_change_needed(diff_current_vs_desired))


    #Taxed Accounts#
    #add- select max amount of taxed value to move around
    reallocate(diff_current_vs_desired, current_account_values, account_rules, 'taxed', 10000000)
    print(absolute_change_needed(diff_current_vs_desired))


    #Cash on Hand#
    #- is cash on hand higher than desired cash?
    #- yes? move some to brokerage account to buy assets
    #- no? don't touch cash on hand
    #-use brokarage cash before cash on hand






    #    #    
    #    #    
    #    #    
    #    #    
    #    #    
    #    #    
    ##   #   # 
    # #  #  #  
    #  # # #   
    #   ###    
    #    #    
  
    ##########################################
    #############################################
    #spit out results#











    return 




