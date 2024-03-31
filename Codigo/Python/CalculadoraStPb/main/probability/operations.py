import math
from scipy.stats import norm
import numpy as np

class ProbabilityOperations:
    def __init__(self):
        pass

    def calculate_probability(self, event_outcomes: int, sample_space: int) -> float:
        """
        Calculates the probability of an event given the number of favorable outcomes and the sample space size.
        """
        return event_outcomes / sample_space

    def complement(self, probability: float) -> float:
        """
        Calculates the complement of a given probability.
        """
        return 1 - probability

    def union(self, probability_a: float, probability_b: float) -> float:
        """
        Calculates the union of two probabilities using the inclusion-exclusion principle.
        """
        return probability_a + probability_b - self.intersection(probability_a, probability_b)

    def intersection(self, probability_a: float, probability_b: float) -> float:
        """
        Calculates the intersection of two probabilities.
        """
        return probability_a * probability_b

    def conditional(self, probability_a: float, probability_b: float) -> float:
        """
        Calculates the conditional probability of A given B.
        """
        return self.intersection(probability_a, probability_b) / probability_b
    
    def calculateTotalFavorableOutcomes(self, sample_space: int, favorableOutcomes:int) -> int:
        """
        Calculates the total number of favorable outcomes. Esto se hace
        de manera mas optima con math.comb(sample_space, favorableOutcomes), esto es una aplicacion para asentar
        conocimientos sobre estadistica y probabilidad.
        """
        return math.factorial(sample_space) / (math.factorial(favorableOutcomes) 
                                               * math.factorial(sample_space - favorableOutcomes))
    
    def calculateBinomialProbability(self, k: float, n: float, p: float) -> float:
        """
        Calculates the probability of k successes in n trials with probability p.
        """
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    
    def normalAproximationToBinomial(self, n: float, p: float) -> tuple:
        """
        Approximates a binomial distribution to a normal distribution.
        """
        _mu = n * p
        _sigma = math.sqrt(n * p * (1 - p))
        return _mu, _sigma
    
    def binomialProbabilityNormalApproximation(self, k: int, n: int, p: float) -> float:
        """
        Calculates the probability of 
            k successes in 
            n trials with  
            p probability using the normal approximation.
        
        This is a more direct aproach to make the calculation.

        mu, sigma = self.normalAproximationToBinomial(n, p)
        return self.normalProbability(k, mu, sigma) 
        more manual approach"""
        # Calculate mean and standard deviation for the binomial dist
        _mean = n * p
        _std = np.sqrt(n * p * (1 - p))
        # Standardize the x value
        z = (k - _mean) / _std
        # Calculate the probability of getting at most 12 small prizes using the normal approximation
        # Since we want "at most", we look for the cumulative probability up to and including x
        prob = norm.cdf(z)

        return(prob)


    def normalProbability(self, x: float, mu: float, sigma: float) -> float:
        """
        Calculates the probability of a value in a normal distribution.
        """
        return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    def normalProbabilityRange(self, x1: float, x2: float, mu: float, sigma: float) -> float:   
        """
        Calculates the probability of a range of values in a normal distribution.
        """
        return self.normalProbability(x2, mu, sigma) - self.normalProbability(x1, mu, sigma)
    
    def calculate_value_probabilities(self, values: list) -> dict:
        """
        Calculates the probability of each value in the given array.
        Returns a dictionary with the value as the key and its probability as the value.
        """
        probabilities = {}
        total_values = len(values)
        for value in values:
            probability = values.count(value) / total_values
            probabilities[value] = round(probability, 5)
        return probabilities
    
    def probability_under_value_manual(self, value: float, mean: float, std_dev: float, sample_size: float) -> float:
        """
        Calculates the probability of getting a value under a given value in a normal distribution.
        """
        z = (value - mean) / (std_dev / math.sqrt(sample_size))
        prob = norm.cdf(z)
        return prob
    
    def probability_under_value_with_sample(self, value: float, data: list) -> float:
        """
        Calculates the probability of getting a value under a given value in a normal distribution.
        """
        mean = np.mean(data)
        std_dev = np.std(data)
        sample_size = len(data)
        z = (value - mean) / (std_dev / math.sqrt(sample_size))
        prob = norm.cdf(z)
        return prob