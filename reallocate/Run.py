from reallocate import reallocate
from export import exportToExcel
from initialize_objects import initializeObjects
import copy
from funding import fulfillFundingRequests

###Initialize Accounts###
assets_list_start_column = 3 # categories start at the 4th column in excel template
assets_list_end_column = -1 #don't include the 'total' column
currentAccounts, fundingRequests, desiredAllocation = initializeObjects('../Allocation_Template.xlsx', assets_list_start_column, assets_list_end_column)



###Fund Accounts###
fundAccounts = copy.deepcopy(currentAccounts)
fulfillFundingRequests(fundAccounts, fundingRequests, desiredAllocation)


###Reallocate Accounts###
reallocateAccounts = copy.deepcopy(fundAccounts)

reallocatedAccounts = reallocate()  #old version of funding and reallcation, Will be removed after new procedure is complete



###Future Portfolio Projections###
futureAccounts = copy.deepcopy(reallocateAccounts)



###Output Results###
exportToExcel(reallocatedAccounts) #old version of export, Will be removed after new procedure is complete
