import unittest
from nextprime import is_prime, next_prime

class TestNextPrime(unittest.TestCase):

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
    
    def test_next_prime(self):
        # Test prime factorization for number 3
        self.assertEqual(next_prime(3), 5)
        # Test prime factorization for number 28
        self.assertEqual(next_prime(14), 17)
        # Test prime factorization for number 28
        self.assertEqual(next_prime(24), 29)

    def test_values(self):
        # Test if value error is raised to n values off the limits
        self.assertRaises(ValueError, next_prime, 0)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, next_prime, "a")