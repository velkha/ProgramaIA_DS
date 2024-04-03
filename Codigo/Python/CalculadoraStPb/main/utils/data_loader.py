from utils.csv_reader import CsvReader
from utils.ui_worker import UIWorker


class DataLoader:
    def __init__(self, data: list = []):
        self.data = data
    def data_check(self, pre_select=-1) -> list | dict:
        '''If preselect is present it will select that option from the csv file types
            pre_select values: int
                1. Single column data
                2. Multiple column data
                3. Single column data with headers
                4. Multiple column data with headers
                5. Load the CSV file into a pandas DataFrame
        '''
        if len(self.data) == 0:
            self.data=CsvReader.ask_for_csv_data(pre_select)
        else:
            UIWorker.print(['Data already loaded.'])
            UIWorker.print(['Would you like to use the loaded data or load a new file?',
                            '1. Use the loaded data',
                            '2. Load a new file'
                            ])
            option = UIWorker.input('Select an option: ')
            while option not in ['1', '2']:
                UIWorker.print(['Invalid option. Please try again.'])
                option = UIWorker.input('Select an option: ')
            if option == '2':
                self.data=CsvReader.ask_for_csv_data(pre_select)
        return self.data
    
    def get_Numeric_Data(self) -> list:
        self.data_check()
        self.data = [float(x) for x in self.data]
        return self.data
        