#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name)
babel = Babel(app)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """define the best supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """render the template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
