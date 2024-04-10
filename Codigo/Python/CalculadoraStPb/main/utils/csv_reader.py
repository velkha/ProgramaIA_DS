import csv
from utils.ui_worker import UIWorker
import pandas as pd
import os
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

    def read_csv_to_object(file_path, delimiter=';') -> list:
        _object_list = []
        with open(file_path, 'r') as file:
            _csv_reader = csv.reader(file, delimiter=delimiter)
            _headers = next(_csv_reader)
            for row in _csv_reader:
                _object = {}
                for i, value in enumerate(row):
                    _object[_headers[i]] = value
                _object_list.append(_object)
        return _object_list

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
    def ask_for_csv_data(pre_select=-1) -> list | dict:
        _file_path = UIWorker.input('Enter the path to the CSV file: ')
        if not _file_path.endswith('.csv'):
            _file_path += '.csv'
        while not os.path.isfile(_file_path):
            UIWorker.print(['File not found. Please try again.'])
            _file_path = UIWorker.input('Enter the path to the CSV file: ')
            if not _file_path.endswith('.csv'):
                _file_path += '.csv'
    
        _delimiter = UIWorker.input('Enter the delimiter of the CSV file (default is ;): ')
        _type_of_data = pre_select

        if _type_of_data == -1:
            while _type_of_data not in ['1', '2', '3', '4', '5']:
                UIWorker.print(['What type of data is in the CSV file?',
                                '1. Single column data',
                                '2. Multiple column data',
                                '3. Single column data with headers',
                                '4. Multiple column data with headers',
                                '5. Load the CSV file into a pandas DataFrame'
                                ])
                _type_of_data = UIWorker.input('Select an option: ')
                if _type_of_data not in ['1', '2', '3', '4' , '5']:
                    UIWorker.print(['Invalid option. Please try again.'])

        if _delimiter == '':
            _delimiter = ';'
        _rtr = CsvReader.get_csv_data(_file_path, _delimiter, _type_of_data)
        return _rtr
    
    @staticmethod
    def get_csv_data(file_path: str, delimiter: str, type_of_data: str) -> list | dict:
        '''
        Get the data from a CSV file, depending on the type of data it contains.
        1. Single column data
        2. Multiple column data
        3. Single column data with headers
        4. Multiple column data with headers
        5. Load the CSV file into a pandas DataFrame
        '''
        if type_of_data == 1:
            return CsvReader.read_csv_to_array(file_path, delimiter)
        elif type_of_data == 2:
            return CsvReader.read_csv_to_bidimensional_array(file_path, delimiter)
        elif type_of_data == 3:
            rtr = CsvReader.read_csv_to_hashmap_w_headers(file_path, delimiter)
            if rtr.keys().__len__() == 1:
                return rtr[list(rtr.keys())[0]]
            else:
                return CsvReader.choose_header_for_single_in_multiple(rtr)
        elif type_of_data == 4:
            return CsvReader.read_csv_to_object(file_path, delimiter)
        elif type_of_data == 5:
            return CsvReader.csv_to_dataframe_pd(file_path, delimiter)
        else:
            UIWorker.print(['Invalid option. Returning None.'])
            return None
    
    def choose_header_for_single_in_multiple(rtr: dict) -> list:
        '''Choose a header from a dictionary with multiple headers. To return only that column.'''
        _keys = list(rtr.keys())
        _selected_column = None
        while _selected_column is None:
            UIWorker.print(['Multiple headers detected:'])
            for i, key in enumerate(_keys):
                UIWorker.print([f'{i+1}. {key}'])
            _selected_option = UIWorker.input('Select a header by number: ')
            try:
                _selected_index = int(_selected_option) - 1
                if _selected_index >= 0 and _selected_index < len(_keys):
                    _selected_column = _keys[_selected_index]
                else:
                    UIWorker.print(['Invalid option. Please try again.'])
                    _selected_column = None
            except ValueError:
                UIWorker.print(['Invalid option. Please try again.'])
        return rtr[_selected_column]
    
    def csv_to_dataframe_pd(file_path: str, delimiter: str) -> pd.DataFrame:
        '''Read a CSV file into a pandas DataFrame.'''
        try:
            return pd.read_csv(file_path, delimiter=delimiter)
        except FileNotFoundError:
            return pd.DataFrame()
    