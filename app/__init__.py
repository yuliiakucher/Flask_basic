from flask import Flask
# from config import Config, UserConf

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config.update(DEBUG=True)
# app.config.from_json('../config.json')
# app.config.from_object(UserConf)
app.config.from_object('config.DevConf')

from app import views
