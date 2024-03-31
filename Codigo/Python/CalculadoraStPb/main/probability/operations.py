import math
from scipy.stats import norm
import numpy as np

class ProbabilityOperations:
    def __init__(self):
        pass

    def calculate_probability(self, event_outcomes, sample_space) -> float:
        """
        Calculates the probability of an event given the number of favorable outcomes and the sample space size.
        """
        return event_outcomes / sample_space

    def complement(self, probability) -> float:
        """
        Calculates the complement of a given probability.
        """
        return 1 - probability

    def union(self, probability_a, probability_b) -> float:
        """
        Calculates the union of two probabilities using the inclusion-exclusion principle.
        """
        return probability_a + probability_b - self.intersection(probability_a, probability_b)

    def intersection(self, probability_a, probability_b) -> float:
        """
        Calculates the intersection of two probabilities.
        """
        return probability_a * probability_b

    def conditional(self, probability_a, probability_b) -> float:
        """
        Calculates the conditional probability of A given B.
        """
        return self.intersection(probability_a, probability_b) / probability_b
    
    def calculateTotalFavorableOutcomes(self, sample_space, favorableOutcomes) -> int:
        """
        Calculates the total number of favorable outcomes. Esto se hace
        de manera mas optima con math.comb(sample_space, favorableOutcomes), esto es una aplicacion para asentar
        conocimientos sobre estadistica y probabilidad.
        """
        return math.factorial(sample_space) / (math.factorial(favorableOutcomes) 
                                               * math.factorial(sample_space - favorableOutcomes))
    
    def calculateBinomialProbability(self, k, n, p) -> float:
        """
        Calculates the probability of k successes in n trials with probability p.
        """
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    
    def normalAproximationToBinomial(self, n, p) -> tuple:
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


    def normalProbability(self, x, mu, sigma) -> float:
        """
        Calculates the probability of a value in a normal distribution.
        """
        return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    def normalProbabilityRange(self, x1, x2, mu, sigma) -> float:   
        """
        Calculates the probability of a range of values in a normal distribution.
        """
        return self.normalProbability(x2, mu, sigma) - self.normalProbability(x1, mu, sigma)
    
    def calculate_value_probabilities(self, values) -> dict:
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