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
    """ Display "HBTN" """
    return "HBTN"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
