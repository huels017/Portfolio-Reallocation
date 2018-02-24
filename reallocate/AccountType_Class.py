
 
class AccountType:
"""Output will be the account type

Arguments: 

name(string): name of account (ex. 401K, Cash, Roth IRA)
tax_status(string): boolean (True/False), Qualified/Not Qualified
is_deferred: boolean? "def" from excel file
is_exempt: boolean? "exempt" from excel file
changes_allowed: boolean Y/N


"""

	def __init__(self, name, tax_status, is_deferred, is_exempt, changes_allowed, limited):
		self.name = name
		self.tax_status = tax_status
		self.is_deferred = is_deferred
		self.is_exempt = is_exempt
		self.changes_allowed = changes_allowed
		self.limited = limited



#Ultimately going to be incorporated in Account Class file

 