import os

class FileHandler:
    def __init__(self, _filename, _extension):
        self._filename = _filename
        self._extension = _extension
    
    def get_file_content(self):
        try:
            with open(self._filename, 'r') as f:
                _content = f.read()
                return _content
        except FileNotFoundError as err:
            return f'{self._filename} is not found, please enter the correct file!'

    def change_file_content(self, new_content):
        """Changes whole file content"""
        with open(self._filename, 'w') as f:
            f.write(new_content)
    
    def add_something_to_file_content(self, content):
        """Appends content to end of the file!"""
        with open(self._filename, 'a') as f:
            f.write()
            
    





def change_file_name(path, new_name):
    os.rename(path, new_name)


    
