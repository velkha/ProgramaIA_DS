import math
import numpy as np
from scipy import stats

class StatisticCalcs:
    def __init__(self):
        pass

    def calculate_mean(self, data):
        return sum(data) / len(data)

    def calculate_median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def calculate_variance(self, data):
        mean = self.calculate_mean(data)
        squared_diffs = [(x - mean) ** 2 for x in data]
        return sum(squared_diffs) / len(data)

    def calculate_standard_deviation(self, data, sample=False):
        sample_correction = 1 if sample else 0
        return np.std(data, ddof=sample_correction)
    
    def calculate_standard_error(self, data):
        return self.calculate_standard_deviation(data) / math.sqrt(len(data))
    
    def calculate_p_value_T(self, sample_data, population_mean, axis=0):
        return stats.ttest_1samp(sample_data, population_mean, axis=axis)
    
    def calculate_p_value_Z(self, sample_data, population_mean, population_std, axis=0):
        n = len(sample_data)
        z_score = (self.calculate_mean(sample_data) - population_mean) / (population_std / np.sqrt(n))
        p_value_two_tailed = stats.norm.sf(abs(z_score)) * 2
        p_value_left = stats.norm.sf(abs(z_score))
        p_value_right = stats.norm.sf(-abs(z_score))
        return z_score, p_value_two_tailed, p_value_left, p_value_right
    
