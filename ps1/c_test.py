import unittest
from ps1c import best_savings_rate

# tests
# class test_calc_monthly_savings(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(calc_monthly_savings(120, .10), 1)

# class test_adjust_anual_salary_test(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(adjust_anual_salary(100, .03), 103)

class test_best_savings_reate(unittest.TestCase):
    def test1(self):
        self.assertEqual(best_savings_rate(150000), (0.4411, 12))
    def test2(self):
        self.assertEqual((300000), (0.2206, 9))
    def test3(self):
        self.assertEqual((10000), ("It is not possible to pay the down payment in three years."))