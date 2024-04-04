import os

class DirectoryWorker:
    @staticmethod
    def secure_save(file_name, file_type):
        '''Saves a file securely by adding a number to the file 
        name if the file already exists. To avoid deleting files by mistake'''
        if not os.path.exists(file_name + file_type):
            return file_name + file_type

        i = 1
        while os.path.exists(file_name + str(i) + file_type):
            i += 1

        return file_name + str(i) + file_type