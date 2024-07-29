#!/usr/bin/python3
"""
    Minimal Flask App
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    "Home Page"
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    "The HBNB Page"
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    "The Random text Page"
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
