import numpy as np
from scipy.stats import binom
from utils.ui_worker import UIWorker
from utils.directory_worker import DirectoryWorker
import matplotlib.pyplot as plt

class ProbabilityPlotter:
    def plot_binomial_probability(self, n, p):
        _x = np.arange(0, n+1)
        _y = binom.pmf(_x, n, p)

        plt.bar(_x, _y)
        plt.xlabel('Number of Successes')
        plt.ylabel('Probability')
        plt.title('Binomial Probability Distribution')
        plt.savefig(DirectoryWorker.secure_save('probabilityplot', '.png'))
        UIWorker.print('The plot has been saved', "Blue")
