### Package for File Handling

**Getting started**
```py
from EasyFileHandling.main import FileHandler

x = FileHandler('test.py', 'py')

print(x.get_file_content()) # This will print file content.

```
**Whats so special about package**
*This lets you use `os` module easily not all features but some of them.


**Whats New?**
*Version: `1.1.0`: In Version `1.1.0` I have decided to add a new method for the class `FileHandler`. Its kinda cool/weird method, its the `what_type_of_file` method. It tells wether its a python file or javascript and etc. Please let me know all the issues you're getting [Here](https://github.com/ProjectsWithPython/FileHandling) and all the issues [Here](https://github.com/ProjectsWithPython/FileHandling/issues)*