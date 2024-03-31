import math
import numpy as np

class BasicCalcs:
    '''All the basic statistical calculations for numerical data are implemented here.'''
    def __init__(self):
        pass

    def calculate_mean(self, data):
        return sum(data) / len(data)

    def calculate_median(self, data):
        _sorted_data = sorted(data)
        _n = len(_sorted_data)
        if _n % 2 == 0:
            return (_sorted_data[_n // 2 - 1] + _sorted_data[_n // 2]) / 2
        else:
            return _sorted_data[_n // 2]

    def calculate_mode(self, data):
        return max(data, key=data.count)

    def calculate_variance(self, data):
        _mean = self.calculate_mean(data)
        _squared_diffs = [(x - _mean) ** 2 for x in data]
        return sum(_squared_diffs) / len(data)

    def calculate_standard_deviation(self, data, sample=False):
        _sample_correction = 1 if sample else 0
        return np.std(data, ddof=_sample_correction)
    
    def calculate_standard_error(self, data):
        return self.calculate_standard_deviation(data) / math.sqrt(len(data))
    
    def calculate_skewness(self, data):
        _mean = self.calculate_mean(data)
        _variance = self.calculate_variance(data)
        _n = len(data)
        return sum([(x - _mean) ** 3 for x in data]) / (_n * _variance ** 1.5)
    
    def calculate_percentiles(self, data, percentiles):
        _sorted_data = sorted(data)
        _n = len(_sorted_data)
        return [_sorted_data[int(p * _n)] for p in percentiles]
    
    def calculate_quartiles(self, data):
        return self.calculate_percentiles(data, [0.25, 0.5, 0.75])
    
    def calculate_value_for_percentile_with_mean_and_standard(self, mean, standard_deviation, percentile):
        return mean + standard_deviation * math.erfinv(2 * percentile - 1) * math.sqrt(2)