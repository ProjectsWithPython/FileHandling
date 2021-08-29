from typing import Union

class AsyncFileHandler:
    def __init__(self, _filename: str) -> None:
        self._filename = _filename
        self._extension = _filename[_filename.rfind('.'):]
    
    async def write_to_file(self, content: str) -> Union[None, str]:
        """**BETA**\n Write to file asynchronous"""
        try:
            with open(self._filename) as f:
                f.write(content)
        except:
            return "Error Occurred"

    async def read_file(self) -> str:
        """**BETA**\n Reads the file asynchronous"""
        try:
            with open(self._filename, 'r') as f:
                data = f.read()
                return data
        except:
            return "Error Occurred"

    async def append_to_file(self, content: str) -> Union[None, str]:
        """**BETA**\n Appends content to the file asynchronous"""
        try:
            with open(self._filename) as f:
                f.write(content)
        except:
             return "Error Occurred"








                
    