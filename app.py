from flask import Flask, render_template, request
app = Flask(__name__)

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
        return "Error: No url Found!"
 
    #TODO: Add functionality to perform OCR and display resutls
    return url