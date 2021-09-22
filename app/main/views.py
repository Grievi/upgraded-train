from flask import render_template
from . import main
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import ReviewForm,UpdateProfile
from .. import db

#views
@main.route('/')
def index():
    '''
    View home / root page functions that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
