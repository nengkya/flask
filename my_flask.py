from flask import Flask

#__name__ is resources path
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> #__name__ is resources path </h1>'
