#!/usr/bin/python3
""" script that starts a Flask web application """


from flask import Flask
# Create an instance with name of the current module
app = Flask(__name__)


# Flask decorator, bind root URL '/' to hello() function
@app.route('/', strict_slashes=False)
def hello():
    """ Display "Hello HBTN!" when access """
    return "Hello HBTN!"


# Check if script is executed as main program
if __name__ == "__main__":
    # Start Flask dev server.
    # Listens all network interfaces (0.0.0.0) on port 5000
    app.run(host="0.0.0.0", port=5000)
