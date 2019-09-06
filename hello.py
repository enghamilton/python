from flask import Flask

hello = Flask(__name__)

@app.route('/')
def source():
 html = 'Hello World!'
 return html
