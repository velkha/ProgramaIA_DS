from utils.CsvReader import CsvReader
import os
from utils.ShowGraphs import ShowGraphs
from utils.StatisticCalcs import StatisticCalcs

def processData(data):
    rtrStr = []
    graphMaker = ShowGraphs()
    print("Data processing")
    print(f"Data: {data}")
    stats = StatisticCalcs()
    mean = round(stats.calculate_mean(data), 3)
    median = round(stats.calculate_median(data), 3)
    variance = round(stats.calculate_variance(data), 3)
    standard_deviation = round(stats.calculate_standard_deviation(data), 3)
    standard_error = round(stats.calculate_standard_error(data), 3)
    ttest, p_value = stats.calculate_p_value_T(data, 113000)
    zttest = stats.calculate_p_value_Z(data, 113000, 15000)
    rtrStr.append(f"Mean: {mean}")
    rtrStr.append(f"Median: {median}")
    rtrStr.append(f"Variance: {variance}")
    rtrStr.append(f"Standard Deviation: {standard_deviation}")
    rtrStr.append(f"Standard Error: {standard_error}")
    rtrStr.append(f"t-test: {ttest}")
    rtrStr.append(f"p-value: {p_value}")
    rtrStr.append("Z----")
    rtrStr.append(f"Z-test: {zttest}")
    saveArrayToFile(rtrStr, 'output.txt')
    graphMaker.plot_normal_graph(data, save=True, filename='data_distribution.png')
    

def saveArrayToFile(array, filename):
    with open(filename, 'w') as file:
        for item in array:
            file.write(item + '\n')
    print(f"Array saved to {filename}")




test = CsvReader()
"""check file path first """
file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, 'data1.csv')
if os.path.isfile(file_path):
    print(f"{file_path} exists in the filepath.")
    test_data = test.read_csv_to_hashmap(file_path)
    keys = list(test_data.keys())
    integer_data = [int(i) for i in test_data[keys[0]]]
    graphMaker = ShowGraphs()
    processData(integer_data)
else:
    print(f"{file_path} does not exist in the filepath.")
    current_path = os.path.abspath(__file__)
    print(f"The current working directory is: {current_path}")

