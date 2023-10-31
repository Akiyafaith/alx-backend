#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)

@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """render the template"""
    return render_template('1-index.html')
