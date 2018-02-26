from reallocate import reallocate
from export import exportToExcel
from initialize_objects import initializeObjects

assets_list_start_column = 3 # categories start at the 4th column in excel template
assets_list_end_column = -1 #don't include the 'total' column
accounts = initializeObjects('../Allocation_Template.xlsx', assets_list_start_column, assets_list_end_column)

reallocatedAccounts = reallocate()

exportToExcel(reallocatedAccounts)
