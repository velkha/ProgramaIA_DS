from utils.CsvReader import CsvReader
import os



test = CsvReader()
"""check file path first """
file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, 'data.csv')
if os.path.isfile(file_path):
    print(f"{file_path} exists in the filepath.")
    print(test.read_csv_to_hashmap(file_path))
else:
    print(f"{file_path} does not exist in the filepath.")
    current_path = os.path.abspath(__file__)
    print(f"The current working directory is: {current_path}")
