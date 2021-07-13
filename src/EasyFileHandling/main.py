import os


class FileHandler:
    def __init__(self, _filename, _extension):
        self._filename = _filename
        self._extension = _extension
    
    def does_file_exist(self):
        if os.path.exists(self._filename):
            return True
        else:
            return False
    
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
            f.write(content)




        

            
    




def change_file_name(path, new_name):
    os.rename(path, new_name)


def delete(file):
    """Deletes file"""
    if os.path.exists(file):
        os.remove(file)   
    else:
        return f"{file} does not exists. Make sure the name is correct or you need to put the file path."


def create_file(file):
    if os.path.exists(file):
        return False
    else:
        with open(file, 'w') as f:
            f.write('File Created With FileHandler ©')
        return "Created File"
