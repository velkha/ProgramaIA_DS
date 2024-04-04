from typing import List
import os
from utils.file_worker import FileWorker
from datetime import datetime
import pandas as pd
from utils.directory_worker import DirectoryWorker
class UIWorker:
    COLOR_CODES = {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m',
        }
    '''Class to handle user interaction with the app, in the future if other way of UI is needed change from this class using it as conector.'''	
    @staticmethod
    def print(_text: any, _color: str = 'white', _save: bool = True) -> None:
        switcher = {
            pd.DataFrame: UIWorker.print_pandas,
            str: UIWorker.print_normal,
            list: UIWorker.print_normal
        }
        handler = switcher.get(type(_text), UIWorker.print_unknown)
        handler(_text, _color, _save)

    @staticmethod
    def print_normal(text: List[str] | str, color: str = 'white', save: bool = True) -> None:
        
        if isinstance(text, str):
            text = [text]

        for t in text:
            print(f"{UIWorker.COLOR_CODES[color.lower()]}{t}{UIWorker.COLOR_CODES['reset']}")
        if save:
            _current_date = datetime.now()
            _date_string = _current_date.strftime("%Y%m%d")
            FileWorker.write_file(f'output{_date_string}.txt', text)
            FileWorker.write_file(f'output{_date_string}.txt', "--- END OF OUTPUT ---")

    @staticmethod
    def print_pandas(text: pd.DataFrame, color: str = 'white', save: bool = True) -> None:
        print (text)
        if save:
            _current_date = datetime.now()
            _date_string = _current_date.strftime("%Y%m%d")
            _pandas_csv_file = DirectoryWorker.secure_save(f'pandas_output{_date_string}', '.csv')
            FileWorker.write_file(f'output{_date_string}.txt', f'Panda saved on {_pandas_csv_file}')
            text.to_csv(_pandas_csv_file)
            FileWorker.write_file(f'output{_date_string}.txt', "--- END OF OUTPUT ---")
    @staticmethod
    def print_unknown(text: any, color: str = 'white', save: bool = True) -> None:
        print(f"{UIWorker.COLOR_CODES[color.lower()]}{text}{UIWorker.COLOR_CODES['reset']}")
        if save:
            _current_date = datetime.now()
            _date_string = _current_date.strftime("%Y%m%d")
            FileWorker.write_file(f'output{_date_string}.txt', text.__str__())
            FileWorker.write_file(f'output{_date_string}.txt', "--- END OF OUTPUT ---")

    @staticmethod
    def input(text: List[str] | str) -> str:
        _rtr = input(text)
        _current_date = datetime.now()
        _date_string = _current_date.strftime("%Y%m%d")
        FileWorker.write_file(f'output{_date_string}.txt', _rtr)
        return _rtr

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def list_data_files() -> List[str]:
        _root_dir = os.path.dirname(os.path.abspath(__file__))
        _files = os.listdir(_root_dir)
        UIWorker.print(_files)

    @staticmethod
    def show_error(error: str | List[str]) -> None:
        UIWorker.print([f"Error: {error}"], 'red', False)