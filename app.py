from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    #TODO: Add homepage to take input
    #getting url ussing a get request
    url = request.args.get("url"," ")
    if url != " ":
        print("We got the Url")

    return render_template("index.html")

@app.route('/resutles')
def resutles():
    #TODO: Add functionality to perform OCR and display resutls
    return "Lorem ipsum sit amor dit"