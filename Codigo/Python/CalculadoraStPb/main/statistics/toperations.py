from scipy import stats
class TOperations:
    def calculate_p_value_T(self, sample_data, population_mean, axis=0):
            return stats.ttest_1samp(sample_data, population_mean, axis=axis)
    
    def t_test(self, sample_data, population_mean):
        return self.calculate_p_value_T(sample_data, population_mean).statistic
    
    