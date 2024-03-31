from typing import List
import os
class FileWorker:
    @staticmethod
    def read_file(file_path) -> List[str]:
        from utils.ui_worker import UIWorker
        try:
            with open(file_path, 'r') as file:
                _lines = file.readlines()
                return [line.strip() for line in _lines]
        except FileNotFoundError:
            UIWorker.show_error(f"File '{file_path}' not found.")
            return []

    @staticmethod
    def write_file(file_path, lines, override=False) -> None:
        from utils.ui_worker import UIWorker
        
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
        
        try:
            if isinstance(lines, str):
                lines = [lines]

            lines = [line.strip() + '\n' for line in lines]

            if not override:
                with open(file_path, 'r') as _file:
                    lines = _file.readlines() + lines

            with open(file_path, 'w') as _file:
                _file.write(''.join(lines))
        except Exception as e:
            UIWorker.show_error(f"Error writing file '{file_path}': {str(e)}")