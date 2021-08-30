# All Errors


class FolderNotFound(Exception):
    def __init__(self, message="Folder or path not found"):
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
