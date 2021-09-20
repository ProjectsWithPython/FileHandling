from PIL import Image, ImageFilter, ImageDraw, ImageFont # image manipulation
import os # For dir making
import secrets # For Handling FileExisting Error



class ImageHandler:
    def __init__(self, _image_file:str) -> None:
        self._image_file = _image_file
        self._image_file_extension = _image_file[_image_file.rfind('.'):]
        if not os.path.exists('./imagesfromimagehandler'):
            os.makedirs("./imagesfromimagehandler")

    def filter_image(self, option):
        """"""
        image = Image.open(self._image_file)
        options = ['blur', 'contour', 'detail', 'edge_enhance', 'emboss', 'edge_enhance_more', 'find_edges', 'sharpen', 'smooth', 'smooth_more']
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