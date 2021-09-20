### Package for File Handling

**[DOCUMENTATION]**(https://filehandling.netlify.app/docs.html)


**Getting started**
```py
from EasyFileHandling.main import FileHandler

x = FileHandler('test.py', 'py')

print(x.get_file_content()) # This will print file content.

```
**Whats so special about package**


*It lets to handle files easliy, whether is JSON, a image, text file and etc.*


**BETA**

*Howdy all, we have decided to add `AsyncFileHandler` for asynchronous python codes. Now you can do all those `append`, `write` and  `read` asynchronouly.* ***REMEMBER THIS IS A BETA***


*How do I use it?*


*Simply import this and get started.*


```py
from EasyFileHandling.beta.main import AsyncFileHandler
```


**Whats New?**

*Howdy, new version `1.4.0` just dropped. You all be thinking whats new `byte` and `json` support added. We have also added `type` hints. Let me show you a example how json handler works*


**ImageHandler**


```py
from EasyFileHandling.imagehandler import ImageHandler
x = ImageHandler('nice.jpg')
x.filter_image('blur') # it will make a imagehandlerimages folder with this file in it.
x.draw_text(100, 50, "Hello World",50, rgb=(0, 0, 0), font="arial.ttf") # rgb and font are default params.
```


*If you are having any issues let us know [Here](https://github.com/ProjectsWithPython/FileHandling/issues).*



