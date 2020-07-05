from wtforms import Form, StringField


class User_form(Form):
    username = StringField('Username')
    email = StringField('Email')
    password = StringField('Password')
