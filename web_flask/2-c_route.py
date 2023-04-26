#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

def hello():
    """Prints 'Hello HBNB!'"""
    return 'Hello HBNB!'

def hbnb():
    """Prints 'HBNB'"""
    return 'HBNB'

app.add_url_rule('/', 'hello', hello)
app.add_url_rule('/hbnb', 'hbnb', hbnb)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
