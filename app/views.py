from app import app
from flask import render_template, request
from app.users import users
from app.posts import posts


@app.route('/')
def start():
    my_users = users
    my_posts = posts
    return render_template('start.html', users=my_users, posts=my_posts)


@app.route('/search', methods=['POST', 'GET'])
def search():
    # result = request.args['search']
    result = ''
    if request.method == 'POST':
      result = request.form['search']

    return render_template('search.html', search=result)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/<id>')
def user(id):
    my_user = {}
    for user in users:
        if user.get('id') == int(id):
            my_user = user

    return render_template('user.html', user=my_user)


@app.route('/city/<city>')
def user_city(city):
    my_user = {}
    for user in users:
        if user.get('address').get('city') == city:
            my_user = user

    return render_template('user.html', user=my_user)
