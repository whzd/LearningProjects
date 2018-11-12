import unittest
from pi import find_pi
from math import pi
from decimal import Decimal

class TestPi(unittest.TestCase):

    def test_pi(self):
        # Test find pi to the 3rd digit
        self.assertEqual(find_pi(3), format(pi, '.3f'))
        # Test find pi to the 11rd digit
        self.assertEqual(find_pi(10), format(pi, '.10f'))

    def test_values(self):
         # Test if value error is raised to n values of the limits
        self.assertRaises(ValueError, find_pi, 0)
        self.assertRaises(ValueError, find_pi, 12)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, find_pi, "a")
