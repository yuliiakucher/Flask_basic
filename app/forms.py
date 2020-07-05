from wtforms import Form, StringField


class Posts_Form(Form):
    name = StringField('Name')
    mail = StringField('Mail')
