from scipy import stats
import numpy as np
from statistics_operation.basic_calcs import BasicCalcs
class ZOperations:
    #todo: correct method signature
    def calculate_p_value_Z(self, sample_data, population_mean, population_std, axis=0):
        _n = len(sample_data)
        _z_score = (BasicCalcs.calculate_mean(sample_data) - population_mean) / (population_std / np.sqrt(_n))
        _p_value_two_tailed = stats.norm.sf(abs(_z_score)) * 2
        _p_value_left = stats.norm.sf(abs(_z_score))
        _p_value_right = stats.norm.sf(-abs(_z_score))
        return _z_score, _p_value_two_tailed, _p_value_left, _p_value_right
    
    def z_test(self, sample_data, population_mean, population_std):
        return self.calculate_p_value_Z(sample_data, population_mean, population_std)[0]