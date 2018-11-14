import unittest
from fibonacci import fibonacci_sequence

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_sequence(self):
        # Test calculate the term number 2 of tha Fibonacci Sequence
        self.assertEqual(fibonacci_sequence(2), 1)
        # Test calculate the term number 15 of tha Fibonacci Sequence
        self.assertEqual(fibonacci_sequence(15), 610)
        # Test calculate the term number 31 of tha Fibonacci Sequence
        self.assertEqual(fibonacci_sequence(31), 1346269)

    def test_values(self):
         # Test if value error is raised to n values off the limits
        self.assertRaises(ValueError, fibonacci_sequence, -1)
    
    def test_type(self):
        # Test if type error is raised to invalid n type
        self.assertRaises(TypeError, fibonacci_sequence, "a")