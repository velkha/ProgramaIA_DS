from menus.menus_show import MenusShow
from statistics.basic_calcs import BasicCalcs
from statistics.zoperations import ZOperations
from statistics.toperations import TOperations
from utils.ui_worker import UIWorker
from utils.csv_reader import CsvReader
from utils.data_loader import DataLoader

class MenusStatistic:

    def __init__(self):
        self.data_loader = DataLoader()

    def statistics_menu(self) -> int:
        _rtr = MenusShow.statistics_menu()
        _switcher = {
            1: self.basic_calcs_menu,
            2: self.hypothesis_testing_menu,
            3: self.sum_operations_menu,
            0: self.start_menu
        }
        return _switcher.get(int(_rtr), self.statistics_menu)()
    
    def basic_calcs_menu(self) -> int:
        _rtr = MenusShow.basic_calcs_menu()
        _switcher = {
            0: self.statistics_menu,
            1: self.calculate_mean,
            2: self.calculate_median,
            3: self.calculate_mode,
            4: self.calculate_variance,
            5: self.calculate_standard_deviation,
            6: self.calculate_standard_error,
            7: self.calculate_skewness,
            8: self.calculate_percentiles,
            9: self.calculate_quartiles,
            10: self.calculate_value_for_percentile,
            11: self.calculate_probability_more_than,
            12: self.get_everything_w_pandas,
            13: self.calculate_probability_sum_more_than,
            14: self.calculatePercentajeStandaricedCurve

        }
        return _switcher.get(_rtr, self.basic_calcs_menu)()
    
    def hypothesis_testing_menu(self) -> int:
        _rtr = MenusShow.hypothesis_testing_menu()
        _switcher = {
            1: self.z_test,
            2: self.t_test,
            3: self.statistics_menu
        }
        return _switcher.get(_rtr, self.hypothesis_testing_menu)()
    
    def sum_operations_menu(self) -> int:
        _rtr = MenusShow.sum_operations_menu()
        _switcher = {
            1: self.calculate_sum,
            2: self.calculate_sum_standard_error,
            3: self.calculate_sum_confidence_interval,
            4: self.calculate_sum_expected_value,
            5: self.calculate_probability_sum_more_than,
            0: self.statistics_menu
        }
        return _switcher.get(_rtr, self.sum_operations_menu)()

    def calculate_mean(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The mean of the data is {BasicCalcs().calculate_mean(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_median(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The median of the data is {BasicCalcs().calculate_median(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_mode(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The mode of the data is {BasicCalcs().calculate_mode(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_variance(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The variance of the data is {BasicCalcs().calculate_variance(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_standard_deviation(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The standard deviation of the data is {BasicCalcs().calculate_standard_deviation(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_standard_error(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The standard error of the data is {BasicCalcs().calculate_standard_error(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def z_test(self) -> None:
        _data=self.data_loader.data_check()
        _mu = float(input('Enter the population mean: '))
        _sigma = float(input('Enter the population standard deviation: '))
        UIWorker.print([f'The Z-score of the data is {ZOperations().z_test(_data, _mu, _sigma)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.hypothesis_testing_menu()
    
    def t_test(self) -> None:
        _data=self.data_loader.data_check()
        _mu = float(input('Enter the population mean: '))
        UIWorker.print([f'The T-score of the data is {TOperations().t_test(_data, _mu)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.hypothesis_testing_menu()
    
    def calculate_skewness(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The skewness of the data is {BasicCalcs().calculate_skewness(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_percentiles(self) -> None:
        _data=self.data_loader.data_check()
        _percentiles = [float(x) for x in input('Enter the percentiles separated by spaces: ').split()]
        UIWorker.print([f'The percentiles of the data are {BasicCalcs().calculate_percentiles(_data, _percentiles)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_quartiles(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The quartiles of the data are {BasicCalcs().calculate_quartiles(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_value_for_percentile(self) -> None:
        _data=self.data_loader.data_check()
        _percentile = float(input('Enter the percentile: '))
        UIWorker.print([f'The value for the percentile of the data is {BasicCalcs().calculate_value_for_percentile(_data, _percentile)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()
    
    def calculate_sum(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The sum of the data is {BasicCalcs().calculate_sum(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.sum_operations_menu()
    
    def calculate_sum_standard_error(self) -> None:
        _data=self.data_loader.data_check()
        _probability = float(input('Enter the probability: '))
        UIWorker.print([f'The sum standard error of the data is {BasicCalcs().calculate_sum_standard_error(_data, _probability)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.sum_operations_menu()
    
    def calculate_sum_confidence_interval(self) -> None:
        _data=self.data_loader.data_check()
        UIWorker.print([f'The sum confidence interval of the data is {BasicCalcs().calculate_sum_confidence_interval(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.sum_operations_menu()
    
    def calculate_sum_expected_value(self) -> None:
        _data=self.data_loader.data_check()
        _probability = float(input('Enter the probability: '))
        UIWorker.print([f'The sum expected value of the data is {BasicCalcs().calculate_sum_expected_value(_data, _probability)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.sum_operations_menu()

    def calculate_probability_more_than(self) -> None:
        _sample_size = int(input('Enter the sample size: '))
        _mean = float(input('Enter the mean: '))
        _standard_deviation = float(input('Enter the standard deviation: '))
        _value = float(input('Enter the value: '))
        UIWorker.print([f'The probability of the data is {BasicCalcs().calculate_probability_more_than(_sample_size, _mean, _standard_deviation, _value)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()

    def calculate_probability_sum_more_than(self) -> None:
        _sample_size = int(input('Enter the sample size: '))
        _mean = float(input('Enter the mean: '))
        _standard_deviation = float(input('Enter the standard deviation: '))
        _value = float(input('Enter the value: '))
        UIWorker.print([f'The probability of the data is {BasicCalcs().calculate_probability_sum_more_than(_sample_size, _mean, _standard_deviation, _value)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.sum_operations_menu()
    
    def get_everything_w_pandas(self) -> None:
        _date_frame = self.data_loader.data_check(5)
        UIWorker.print(_date_frame.describe())
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()

    def calculatePercentajeStandaricedCurve(self) -> None:
        _value = float(input('Enter the value: '))
        _rtr = BasicCalcs().calculatePercentajeStandaricedCurve(_value)
        UIWorker.print(['The probability of the data is: ', f'left side: {_rtr*100}', f'right side: {(1-_rtr)*100}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        self.basic_calcs_menu()

    def start_menu(self) -> int:
        pass

