import numpy as np
from scipy.stats import norm, t

import matplotlib.pyplot as plt

class GraphTransformer:
    def __init__(self, data):
        self.data = data

    def plot_normal_graph(self):
        mean = np.mean(self.data)
        std = np.std(self.data)
        x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
        y = norm.pdf(x, mean, std)
        plt.plot(x, y)
        plt.xlabel('Data')
        plt.ylabel('Probability')
        plt.title('Normal Distribution')
        plt.show()

    