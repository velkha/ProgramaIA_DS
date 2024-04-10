import matplotlib.pyplot as plt
from utils.directory_worker import DirectoryWorker
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
sns.set_theme(style="whitegrid")

class LinnearRegresionOperations:

    def __init__(self):
        self.data = None
        self.model = None
        self.x_column = None
        self.y_column = None

    def set_data(self, data: pd.DataFrame):
        self.data = data

    def set_columns(self, x_column: str, y_column: str):
        self.x_column = x_column
        self.y_column = y_column

    def set_model(self, model=None):
        if model is None:
            _y = self.data[self.y_column]
            _x1 = self.data[self.x_column]
            _x = sm.add_constant(_x1)
            self.model = sm.OLS(_y, _x).fit()
        else:
            self.model = model

    def plot_data(self, constant=1) -> None:
        '''Plots the data of the columns given.'''
        _y = self.data[self.y_column]
        _x1 = self.data[self.x_column]
        plt.scatter(_x1, _y)
        plt.xlabel(self.x_column, fontsize=20)
        plt.ylabel(self.y_column, fontsize=20)
        plt.savefig(DirectoryWorker.secure_save('lrPlot', '.png'))
        plt.show()

    def generate_summary(self) -> any:
        '''Generates a summary of the linear regresion model.'''
        return self.model.summary()

    def plot_regresion(self) -> None:
        '''Plots the regresion of the columns given.'''
        _y = self.data[self.y_column]
        _x1 = self.data[self.x_column]

        yhat = self.model.params[0] + self.model.params[1] * _x1

        _lw = 4 # Line width
        plt.scatter(_x1, _y)
        plt.plot(_x1, yhat, lw=_lw, color='orange', label='regresion line')
        plt.xlabel(self.x_column, fontsize=20)
        plt.ylabel(self.y_column, fontsize=20)
        plt.savefig(DirectoryWorker.secure_save('lrPlot', '.png'))
        plt.show()
