from flask import Flask
from .post.views import posts
from .users_bp.views import users_bp
# from config import Config, UserConf

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config.update(DEBUG=True)
# app.config.from_json('../config.json')
# app.config.from_object(UserConf)
app.config.from_object('config.DevConf')

app.register_blueprint(posts, url_prefix='/posts')

app.register_blueprint(users_bp, url_prefix='/users_bp')

from app import views
