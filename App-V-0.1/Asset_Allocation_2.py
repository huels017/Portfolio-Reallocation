from pull_2 import pull_allocation_data
from reallocate_2 import reallocate_accounts
from Write_2 import output_results

def resourceAllocation(excel_name):


    


    #Pull in Account Data, desired allocation, and IRS statues from excel
    #pull_allocation_data(excel_name)
    #print('Here')
    #print(pull_allocation_data(excel_name))

    current_account_values, desired_allocation, ira_statues, max_taxed_sales = pull_allocation_data(excel_name)

    #print(current_account_valuesS)
    

    #Adjust accounts toward desired allocation
    
    #print(current_account_values)

    while True:
        try: 

            reallocation_suggestion = reallocate_accounts(current_account_values, desired_allocation, ira_statues, max_taxed_sales)       
            print('Reallocation succesful.')
            break
        except (TypeError):
            print('Error: Trying to Reallocate')
            return


    output_results(current_account_values)
 

    return #reallocation_suggestion


#resourceAllocation('Allocation_Template_2 _Hurley.xlsx')

