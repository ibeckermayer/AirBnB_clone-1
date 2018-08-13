#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!

    Returns:
        str: Hello HBNB!

    """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB

    Returns:
        str: HBNB

    """
    return "HBNB"

def fdjk(ksjaf, ksjafsa):
    """fjdksf

    Args:
       ksjaf arg1
       ksjafsa arg2

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If param2 is equal to param1.

    """


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C <something>

    Args:
        text (str): input text

    Returns:
        str: C <text>

    """
    return "C {:s}".format(text).replace('_', " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
