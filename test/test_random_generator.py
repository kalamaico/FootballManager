import unittest
from resources.random_generator import *

class TestRandomGenerator(unittest.TestCase):

    def setUp(self):
        self.rng = RandomGenerator()
        
    def test_generate_int(self):
        val = self.rng.generate_int(1,10)
        self.assertTrue(val >= 1)
        self.assertTrue(val <= 10)
        
    def test_generate_int_sequence_no_repetitions(self):
        vals = self.rng.generate_int_sequence_no_repetitions(5, 1, 10)
        self.assertEqual(len(vals), 5)
        with self.assertRaises(ValueError):
			self.rng.generate_int_sequence_no_repetitions(5, 1, 3)

    def test_generate_int_sequence(self):
        vals = self.rng.generate_int_sequence(5, 1, 10)
        self.assertEqual(len(vals), 5)
        
