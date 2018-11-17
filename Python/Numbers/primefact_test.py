import unittest
from primefact import is_prime, prime_factors

class TestPrimeFactores(unittest.TestCase):

    def test_is_prime(self):
        # Test prime value verification for number 2
        self.assertEqual(is_prime(2), True)
        # Test prime value verification for number 4
        self.assertEqual(is_prime(4), False)
        # Test prime value verification for number 13
        self.assertEqual(is_prime(13), True)
        # Test prime value verification for number 28
        self.assertEqual(is_prime(28), False)
        # Test prime value verification for number 43
        self.assertEqual(is_prime(43), True)
        # Test prime value verification for number 49
        self.assertEqual(is_prime(49), False)
    
    def test_prime_factores(self):
        # Test prime factorization for number 3
        self.assertEqual(prime_factors(3), [3])
        # Test prime factorization for number 28
        self.assertEqual(prime_factors(28), [2, 2, 7])

    def test_values(self):
         # Test if value error is raised to n values off the limits
        self.assertRaises(ValueError, prime_factors, 0)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, prime_factors, "a")