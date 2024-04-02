from utils.csv_reader import CsvReader
from utils.ui_worker import UIWorker


class DataLoader:
    def __init__(self, data: list = []):
        self.data = data
    def data_check(self) -> list | dict:
        if len(self.data) == 0:
            self.data=CsvReader.ask_for_csv_data()
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
                self.data=CsvReader.ask_for_csv_data()
        return self.data
    
    def get_Numeric_Data(self) -> list:
        self.data_check()
        self.data = [float(x) for x in self.data]
        return self.data
        