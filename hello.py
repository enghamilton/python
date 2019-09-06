from flask import Flask

abyarapython = Flask(__name__)

@app.route('/')
def source():
 html = 'Hello World!'
 return html
