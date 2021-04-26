from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    #TODO: Add homepage to take input
    return "Hello, There!"

@app.route('/resutles')
def resutles():
    #TODO: Add functionality to perform OCR and display resutls
    return "Lorem ipsum sit amor dit"