#!/usr/bin/python3
""" Start a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbtn', strict_slashes=False)
def hbtn():
    """ Display "HBTN"
    """
    return "HBTN"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
