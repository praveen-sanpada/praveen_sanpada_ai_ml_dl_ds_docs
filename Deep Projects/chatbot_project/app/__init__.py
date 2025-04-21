from flask import Flask
from .routes import main_routes
from .nlp import load_nlp_model

def create_app():
    app = Flask(__name__)

    # Load NLP model here
    load_nlp_model()

    app.register_blueprint(main_routes)
    return app
