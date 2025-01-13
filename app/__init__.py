from flask import Flask

from pymongo import MongoClient
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    # config
    app.config.from_object('app.config.Config')
    
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    # mongoDB connection
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client.get_database('datasets')

    # routes init
    from app.routes.detect_routes import detect_bp
    app.register_blueprint(detect_bp, url_prefix='/api')
    
    return app
