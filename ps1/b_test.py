import unittest
from ps1b import calc_month_to_downpayment_with_raise, adjust_anual_salary, calc_monthly_savings

# tests
class test_calc_monthly_savings(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc_monthly_savings(120, .10), 1)

class test_adjust_anual_salary_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(adjust_anual_salary(100, .03), 103)

class test_downpayment(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc_month_to_downpayment_with_raise(120000, .05, .03, 500000), 142)
    def test2(self):
        self.assertEqual(calc_month_to_downpayment_with_raise(80000, .1, .03, 800000), 159)
    def test3(self):
        self.assertEqual(calc_month_to_downpayment_with_raise(75000, .05, .05, 1500000), 261)
