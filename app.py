from flask import Flask, render_template, request
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Moiz\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import requests
from PIL import Image

app = Flask(__name__)

def image_to_text(url):
    img = Image.open(requests.get(url, stream=True).raw)
    text = tess.image_to_string(img)
    return text


@app.route('/')
def root():
    #Homepage to take input
    return render_template("index.html")

@app.route('/result', methods=["POST", "GET"])
def result():
    url = ""
    #getting url ussing a get request
    if request.method == "GET":
        url = request.args.get("url"," ")
    else:
        #Getting from the POST method
        url = request.form.get("url")

    #Error Handling
    if url == " " or not url :
        return render_template("error.html", error = "No url Found!")
 
    text = image_to_text(url)
    print(text)
    return render_template("result.html", result = text)

