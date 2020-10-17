from PIL import Image
import pytesseract
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = cv2.imread('./emails/5c2eb51c530c7008bbb9953c.png', cv2.IMREAD_UNCHANGED)

# img = Image.open('./emails/5c2eb51c530c7008bbb9953c.png')
# img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
# img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


scale_percent = 200 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


ret,img = cv2.threshold(np.array(img), 0, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(img, lang="eng", timeout=5)
print(text)
