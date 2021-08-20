import os
import io


class FileHandler:
    def __init__(self, _filename):
        self._filename = _filename
        self._extension = _filename[_filename.rfind('.'):]

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

    def get_line_count(self):
        """Returns number of lines in file"""
        try:
            num_lines = sum(1 for _ in open(self._filename))
            return num_lines
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
        fileTypes = {'.py': 'Python', '.js': 'Javascript',
                     '.cpp': 'C++', '.c': 'C',
                     '.sql': 'SQL', '.ts': 'TypeScript',
                     '.json': 'JSON', '.csv': 'CSV',
                     '.html': 'HTML', '.css': 'CSS',
                     '.rb': 'Ruby', '.swift': 'Swift',
                     '.txt': 'Text'}

        if self._extension not in fileTypes:
            return "Unknown file/extension. Please Report The Developers [ https://github.com/ProjectsWithPython/FileHandling/issues ]"
        else:
            return f'This is a {fileTypes[self._extension]} file.'

    def change_file_extension(self, current_extension, new_extension):
        try:
            os.name(self._filename, self._filename.replace(rf'[{current_extension}]', f'{new_extension}'))
            return 'Done!'
        except:
            return f"Please Report The Developers [ https://github.com/ProjectsWithPython/FileHandling/issues ]"

    def is_file_writeable(self) -> bool:
        """Tells you if the file is writeable"""
        with open(f'{self._filename}', 'w') as f:
            if f.writable():
                return True
            else:
                return False
    
    



def change_file_name(path, new_name):
    """Changes file name"""
    os.rename(path, new_name)


def delete(file):
    """Deletes file"""
    if os.path.exists(file):
        os.remove(file)
    else:
        return f"{file} does not exists. Make sure the name is correct or you need to put the file path."


def create_file(file):
    """Creates a file"""
    if os.path.exists(file):
        return False
    else:
        with open(file, 'w') as f:
            f.write('File Created With FileHandler ©')
        return "Created File"


def list_item_in_dir(path) -> list:
    """Gives a list of all items in the folder"""
    if os.path.exists(path):
        return os.listdir(path)
    else:
        raise FileNotFoundError('Folder Not Found!')


def delete_all_item_in_dict(path):
    """Deletes all items in the folder"""
    em = []
    if os.path.exists(path):
        for i in os.listdir(path):
            os.remove(i)
            em.append(i)
        return em
    else:
        raise FileNotFoundError('Folder not found or wrong path.')


def is_pythonfile(file):
    """Returns True if file extension is py and if not then false."""
    if file.endswith('py'):
        return True
    else:
        return False
