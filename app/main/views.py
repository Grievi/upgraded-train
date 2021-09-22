from flask import render_template
from . import main
from flask_login import login_required

#views
@main.route('/')
def index():
    '''
    View home / root page functions that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    