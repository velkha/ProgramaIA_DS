import csv
from utils.ui_worker import UIWorker
class CsvReader:
    @staticmethod
    def read_csv_to_hashmap_w_headers(file_path, delimiter=';') -> dict:
        _hashmap = {}
        with open(file_path, 'r') as file:
            _csv_reader = csv.reader(file, delimiter=delimiter)  # Set the delimiter to ;
            _headers = next(_csv_reader)  # Get the column headers
            for header in _headers:
                _hashmap[header] = []  # Initialize an empty array for each column
            for row in _csv_reader:
                for i, value in enumerate(row):
                    _hashmap[_headers[i]].append(value)  # Append the value to the corresponding column
        return _hashmap

    @staticmethod
    def read_csv_to_array(file_path, delimiter=';') -> list:
        _array = []
        with open(file_path, 'r') as file:
            _csv_reader = csv.reader(file, delimiter=delimiter)
            for row in _csv_reader:
                _array.append(row[0])
        return _array

    @staticmethod
    def read_csv_to_bidimensional_array(file_path, delimiter=';') -> list:
        _bidimensional_array = []
        with open(file_path, 'r') as file:
            _csv_reader = csv.reader(file, delimiter=delimiter)
            for row in _csv_reader:
                _bidimensional_array.append(row)
        return _bidimensional_array

    @staticmethod
    def write_array_to_csv(file_path, array, delimiter=';') -> None:
        with open(file_path, 'w', newline='') as file:
            _csv_writer = csv.writer(file, delimiter=delimiter)
            for row in array:
                _csv_writer.writerow(row)

    @staticmethod
    def write_hashmap_to_csv(file_path, hashmap, delimiter=';') -> None:
        _headers = list(hashmap.keys())
        with open(file_path, 'w', newline='') as file:
            _csv_writer = csv.writer(file, delimiter=delimiter)
            _csv_writer.writerow(_headers)
            for i in range(len(hashmap[_headers[0]])):
                row = []
                for header in _headers:
                    row.append(hashmap[header][i])
                _csv_writer.writerow(row)

    @staticmethod
    def get_headers_from_csv(file_path, delimiter=';') -> list:
        with open(file_path, 'r') as file:
            _csv_reader = csv.reader(file, delimiter=delimiter)
            return next(_csv_reader)
        
    @staticmethod
    def ask_for_csv_data() -> list | dict:
        _file_path = UIWorker.input('Enter the path to the CSV file: ')
        _delimiter = UIWorker.input('Enter the delimiter of the CSV file (default is ;): ')
        _type_of_data = ''
        while _type_of_data not in ['1', '2', '3', '4']:
            UIWorker.print(['What type of data is in the CSV file?',
                            '1. Single column data',
                            '2. Multiple column data',
                            '3. Single column data with headers',
                            '4. Multiple column data with headers',
                            ])
            _type_of_data = UIWorker.input('Select an option: ')
            if _type_of_data not in ['1', '2', '3', '4']:
                UIWorker.print(['Invalid option. Please try again.'])
        if _delimiter == '':
            _delimiter = ';'
        return CsvReader.get_csv_data(_file_path, _delimiter, _type_of_data)
    
    @staticmethod
    def get_csv_data(file_path, delimiter, type_of_data=1) -> list | dict:
        '''
        Get the data from a CSV file, depending on the type of data it contains.
        1. Single column data
        2. Multiple column data
        3. Single column data with headers
        4. Multiple column data with headers
        '''
        if type_of_data == '1':
            return CsvReader.read_csv_to_array(file_path, delimiter)
        elif type_of_data == '2':
            return CsvReader.read_csv_to_bidimensional_array(file_path, delimiter)
        elif type_of_data == '3':
            return CsvReader.read_csv_to_hashmap_w_headers(file_path, delimiter)
        elif type_of_data == '4':
            return CsvReader.read_csv_to_hashmap_w_headers(file_path, delimiter)
        else:
            UIWorker.print(['Invalid option. Using default.'])
            return CsvReader.get_csv_data(file_path, delimiter)
    