from scipy import stats
import numpy as np
from statistics.basic_calcs import BasicCalcs
class ZOperations:
    def calculate_p_value_Z(self, sample_data, population_mean, population_std, axis=0):
        n = len(sample_data)
        z_score = (BasicCalcs.calculate_mean(sample_data) - population_mean) / (population_std / np.sqrt(n))
        p_value_two_tailed = stats.norm.sf(abs(z_score)) * 2
        p_value_left = stats.norm.sf(abs(z_score))
        p_value_right = stats.norm.sf(-abs(z_score))
        return z_score, p_value_two_tailed, p_value_left, p_value_right
    
    def z_test(self, sample_data, population_mean, population_std):
        return self.calculate_p_value_Z(sample_data, population_mean, population_std)[0]