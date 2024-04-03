from menus.menus_show import MenusShow
from utils.data_loader import DataLoader
from hypotesis_testing.data_processor import DataProcessor
from utils.ui_worker import UIWorker


class MenusHypotesis:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_processor = DataProcessor()
        self.group_key = ""
        self.value_key = ""

    def hypotesis_menu(self) -> int:
        _rtr = MenusShow.hypotesis_menu()
        _switcher = {
            0: self.start_menu,
            1: self.hypotesis_test_simple,
            2: self.hypotesis_test_full_data
        }
        return _switcher.get(_rtr, self.hypotesis_menu)()

    def start_menu(self) -> int:
        pass
    def hypotesis_test_simple(self) -> None:
        self.data_processor.data = self.data_loader.data_check()
        if not self.data_processor.data:
            return
        self.hypotesis_test_simple_menu()
    
    def hypotesis_test_simple_menu(self) -> None:
        _rtr = MenusShow.hypotesis_test_simple_menu()
        _switcher = {
            0: self.hypotesis_menu,
            1: self.check_average_of_sample_data_in_groups,
            2: self.check_variance_of_sample_data_in_groups,
            3: self.check_proportion_of_sample_data_in_groups
        }

        return _switcher.get(_rtr, self.hypotesis_menu)()
    
    def check_average_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _averages = self.data_processor.average_by_key(self.group_key, self.value_key)
        for key, value in _averages.items():
            UIWorker.print(f"Average of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        self.hypotesis_test_simple_menu()

    def check_variance_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _variances = self.data_processor.variance_by_key(self.group_key, self.value_key)
        for key, value in _variances.items():
            UIWorker.print(f"Variance of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        self.hypotesis_test_simple_menu()

    def check_proportion_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _proportions = self.data_processor.proportion_by_key(self.group_key, self.value_key)
        for key, value in _proportions.items():
            UIWorker.print(f"Proportion of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        self.hypotesis_test_simple_menu()
    
    def ask_keys(self) -> tuple[str, str]:
        if self.group_key and self.value_key:
            UIWorker.print("Keys already exist. Do you want to override them?")
            _option = UIWorker.input("Y/N: ")
            if _option.lower() == "n":
                return self.group_key, self.value_key
        UIWorker.print("This are the keys of the data you have loaded:")
        UIWorker.print(self.data_processor.data[0].keys())
        UIWorker.print("Give me the key of the group you want to check. If it is a multikey group, separate them with a ';'.")
        self.group_key = UIWorker.input("Key/s to compare: ")
        UIWorker.print("Give me the key of the value you want to check.")
        self.value_key = UIWorker.input("Value Key: ")
        return self.group_key, self.value_key
    
    def hypotesis_test_full_data(self) -> None:
        self.data_processor.data = self.data_loader.data_check()
        if not self.data_processor.data:
            return
        self.hypotesis_test_full_data_menu()

    def hypotesis_test_full_data_menu(self) -> None:
        _rtr = MenusShow.hypotesis_test_full_data_menu()
        _switcher = {
            0: self.hypotesis_menu,
            1: self.compare_keys_values,
        }

        _switcher.get(_rtr, self.hypotesis_menu)()
    
    def compare_keys_values(self) -> None:
        self.ask_keys()
        UIWorker.print("Expected value of null hypothesis: ")
        _expected_value = UIWorker.input("Expected value: ")
        _rtr = self.data_processor.compare_key_values(self.group_key, self.value_key, float(_expected_value))
        if not _rtr or not _rtr[0]:
            UIWorker.print("There was an error with the data. Please try again.")
        else:
            UIWorker.print("Results:")
            for key, value in _rtr[0].items():
                UIWorker.print(f"Key: {key}, Value: {value}")
            UIWorker.print(f"Pooled Values: {_rtr[1]} ")
        
        UIWorker.input("Press Enter to continue...")
        self.hypotesis_test_full_data_menu()
