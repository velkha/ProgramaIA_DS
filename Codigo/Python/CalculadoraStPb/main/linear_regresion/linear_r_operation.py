import matplotlib.pyplot as plt
from utils.directory_worker import DirectoryWorker
import pandas as pd
import statsmodels.api as sm

class LinnearRegresionOperations:

    def __init__(self):
        self.data = None
        self.model = None

    def set_data(self, data: pd.DataFrame):
        self.data = data

    def plot_data(self, x_column: str, y_column: str, constant=1) -> None:
        '''Plots the data of the columns given.'''
        _y = self.data[y_column]
        _x1 = self.data[x_column]
        plt.scatter(_x1, _y)
        plt.xlabel(x_column, fontsize=20)
        plt.ylabel(y_column, fontsize=20)
        plt.savefig(DirectoryWorker.secure_save('lrPlot', '.png'))
        plt.show()
    

    def generate_summary(self, x_column: str, y_column: str) -> any:
        '''Generates a summary of the linear regresion model.'''
        _y = self.data[y_column]
        _x1 = self.data[x_column]
        _x = sm.add_constant(_x1)
        self.model = sm.OLS(_y, _x).fit()
        return self.model.summary()