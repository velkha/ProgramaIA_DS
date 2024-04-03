from utils.data_loader import DataLoader
from menus.menus_show import MenusShow
from utils.ui_worker import UIWorker
import matplotlib.pyplot as plt
from utils.directory_worker import DirectoryWorker
class MenusLinearRegresion:

    def __init__(self):
        self.data_loader = DataLoader()

    def start_menu(self) -> int:
        pass

    def linear_regresion_menu(self) -> int:
        _rtr = MenusShow.linear_regresion_menu()
        _switcher = {
            1: self.plot_data,
            0: self.start_menu
        }
        return _switcher.get(int(_rtr), self.linear_regresion_menu)()
    
    def plot_data(self) -> int:
        _data = self.data_loader.data_check(5)
        UIWorker.print("Select the name of the y column")
        _y_column = UIWorker.input("Column name: ")
        UIWorker.print("Select the name of the x column")
        _x_column = UIWorker.input("Column name: ")
        _y = _data[_y_column]
        _x1 = _data[_x_column]
        plt.scatter(_x1, _y)
        plt.xlabel(_x_column, fontsize=20)
        plt.ylabel(_y_column, fontsize=20)
        plt.savefig(DirectoryWorker.secure_save('lrPlot', '.png'))
        plt.show()
        self.linear_regresion_menu()
