import unittest
from tilecost import tile_cost

class TestTileCost(unittest.TestCase):


    def test_next_prime(self):
        # Test the cost for a 2m x 3m that cost 4 per m^2
        self.assertEqual(tile_cost(2,3,4), 24)
        # Test the cost for a 5m x 6m that cost 7 per m^2
        self.assertEqual(tile_cost(5,6,7), 210)


    def test_values(self):
        # Test if value error is raised to values off the limits
        self.assertRaises(ValueError, tile_cost, 0,1,2)
        # Test if value error is raised to values off the limits
        self.assertRaises(ValueError, tile_cost, 1,-1,2)
        # Test if value error is raised to values off the limits
        self.assertRaises(ValueError, tile_cost, 1,2,-2)
    

    def test_type(self):
        # Test if type error is raised to invalid value type
        self.assertRaises(TypeError, tile_cost, "a")