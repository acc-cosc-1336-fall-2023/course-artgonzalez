#
import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(4), 24)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(6), 720)

    def test_get_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(9), 25)
        self.assertEqual(sum_odd_numbers(10), 25)
