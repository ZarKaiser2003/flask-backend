from flask import Flask
from .modules.auth import auth

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.register_blueprint(auth)

    return app