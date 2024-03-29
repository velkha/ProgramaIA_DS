from menus.menus_show import MenusShow
from statistics.basic_calcs import BasicCalcs
from statistics.zoperations import ZOperations
from statistics.toperations import TOperations
from utils.ui_worker import UIWorker
class MenusStatistic:
    def statistics_menu(self) -> int:
        rtr = MenusShow.statistics_menu()
        switcher = {
            1: self.basic_calcs_menu,
            2: self.hypothesis_testing_menu,
            3: self.start_menu
        }
        return switcher.get(int(rtr), self.statistics_menu)()
    
    def basic_calcs_menu(self) -> int:
        rtr = MenusShow.basic_calcs_menu()
        switcher = {
            1: self.calculate_mean,
            2: self.calculate_median,
            3: self.calculate_mode,
            4: self.calculate_variance,
            5: self.calculate_standard_deviation,
            6: self.calculate_standard_error,
            7: self.statistics_menu
        }
        return switcher.get(rtr, self.basic_calcs_menu)()
    
    def hypothesis_testing_menu(self) -> int:
        rtr = MenusShow.hypothesis_testing_menu()
        switcher = {
            1: self.z_test,
            2: self.t_test,
            3: self.statistics_menu
        }
        return switcher.get(rtr, self.hypothesis_testing_menu)()
    
    def calculate_mean(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The mean of the data is {BasicCalcs().calculate_mean(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_median(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The median of the data is {BasicCalcs().calculate_median(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_mode(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The mode of the data is {BasicCalcs().calculate_mode(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_variance(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The variance of the data is {BasicCalcs().calculate_variance(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_standard_deviation(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The standard deviation of the data is {BasicCalcs().calculate_standard_deviation(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def calculate_standard_error(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        UIWorker.print([f'The standard error of the data is {BasicCalcs().calculate_standard_error(data)}'], "Blue")
        input('Press Enter to continue...')
        return self.basic_calcs_menu()
    
    def z_test(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        mu = float(input('Enter the population mean: '))
        sigma = float(input('Enter the population standard deviation: '))
        UIWorker.print([f'The Z-score of the data is {ZOperations().z_test(data, mu, sigma)}'], "Blue")
        input('Press Enter to continue...')
        return self.hypothesis_testing_menu()
    
    def t_test(self) -> None:
        data = list(map(float, input('Enter the data separated by spaces: ').split()))
        mu = float(input('Enter the population mean: '))
        UIWorker.print([f'The T-score of the data is {TOperations().t_test(data, mu)}'], "Blue")
        input('Press Enter to continue...')
        return self.hypothesis_testing_menu()
    

    
    def start_menu(self) -> int:
        pass
