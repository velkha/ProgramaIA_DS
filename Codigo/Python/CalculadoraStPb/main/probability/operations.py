
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