from app.users_bp import users_bp
from flask import render_template, request
from .user_form import User_form


@users_bp.route('/', methods=['POST', 'GET'])
def users_start():
    rez_username = ''
    rez_email = ''
    rez_password = ''
    if request.method == 'POST':
        rez_username = request.form['username']
        rez_email = request.form['email']
        rez_password = request.form['password']
    return render_template('users_bp/users_start.html', username=rez_username, email=rez_email, password=rez_password)


@users_bp.route('/form/', methods=['GET','POST'])
def user_form():
    form = User_form()
    username = ''
    email = ''
    password = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
    return render_template('users_bp/user_form.html', username=username, email=email, password=password, form=form)
