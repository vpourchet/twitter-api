# app/__init__.py
from flask import Flask # This line already exists
from flask_restx import Api

from .db import repository
from .models import Tweet
from .apis.tweets import api as tweets

repository.add(Tweet("My tweet 1"))
repository.add(Tweet("My tweet 2"))

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return "Hello World!"

    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
