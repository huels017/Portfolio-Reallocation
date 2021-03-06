class AccountType:
"""Represents the characteristics of an account type

Arguments: 
	name(string): name of account (ex. 401K, Cash, Roth IRA)
	is_qualified(bool): whether account tax status is "qualified" or "not qualified"
	is_deferred(bool): whether account tax status is "deferred"
	is_exempt(bool):
	changes_allowed(bool): the account can be modified
"""

	def __init__(self, name, tax_status, is_deferred, is_exempt, changes_allowed, limited):
		self.name = name
		self.tax_status = tax_status
		self.is_deferred = is_deferred
		self.is_exempt = is_exempt
		self.changes_allowed = changes_allowed
		self.limited = limited
