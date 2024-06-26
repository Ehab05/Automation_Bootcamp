import unittest

from math_function import is_even


class TestMathFunction(unittest.TestCase):
    def test_is_even_true(self):
        num = 4
        result = is_even(num)
        return self.assertTrue(result)

    def test_is_even_true(self):
        num = 0
        result = is_even(num)
        return self.assertTrue(result)

    def test_is_even_true(self):
        num = -2
        result = is_even(num)
        return self.assertTrue(result)
