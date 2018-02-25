from reallocate import reallocate
from export import exportToExcel

reallocatedAccounts = reallocate()

exportToExcel(reallocatedAccounts)
