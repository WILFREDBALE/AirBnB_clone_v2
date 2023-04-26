#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    """Displays 'C <text>'"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """Displays 'Python <text>'"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
