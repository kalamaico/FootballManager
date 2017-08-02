import unittest
from resources.player import *
from resources.random_generator import *

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.rng = RandomGenerator()

    def test_generate_generic(self):
        self.assertTrue(self.validate_generic(Player.generate(self.rng, 1), 1, 5))
        self.assertTrue(self.validate_generic(Player.generate(self.rng, 2), 2, 6))
        self.assertTrue(self.validate_generic(Player.generate(self.rng, 3), 3, 7))
        self.assertTrue(self.validate_generic(Player.generate(self.rng, 4), 4, 8))
        self.assertTrue(self.validate_generic(Player.generate(self.rng, 10), 10, 14))
        with self.assertRaises(ValueError):
			Player.generate(self.rng, 15)
        
    def validate_generic(self, p, minval, maxval):
        return  p._physical >= minval and \
            p._physical <= maxval and \
            p._mental >= minval and \
            p._mental <= maxval
        
    def test_generate_goalkeeper(self):
        self.assertTrue(self.validate_keeper(Goalkeeper.generate(self.rng, 1), 2, 4))
        self.assertTrue(self.validate_keeper(Goalkeeper.generate(self.rng, 3), 4, 6))
        self.assertTrue(self.validate_keeper(Goalkeeper.generate(self.rng, 7), 8, 10))
        self.assertTrue(self.validate_keeper(Goalkeeper.generate(self.rng, 10), 11, 13))
        with self.assertRaises(ValueError):
			Goalkeeper.generate(self.rng, 15)

    def validate_keeper(self, p, minval, maxval):
        return  p._keeper >= minval and \
            p._keeper <= maxval
        
    def test_generate_outfielder(self):
        p = Outfielder.generate(self.rng, 1, "winger")
        self.assertEqual(p._defence, 1)
