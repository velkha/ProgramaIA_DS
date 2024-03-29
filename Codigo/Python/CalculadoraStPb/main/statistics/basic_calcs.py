import math
import numpy as np

class BasicCalcs:
    '''All the basic statistical calculations for numerical data are implemented here.'''
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

    def calculate_mode(self, data):
        return max(data, key=data.count)

    def calculate_variance(self, data):
        mean = self.calculate_mean(data)
        squared_diffs = [(x - mean) ** 2 for x in data]
        return sum(squared_diffs) / len(data)

    def calculate_standard_deviation(self, data, sample=False):
        sample_correction = 1 if sample else 0
        return np.std(data, ddof=sample_correction)
    
    def calculate_standard_error(self, data):
        return self.calculate_standard_deviation(data) / math.sqrt(len(data))