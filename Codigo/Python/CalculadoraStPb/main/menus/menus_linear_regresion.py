from utils.data_loader import DataLoader
from menus.menus_show import MenusShow
from utils.ui_worker import UIWorker
from linear_regresion.linear_r_operation import LinnearRegresionOperations
class MenusLinearRegresion:

    def __init__(self):
        self.data_loader = DataLoader()
        self.operations = LinnearRegresionOperations()

    def start_menu(self) -> int:
        pass

    def linear_regresion_menu(self) -> int:
        _rtr = MenusShow.linear_regresion_menu()
        _switcher = {
            1: self.set_data,
            2: self.plot_data,
            3: self.generate_summary,
            0: self.start_menu
        }
        return _switcher.get(int(_rtr), self.linear_regresion_menu)()
    
    def set_data(self) -> int:
        _data = self.data_loader.data_check(5)
        self.operations.set_data(_data)
        UIWorker.print("Data set.")
        UIWorker.input('Press Enter to continue...')
        self.linear_regresion_menu()

    def getColumnNames(self) -> tuple:
        UIWorker.print("Select the name of the y column")
        _y_column = UIWorker.input("Column name: ")
        UIWorker.print("Select the name of the x column")
        _x_column = UIWorker.input("Column name: ")
        return _x_column, _y_column
    def plot_data(self) -> int:
        if self.operations.data is None:
            UIWorker.print("No data has been set yet.")
            UIWorker.input('Press Enter to continue...')
            self.linear_regresion_menu()
        else:
            _x_column, _y_column = self.getColumnNames()
            self.operations.plot_data(_x_column, _y_column)
            UIWorker.input('Press Enter to continue...')
            self.linear_regresion_menu()

    def generate_summary(self) -> int:
        if self.operations.data is None:
            UIWorker.print("No data has been set yet.")
            UIWorker.input('Press Enter to continue...')
            self.linear_regresion_menu()
        else:
            _x_column, _y_column = self.getColumnNames()
            UIWorker.print(self.operations.generate_summary(_x_column, _y_column), 'Green')
            UIWorker.print("Summary generated.")
            UIWorker.input('Press Enter to continue...')
            self.linear_regresion_menu()