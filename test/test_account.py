import unittest
from reallocate.account import Account

class TestAccount(unittest.TestCase):

	def setUp(self):
		self.assets = {'Cash/MMKT': 500,'Tax Bonds': 3703.27,'Sm/Mid Blend': 136.84}
		self.account = Account('John', 'Bank', 'Roth IRA', self.assets)

	def test_get_total_value(self):
		expected_value = 0
		for asset in self.assets:
			expected_value += self.assets[asset]
		self.assertEqual(expected_value, self.account.get_total_value())

	def test_get_category_value(self):
		expected_value = self.assets['Tax Bonds']
		self.assertEqual(expected_value, self.account.get_category_value('Tax Bonds'))

	def test_fund_account(self):
		fund_amount = 10.4
		self.account.fund_account('Cash/MMKT', fund_amount)
		expected_value = self.assets['Cash/MMKT'] + fund_amount
		self.assertEqual(expected_value, self.account.assets['Cash/MMKT'])

	def test_fund_non_existent_asset_category(self):
		fund_amount = 100
		self.assertRaises(Exception, self.account.fund_account, 'non-existent asset', fund_amount)

	def test_withdraw_account(self):
		withdraw_amount = 14.2
		self.account.withdraw_account('Tax Bonds', withdraw_amount)
		expected_value = self.assets['Tax Bonds'] - withdraw_amount
		self.assertEqual(expected_value, self.account.assets['Tax Bonds'])

	def test_withdraw_account_insufficient_funds(self):
		withdraw_amount = 10000000
		self.assertRaises(ValueError, self.account.withdraw_account, 'Tax Bonds', withdraw_amount)

	def test_withdraw_all_funds(self):
		# Withdraw all funds from this asset
		withdraw_amount = self.assets['Sm/Mid Blend']
		self.account.withdraw_account('Sm/Mid Blend', withdraw_amount)
		self.assertEqual(0, self.account.assets['Sm/Mid Blend'])

	def test_withdraw_from_non_existent_asset_category(self):
		withdraw_amount = 100
		self.assertRaises(Exception, self.account.withdraw_account, 'non-existent asset', withdraw_amount)