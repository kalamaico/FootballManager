#!python

import random, time

class RandomGenerator:
    def __init__(self):
        random.seed(time.clock())
        
    def generate_uniform(self, min_v, max_v):
        return random.uniform(min_v, max_v)
        
    def generate_int(self, min_v, max_v):
        return random.randint(min_v, max_v)
        
    def generate_int_sequence_no_repetitions(self, length, min_v, max_v):
        ret = set()
        if length > max_v - min_v + 1:
            raise ValueError("Requested a length of " + str(length) + " for an interval of " + str(max_v - min_v + 1))
        
        while len(ret) < length:
            val = ret.add(self.generate_int(min_v, max_v))

        return sorted(ret)
        
        
        
class RandomGeneratorDeterministic(RandomGenerator):
    def __init__(self):
        random.seed(0)
    
    def generate_uniform(self, min_v, max_v):
        return (max_v - min_v) /2
        
    def generate_int(self, min_v, max_v):
        return 42
