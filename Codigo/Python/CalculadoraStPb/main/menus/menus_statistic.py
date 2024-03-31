from menus.menus_show import MenusShow
from statistics.basic_calcs import BasicCalcs
from statistics.zoperations import ZOperations
from statistics.toperations import TOperations
from utils.ui_worker import UIWorker
from utils.csv_reader import CsvReader

class MenusStatistic:

    def __init__(self):
        self.data = []

    def statistics_menu(self) -> int:
        _rtr = MenusShow.statistics_menu()
        _switcher = {
            1: self.basic_calcs_menu,
            2: self.hypothesis_testing_menu,
            3: self.start_menu
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
    
    def calculate_mean(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The mean of the data is {BasicCalcs().calculate_mean(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_median(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The median of the data is {BasicCalcs().calculate_median(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_mode(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The mode of the data is {BasicCalcs().calculate_mode(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_variance(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The variance of the data is {BasicCalcs().calculate_variance(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_standard_deviation(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The standard deviation of the data is {BasicCalcs().calculate_standard_deviation(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_standard_error(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The standard error of the data is {BasicCalcs().calculate_standard_error(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def z_test(self) -> None:
        _data=self.data_check()
        _mu = float(input('Enter the population mean: '))
        _sigma = float(input('Enter the population standard deviation: '))
        UIWorker.print([f'The Z-score of the data is {ZOperations().z_test(_data, _mu, _sigma)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.hypothesis_testing_menu()
    
    def t_test(self) -> None:
        _data=self.data_check()
        _mu = float(input('Enter the population mean: '))
        UIWorker.print([f'The T-score of the data is {TOperations().t_test(_data, _mu)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.hypothesis_testing_menu()
    
    def calculate_skewness(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The skewness of the data is {BasicCalcs().calculate_skewness(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_percentiles(self) -> None:
        _data=self.data_check()
        percentiles = [float(x) for x in input('Enter the percentiles separated by spaces: ').split()]
        UIWorker.print([f'The percentiles of the data are {BasicCalcs().calculate_percentiles(_data, _percentiles)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_quartiles(self) -> None:
        _data=self.data_check()
        UIWorker.print([f'The quartiles of the data are {BasicCalcs().calculate_quartiles(_data)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_value_for_percentile(self) -> None:
        _data=self.data_check()
        _percentile = float(input('Enter the percentile: '))
        UIWorker.print([f'The value for the percentile of the data is {BasicCalcs().calculate_value_for_percentile(_data, _percentile)}'], "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    

    def start_menu(self) -> int:
        pass

    def data_check(self) -> list | dict:
        if len(self.data) == 0:
            self.data=CsvReader.ask_for_csv_data()
        else:
            UIWorker.print(['Data already loaded.'])
            UIWorker.print(['Would you like to use the loaded data or load a new file?',
                            '1. Use the loaded data',
                            '2. Load a new file'
                            ])
            option = UIWorker.input('Select an option: ')
            while option not in ['1', '2']:
                UIWorker.print(['Invalid option. Please try again.'])
                option = UIWorker.input('Select an option: ')
            if option == '2':
                self.data=self.data_check()
        
        self.data = [float(x) for x in self.data]
        return self.data
