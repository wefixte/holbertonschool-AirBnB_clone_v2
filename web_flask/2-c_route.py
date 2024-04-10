#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display "Hello HBTN!" when access """
    return "Hello HBTN!"


@app.route('/hbtn', strict_slashes=False)
def hbtn():
    """ Display "HBTN" when access /hbtn route """
    return "HBTN"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """ Display string when access /c/<text> route """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
