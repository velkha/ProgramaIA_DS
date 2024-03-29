import numpy as np
from scipy.stats import norm, t

import matplotlib.pyplot as plt

class ShowGraphs:
    def __init__(self):
        pass

    def plot_normal_graph(self, data, save=False, filename=None):
        mean = np.mean(data)
        std = np.std(data)
        x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
        y = norm.pdf(x, mean, std)
        plt.plot(x, y)
        plt.xlabel('Data')
        plt.ylabel('Probability')
        plt.title('Normal Distribution')
        if save:
            plt.savefig(filename)
        plt.show()

    def plot_t_graph(self, data, save=False, filename=None):
        df = 10
        # Normalize the data by subtracting the mean and dividing by the standard deviation
        standardized_data = round((data - np.mean(data)) / np.std(data, ddof=1), 3)
        # Generate values on the x axis
        x = round(np.linspace(min(standardized_data) - 4, max(standardized_data) + 4, 1000), 3)
        # Generate the pdf for the t distribution with df degrees of freedom
        pdf = t.pdf(x, df)
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(x, pdf, label=f't-distribution (df={df})')
        # Plot the standardized data on the x-axis
        plt.scatter(standardized_data, np.zeros_like(standardized_data), color='red', label='Data Points')
        # Adding labels and title
        plt.title('PDF of Student\'s t-Distribution with Sample Data Overlay')
        plt.xlabel('Value')
        plt.ylabel('Probability Density')
        plt.legend()
        # Save the plot if requested
        if save:
            plt.savefig(filename)

        # Show the plot
        plt.show()
        

    def plot_data(self, data, save=False, filename=None):
        plt.hist(data, bins='auto')
        plt.xlabel('Data')
        plt.ylabel('Frequency')
        plt.title('Data Distribution')
        if save:
            plt.savefig(filename)
            
        plt.show()

    