from typing import List
import os
from utils.file_worker import FileWorker
from datetime import datetime
class UIWorker:
    '''Class to handle user interaction with the app, in the future if other way of UI is needed change from this class using it as conector.'''	
    @staticmethod
    def print(_text: List[str] | str, _color: str = 'white', _save: bool = True) -> None:
        _color_codes = {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m',
        }
        if isinstance(_text, str):
            _text = [_text]

        for t in _text:
            print(f"{_color_codes[_color.lower()]}{t}{_color_codes['reset']}")
        if _save:
            _current_date = datetime.now()
            _date_string = _current_date.strftime("%Y%m%d")
            FileWorker.write_file(f'output{_date_string}.txt', _text)
            FileWorker.write_file(f'output{_date_string}.txt', "--- END OF OUTPUT ---")

    @staticmethod
    def input(_text: List[str] | str) -> str:
        _rtr = input(_text)
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
    def show_error(_error: str | List[str]) -> None:
        UIWorker.print([f"Error: {_error}"], 'red', False)