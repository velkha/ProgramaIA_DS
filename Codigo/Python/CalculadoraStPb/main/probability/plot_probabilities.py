import numpy as np
from scipy.stats import binom
from utils.ui_worker import UIWorker
from utils.directory_worker import DirectoryWorker
from probability.operations import ProbabilityOperations
import matplotlib.pyplot as plt

class ProbabilityPlotter:
    def plot_binomial_probability(self, n: float, p: float):
        _x = np.arange(0, n+1)
        _y = binom.pmf(_x, n, p)

        plt.bar(_x, _y)
        plt.xlabel('Number of Successes')
        plt.ylabel('Probability')
        plt.title('Binomial Probability Distribution')
        plt.savefig(DirectoryWorker.secure_save('probabilityplot', '.png'))
        UIWorker.print('The plot has been saved', "Blue")

    def plot_probabilities_histogram(self, data: list | dict):

        if not isinstance(data, dict):
            operator = ProbabilityOperations()
            _data = operator.calculate_value_probabilities(data)
        else:
            _data = data

        outcomes = list(_data.keys())
        probabilities = list(_data.values())

        plt.bar(outcomes, probabilities)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.xticks(outcomes)
        plt.title('Probability Distribution Histogram')
        plt.savefig(DirectoryWorker.secure_save('probabilityhistogram', '.png'))
        UIWorker.print('The plot has been saved', "Blue")