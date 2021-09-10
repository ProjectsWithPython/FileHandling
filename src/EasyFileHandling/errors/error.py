# All Errors
exception_sentences = [
    "Folder or path not found",
    "Content must be string or bytes type object",
    "File has zero lines",
    "This looks like a unexpected, please review your code."
    "JSON takes list or dict"
]

class FolderNotFound(Exception):
    def __init__(self, message=exception_sentences[0]):
        self.message = message
        super().__init__(self.message)


class NotStringOrBytes(Exception):
    def __init__(self, message=exception_sentences[1]):
        self.message = message
        super().__init__(self.message)


class ZeroLineFile(Exception):
    def __init__(self, message=exception_sentences[2]):
        self.message = message
        super().__init__(self.message)

class UnexpectedError(Exception):
    def __init__(self, message=exception_sentences[3]) -> None:
        self.message = message
        super().__init__(self.message)
    

class JSONTakesListOrDict(Exception):
    def __init__(self, message=exception_sentences[4]):
        self.message = message
        super().__init__(self.message)
