#!/usr/bin/python3
"""List states in template"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
"""Flask Instance"""
app.url_map_strict_slashes = False


@app.route('/states_list')
def state_list():
    """Page That lists states"""
    states = list(storage.all(State).values)
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html',states)

@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')