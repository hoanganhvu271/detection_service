from flask import Flask

from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # config
    app.config.from_object('app.config.Config')
    
    
    # mongoDB connection
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client.get_database('datasets')

    # routes init
    from app.routes.detect_routes import detect_bp
    app.register_blueprint(detect_bp, url_prefix='/api')
    
    return app
