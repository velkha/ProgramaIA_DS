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
            1: self.hypotesis_test,
        }
        return _switcher.get(_rtr, self.hypotesis_menu)()

    def start_menu(self) -> int:
        pass
    def hypotesis_test(self) -> None:
        self.data_processor.data = self.data_loader.data_check()
        if not self.data_processor.data:
            return
        self.hypotesis_test_menu()
    
    def hypotesis_test_menu(self) -> None:
        UIWorker.print("What kind of test do you want to perform?")
        UIWorker.print(["1. Check average of sample data in groups",
                        "2. Check variance of sample data in groups",
                        "3. Check proportion of sample data in groups",
                        "0. Back to previous menu"
                        ])
        option = int(UIWorker.input("Select an option: "))
        _switcher = {
            0: self.hypotesis_menu,
            1: self.check_average_of_sample_data_in_groups,
            2: self.check_variance_of_sample_data_in_groups,
            3: self.check_proportion_of_sample_data_in_groups
        }

        return _switcher.get(option, self.hypotesis_menu)()
    
    def check_average_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _averages = self.data_processor.average_by_key(self.group_key, self.value_key)
        for key, value in _averages.items():
            UIWorker.print(f"Average of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        return self.hypotesis_test_menu()

    def check_variance_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _variances = self.data_processor.variance_by_key(self.group_key, self.value_key)
        for key, value in _variances.items():
            UIWorker.print(f"Variance of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        return self.hypotesis_test_menu()

    def check_proportion_of_sample_data_in_groups(self) -> None:
        self.ask_keys()
        _proportions = self.data_processor.proportion_by_key(self.group_key, self.value_key)
        for key, value in _proportions.items():
            UIWorker.print(f"Proportion of {key}: {value}")
        UIWorker.input("Press Enter to continue...")
        return self.hypotesis_test_menu()
    
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