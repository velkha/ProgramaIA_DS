import numpy as np
import math
from scipy.stats import norm, t
import matplotlib.pyplot as plt

class StudentsT:
    def __init__(self):
        pass

    def calculate_confidence_level(self, confidence, data):
        n = len(data)
        degrees_of_freedom = n - 1
        t_critical = np.abs(t.ppf((1 - confidence) / 2, degrees_of_freedom))
        margin_of_error = t_critical * np.std(self.data) / math.sqrt(n)
        confidence_interval = (np.mean(data) - margin_of_error, np.mean(self.data) + margin_of_error)
        return confidence_interval

    def plot_t_graph(self, degrees_of_freedom, data):
        mean = np.mean(data)
        std = np.std(data)
        x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
        y = t.pdf(x, degrees_of_freedom, mean, std)
        plt.plot(x, y)
        plt.xlabel('Data')
        plt.ylabel('Probability')
        plt.title(f'Student\'s T Distribution (df={degrees_of_freedom})')
        plt.show()