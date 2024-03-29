from typing import List
import os
from utils.file_worker import FileWorker
from datetime import datetime
class UIWorker:
    '''Class to handle user interaction with the app, in the future if other way of UI is needed change from this class using it as conector.'''	
    @staticmethod
    def print(text: List[str] | str, color: str = 'white', save: bool = True) -> None:
        color_codes = {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m',
        }
        if isinstance(text, str):
            text = [text]

        for t in text:
            print(f"{color_codes[color.lower()]}{t}{color_codes['reset']}")
        if save:
            current_date = datetime.now()
            date_string = current_date.strftime("%Y%m%d")
            FileWorker.write_file(f'output{date_string}.txt', text)
            FileWorker.write_file(f'output{date_string}.txt', "--- END OF OUTPUT ---")

    @staticmethod
    def input(text):
        return input(text)

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def list_data_files() -> List[str]:
        _root_dir = os.path.dirname(os.path.abspath(__file__))
        _files = os.listdir(_root_dir)
        UIWorker.print(_files)

    @staticmethod
    def show_error(error) -> None:
        UIWorker.print([f"Error: {error}"], 'red', False)