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

*Howdy, new version `1.4.0` just dropped. You all be thinking whats new `byte` and `json` support added. We have also added `type` hints. Let me show you a example how json handler works*


**JsonHandler**


```py
from EasyFileHandling.main import JsonHandler
my_obj = [
    {'Sad': 100}
]
x = JsonHandler('sad.json')
x.write_to_json(obj)
```


*If you are having any issues let us know [Here](https://github.com/ProjectsWithPython/FileHandling/issues).*



