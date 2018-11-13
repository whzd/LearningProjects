import unittest
from e import find_e, fatorial
from math import e
from math import factorial

class TestE(unittest.TestCase):

    def test_fatorial(self):
        # Test created fatorial method to calculate the fatorial of 3
        self.assertEqual(fatorial(3), factorial(3))
        # Test created fatorial method to calculate the fatorial of 15
        self.assertEqual(fatorial(15), factorial(15))
        # Test created fatorial method to calculate the fatorial of 25
        self.assertEqual(fatorial(25), factorial(25))

    def test_e(self):
        # Test find e to the 3rd digit
        self.assertEqual(find_e(3), format(e, '.3f'))
        # Test find e to the 11rd digit
        self.assertEqual(find_e(9), format(e, '.9f'))
        # Test find e to the 15rd digit
        self.assertEqual(find_e(14), format(e, '.14f'))

    def test_values(self):
         # Test if value error is raised to n values off the limits
        self.assertRaises(ValueError, find_e, 0)
        self.assertRaises(ValueError, find_e, 16)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, find_e, "a")