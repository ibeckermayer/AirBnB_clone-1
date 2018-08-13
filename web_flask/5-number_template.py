#!/usr/bin/python3
from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C <text>

    Args:
        text (str): input text

    Returns:
        str: C <text>

    """
    return "C {:s}".format(text).replace('_', " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """display Python <text>

    Args:
        text (str): input text

    Returns:
        str: Python <text>

    """
    return "Python {:s}".format(text).replace('_', " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display Python <text>

    Args:
        n (str): input number, must be int

    Returns:
        str: <n> is a number

    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display Python <text>

    Args:
        n (str): input n, must be int

    Returns:
        str: rendered html

    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
