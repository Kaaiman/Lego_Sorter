import os
from convert_image import convert
from rgbToColor import photo_to_color

def detect_color():
    os.system('libcamera-jpeg  -o photo.jpg --width 640 --height 480 --nopreview -t 1')
    convert(0.2)
    return photo_to_color()