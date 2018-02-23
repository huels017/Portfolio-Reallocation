import copy

class Account(object):
	""" Represents an account
	"""

	def __init__(self, owner, institution, account_type, assets):
		""" Create an account

		Args:
			owner (string): The owner of the account
			institution (string): The institution associated with the account
			account_type (string): The account type (401(k), cash, SIMPLE IRA, etc.)
			assets (dict): A dictionary of asset classes and their associated values.
				For example: assets = {'Cash/MMKT': 500,'Tax Bonds': 3703.27,'Sm/Mid Blend': 136.84}
		"""

		self.owner = owner
		self.institution = institution
		self.account_type = account_type
		self.assets = copy.deepcopy(assets)

	def get_total_value(self):
		""" Gets the total value of all assets in the account

		"""
		total_value = 0
		for asset_category in self.assets:
			total_value += self.assets[asset_category]

		return total_value

	def get_category_value(self, asset_category):
		return self.assets[asset_category]

	def fund_account(self, asset_category, value):
		""" Add funds to the specified asset category within the account.

		"""
		if asset_category not in self.assets:
			raise Exception('The specified asset category does not exist')

		self.assets[asset_category] += value

	def withdraw_account(self, asset_category, value):
		""" Subtract funds from the specified asset category within the account.

		"""
		if asset_category not in self.assets:
			raise Exception('The specified asset category does not exist')

		if self.assets[asset_category] < value:
			raise ValueError('Insufficient funds')

		self.assets[asset_category] -= value
