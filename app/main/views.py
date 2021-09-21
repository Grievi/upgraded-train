from flask import render_template
from . import main

#views
@main.route('/')
def index():
    '''
    View home / root page functions that returns the index page and its data
    '''
    return render_template('index.html')