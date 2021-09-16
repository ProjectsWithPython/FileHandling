class FolderNotFound(Exception):
    def __init__(self, message="Folder or path not found",):
        self.message = message
        super().__init__(self.message)


class NotStringOrBytes(Exception):
    def __init__(self, message="Content must be string or bytes type object"):
        self.message = message
        super().__init__(self.message)


class ZeroLineFile(Exception):
    def __init__(self, message="File has zero lines"):
        self.message = message
        super().__init__(self.message)

class UnexpectedError(Exception):
    def __init__(self, message="This looks like a unexpected, please review your code.") -> None:
        self.message = message
        super().__init__(self.message)
    

class JSONTakesListOrDict(Exception):
    def __init__(self, message="JSON takes list or dict"):
        self.message = message
        super().__init__(self.message)
