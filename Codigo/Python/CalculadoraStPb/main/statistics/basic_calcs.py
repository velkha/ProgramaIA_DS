import math
import numpy as np
import pandas as pd
class BasicCalcs:
    '''All the basic statistical calculations for numerical data are implemented here.'''
    def __init__(self):
        pass

    def calculate_mean(self, data: list) -> float:
        return sum(data) / len(data)

    def calculate_median(self, data: list) -> float:
        _sorted_data = sorted(data)
        _n = len(_sorted_data)
        if _n % 2 == 0:
            return (_sorted_data[_n // 2 - 1] + _sorted_data[_n // 2]) / 2
        else:
            return _sorted_data[_n // 2]

    def calculate_mode(self, data: list) -> float:
        return max(data, key=data.count)

    def calculate_variance(self, data: list) -> float:
        _mean = self.calculate_mean(data)
        _squared_diffs = [(x - _mean) ** 2 for x in data]
        return sum(_squared_diffs) / len(data)

    def calculate_standard_deviation(self, data: list, sample=False) -> float:
        _sample_correction = 1 if sample else 0
        return np.std(data, ddof=_sample_correction)
    
    def calculate_standard_error(self, data: list) -> float:
        return self.calculate_standard_deviation(data) / math.sqrt(len(data))
    
    def calculate_skewness(self, data: list) -> float:
        _mean = self.calculate_mean(data)
        _variance = self.calculate_variance(data)
        _n = len(data)
        return sum([(x - _mean) ** 3 for x in data]) / (_n * _variance ** 1.5)
    
    def calculate_percentiles(self, data: list, percentiles: float) -> list:
        _sorted_data = sorted(data)
        _n = len(_sorted_data)
        return [_sorted_data[int(p * _n)] for p in percentiles]
    
    def calculate_quartiles(self, data: list) -> list:
        return self.calculate_percentiles(data, [0.25, 0.5, 0.75])
    
    def calculate_value_for_percentile_with_mean_and_standard(self, mean: float, standard_deviation: float, percentile: float):
        return mean + standard_deviation * math.erfinv(2 * percentile - 1) * math.sqrt(2)
    
    def calculate_sum(self, data: list) -> float:
        return sum(data)
    
    def calculate_sum_standard_error(self, data: list, probabilities) -> float:
        if isinstance(probabilities, float):
            probabilities = [probabilities] * len(data)
        _mean = self.calculate_mean(data)
        rtrvalue = sum([(x - _mean)**2 * p for x, p in zip(data, probabilities)])
        rtrStandardError = math.sqrt(rtrvalue)
        return math.sqrt(len(data)) * rtrStandardError
        #return math.sqrt(sum([p ** 2 * x for x, p in zip(data, probabilities)]))
        
    def calculate_sum_confidence_interval(self, data: list, alpha=0.05) -> tuple:
        _mean = self.calculate_mean(data)
        _standard_error = self.calculate_standard_error(data)
        _z_score = 1.96
        _margin_of_error = _z_score * _standard_error
        return _mean - _margin_of_error, _mean + _margin_of_error
    
    def calculate_sum_expected_value(self, data: list, probabilities: float | list):
        if isinstance(probabilities, float):
            probabilities = [probabilities] * len(data)
        #zip function is used to combine data and probabilities into a single list of tuples.
        return sum([x * p for x, p in zip(data, probabilities)])
    
    def calculate_probability_more_than(self, mean: float, standard_deviation: float, value: float):
        z_score = (value - mean) / standard_deviation
        probability = 1 - self.calculate_cumulative_probability(z_score)
        return probability

    def calculate_cumulative_probability(self, z_score):
        return 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
    
    def calculate_probability_sum_more_than(self, sample_size: float, mean: float, standard_deviation: float, value: float):
        z_score = (value - (mean * sample_size)) / (standard_deviation * math.sqrt(sample_size))
        probability = 1 - self.calculate_cumulative_probability(z_score)
        return probability
    
    def get_all_w_pd(self, dataFrame: pd.DataFrame) -> pd.DataFrame:
        return dataFrame.describe()