from flask import Flask, render_template, request
import pytesseract as tess
#tess.pytesseract.tesseract_cmd = r'C:\Users\Moiz\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
tess.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
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
    results = ""
    #getting url ussing a get request
    if request.method == "GET":
        url = request.args.get("url"," ")
    else:
        #Getting from the POST method
        url = request.form.get("url")

    #Error Handling
    if url == " " or not url :
        return render_template("error.html", error = "No url Found!")
 
    final_text = []
    # try:
    #     text = image_to_text(url)
    #     results = text.split('\n')
    #     for r in results:
    #         if r != "" and r !=" " and r !="  " and r !="   ":
    #             final_text.append(r)
    # except:
    #     return render_template("error.html", error = "Invalid Url")

    text = image_to_text(url)
    results = text.split('\n')
    for r in results:
        if r != "" and r !=" " and r !="  " and r !="   ":
            final_text.append(r)
            
    print(text)
    return render_template("result.html", result = text, url = url)

