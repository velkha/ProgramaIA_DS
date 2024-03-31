import random
from typing import List

class DiscreteRandomVariable:
    '''	
    A class to represent a discrete random variable.
    '''	
    def __init__(self, outcomes: List[str], probabilities: List[float]):
        self.outcomes = outcomes
        self.probabilities = probabilities

    def simulate(self, n: int) -> List[str]:
        '''
        Simulate n samples from the random variable.
        '''
        _samples = []
        for _ in range(n):
            _rand_num = random.random()
            _cumulative_prob = 0
            for i, prob in enumerate(self.probabilities):
                _cumulative_prob += prob
                if _rand_num <= _cumulative_prob:
                    _samples.append(self.outcomes[i])
                    break
        return _samples
