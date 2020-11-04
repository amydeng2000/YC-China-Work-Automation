from PIL import Image
import pytesseract
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

path = r'C:\Users\12246\Desktop\YC-China-Work-Automation\webcrawling&ImageToText\emails\001-53f31a52dabfae9a84430cc8.png'
img = cv2.imread(path)

cv2.imshow('image', img) 
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

scale_percent = 200 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

text = pytesseract.image_to_string(img, lang="eng", timeout=15)
print(text)
