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
    
    def what_type_of_file(self) -> str:
        """Tells you what type of file is it."""
        if self._filename.endswith('.py'):
            return 'This is a Python file.'
        elif self._filename.endswith('.js'):
            return 'This is a JavaScript file.'
        elif self._filename.endswith('.cpp'):
            return 'This is a C++ file'
        elif self._filename.endswith('.c'):
            return "This is a C file"
        elif self._filename.endswith('.sql'):
            return "This is a SQL file"
        elif self._filename.endswith('.ts'):
            return "This is a TypeScript"
        elif self._filename.endswith('.json'):
            return "This is a JSON file."
        elif self._filename.endswith('.csv'):
            return "This is a CSV file"
        elif self._filename.endswith('.html'):
            return "This is a HTML file"
        elif self._filename.endswith('.css'):
            return "This is a CSS file"
        elif self._filename.endswith('.rb'):
            return "This is a Ruby file"
        elif self._filename.endswith('.swift'):
            return "This is a Swift file"
        else:
            return "Unknown file/extension. Please Report The Developers [ https://github.com/ProjectsWithPython/FileHandling/issues ]"
        
    def change_file_extension(self, current_extension, new_extension):
        try:
            os.name(self._filename, self._filename.replace(rf'[{current_extension}]', f'{new_extension}'))
            return 'Done!'
        except:
            return f"Please Report The Developers [ https://github.com/ProjectsWithPython/FileHandling/issues ]"


    
        
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



def list_item_in_dir(path) -> list:
    if os.path.exists(path):
        return os.listdir(path)
    else:
        raise FileNotFoundError('Folder Not Found!')

def delete_all_item_in_dict(path):
    em = []
    if os.path.exists(path):
        for i in os.listdir(path):
            os.remove(i)
            em.append(i)
        return em
    else:
        raise FileNotFoundError('Folder not found or wrong path.')

