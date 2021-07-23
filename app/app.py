import os, sys

from PIL import Image, ImageFilter
import pyocr
import numpy as np

OCR_PATH = "../tesseract/tesseract.exe"
image_file = sys.argv[1]

def get_img():
    im = Image.open('image_file')
