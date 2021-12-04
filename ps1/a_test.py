import unittest
from ps1a import calc_month_to_downpayment

# tests
class test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc_month_to_downpayment(120000, .10, 1000000), 183)
    def test2(self):
        self.assertEqual(calc_month_to_downpayment(80000, .15, 500000), 105)
