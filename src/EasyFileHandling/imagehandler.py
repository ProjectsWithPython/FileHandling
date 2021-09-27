from PIL import Image, ImageFilter, ImageDraw, ImageFont # image manipulation
import os # For dir making
import secrets # For Handling FileExisting Error
import cv2
import numpy

class ImageHandler:
    def __init__(self, _image_file:str) -> None:
        self._image_file = _image_file
        self._image_file_extension = _image_file[_image_file.rfind('.'):]
        if not os.path.exists('./imagesfromimagehandler'):
            os.makedirs("./imagesfromimagehandler")

    def filter_image(self, option, size = (64, 64)):
        """"""
        image = Image.open(self._image_file)
        options = ['blur', 'contour', 'detail', 'edge_enhance', 'emboss', 'edge_enhance_more', 'find_edges', 'sharpen', 'smooth', 'smooth_more', 'color_2_grayscale', 'color_2_HSV', 'resize']
        if option in options:
            if option == options[0]:
                new_image = image.filter(ImageFilter.BLUR)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[0]}Image{token}{self._image_file_extension}') 
            elif option == options[1]:
                new_image = image.filter(ImageFilter.CONTOUR)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[1]}Image{token}{self._image_file_extension}') 
            elif option == options[2]:
                new_image= image.filter(ImageFilter.DETAIL)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[2]}Image{token}{self._image_file_extension}') 
            elif option == options[3]:
                new_image = image.filter(ImageFilter.EDGE_ENHANCE)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[3]}Image{token}{self._image_file_extension}') 
            elif option == options[4]:
                new_image = image.filter(ImageFilter.EMBOSS)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[4]}Image{token}{self._image_file_extension}') 
            elif option == options[5]:
                new_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[5]}Image{token}{self._image_file_extension}') 
            elif option == options[6]:
                new_image = image.filter(ImageFilter.FIND_EDGES)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[6]}Image{token}{self._image_file_extension}') 
            elif option == options[7]:
                new_image = image.filter(ImageFilter.SHARPEN)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[7]}Image{token}{self._image_file_extension}')            
            elif option == options[8]:
                new_image = image.filter(ImageFilter.SMOOTH)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[8]}Image{token}{self._image_file_extension}')
            elif option == options[9]:
                new_image = image.filter(ImageFilter.SMOOTH_MORE)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[9]}Image{token}{self._image_file_extension}')
            elif option == options[10]:
                numpy_image=numpy.array(image)
                new_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) # converting PIL object to cv2 
                new_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2GRAY) # converting to GRAYSCALE
                new_image=Image.fromarray(new_image)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[9]}Image{token}{self._image_file_extension}')
            elif option == options[11]:
                numpy_image=numpy.array(image)
                new_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)  # converting PIL image to cv2 
                new_image = cv2.cvtColor(numpy_image, cv2.COLOR_BGR2HSV)  # converting to HSV
                new_image=Image.fromarray(new_image)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[9]}Image{token}{self._image_file_extension}')
            elif option == options[12]:
                numpy_image=numpy.array(image)
                new_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
                new_image = cv2.reshape(new_image, size) # here the size is set to a default of 64, 64, x where x ==3 for RGB and 1 for GRAYSCALE
                new_image=Image.fromarray(new_image)
                token = secrets.token_urlsafe(4)
                new_image.save(f'./imagesfromimagehandler/{options[9]}Image{token}{self._image_file_extension}')
            else:
                return 'Not a valid Image option', options
        else:
            return 'Not a valid Image option', options

    def draw_text(self, x, y, text: str, fontsize: int, rgb=(0, 0, 0), font="arial.ttf"):
        font = ImageFont.truetype(font, fontsize)
        image = Image.open(self._image_file)
        draw = ImageDraw.Draw(image)
        draw.text((x, y), text, rgb, font=font)
        token = secrets.token_urlsafe(4)
        image.save(f'./imagesfromimagehandler/drawedImage{token}{self._image_file_extension}')
