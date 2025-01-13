from flask import Flask
from app.routes.detect_routes import detect_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.register_blueprint(detect_bp, url_prefix='/api')
    
    return app
