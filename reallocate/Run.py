from reallocate import reallocate
from export import exportToExcel
from initialize_objects import initializeObjects

accountsDictionary = initializeObjects('../Allocation_Template.xlsx')

reallocatedAccounts = reallocate()

exportToExcel(reallocatedAccounts)
