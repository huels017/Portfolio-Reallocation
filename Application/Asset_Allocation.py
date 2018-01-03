from pull import pull_allocation_data
from reallocate import reallocate_accounts
from Write import output_results

def resourceAllocation(financialAccounts):


    


    #Pull in Account Data, desired allocation, and IRS statues from excel
	
    current_account_values, desired_allocation, ira_statues = pull_allocation_data('Allocation.xlsx')

    #print(desired_allocation, "here")
    #print(current_account_values, "There")

    #Determine how to adjust accounts to reach desired allocation
    
    reallocation_suggestion = reallocate_accounts(current_account_values, desired_allocation, ira_statues)


    output_results(current_account_values)
 

    return reallocation_suggestion


print(resourceAllocation('Allocation.xlsx'))

