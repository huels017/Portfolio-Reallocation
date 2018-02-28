import unittest
from reallocate.funding_request import FundingRequest

class TestFundingRequest(unittest.TestCase):

    def setUp(self):
        self.account = 'A1'
        self.fundingValue = 9999

        self.funding_request = FundingRequest(self.account, self.fundingValue)

    def test_account(self):
        self.assertEqual(self.account, self.funding_request.account)

    def test_value(self):
        self.assertEqual(self.fundingValue, self.funding_request.fundingValue)
