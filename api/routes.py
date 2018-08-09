from flask import flash, redirect, render_template, url_for

from api import app
from api.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            'name' : 'smartcow',
            'Cliente' : 'Alpina',
            'created_at' : '09/08/2018',
            'author': {'username': 'Jairo'},
            'description': 'Optimize cows in marketing to increase sells',
            'techniques' : [
                'machine learning',
                'deep learning',
            ]
        }
    ]
    user = {'username': 'Jairo'}
    return render_template('index.html', title='Home', user=user, projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
