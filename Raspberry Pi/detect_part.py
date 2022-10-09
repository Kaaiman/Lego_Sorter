from convert_image import convert
from predict import detect_part
from convert_white import white_convert
import os

os.system('libcamera-jpeg  -o photo.jpg --width 640 --height 480 --nopreview -t 1')
#convert(0)
white_convert(0, 0)
part = detect_part()
print(part)
