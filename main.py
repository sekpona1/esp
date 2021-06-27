
import matplotlib.pyplot as plt
from fastapi import FastAPI, UploadFile, File
import pytesseract as tess
from PIL import Image
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re
from gensim.summarization import summarize
from PIL import Image
from io import BytesIO
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\sitsope sekpona\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

def tesser(image):
    img = Image.open(BytesIO(image))
    text = tess.image_to_string(img)
    return {"text": text}


#Creation d'une api
app=FastAPI()

@app.get('/'):
async def index():
    return {"detail": "app working"}

@app.post('/ocr_pred/')
async def ocr1(file: bytes = File(...)):
    #image = Image.open(image)
    prediction = tesser(file)
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
