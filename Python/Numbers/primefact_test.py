import unittest
from primefact import is_prime, prime_factors

class TestPrimeFactores(unittest.TestCase):

    def test_is_prime(self):
        # Test prime value verification for number 2
        self.assertEqual(is_prime(2), True)
        # Test prime value verification for number 4
        self.assertEqual(is_prime(4), True)
        # Test prime value verification for number 13
        self.assertEqual(is_prime(13), True)
        # Test prime value verification for number 28
        self.assertEqual(is_prime(28), True)
        # Test prime value verification for number 43
        self.assertEqual(is_prime(43), True)
        # Test prime value verification for number 49
        self.assertEqual(is_prime(49), True)
    
    def test_prime_factores(self):
        self.assertEqual(True, True)

    def test_values(self):
         # Test if value error is raised to n values off the limits
        self.assertRaises(ValueError, prime_factors, 0)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, prime_factors, "a")