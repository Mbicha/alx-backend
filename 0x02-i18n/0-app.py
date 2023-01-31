#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Prints Hello world.
    """
    return render_template('0-index.html')
