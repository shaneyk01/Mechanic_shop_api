from flask import Flask
from .extensions import db, ma
from app.blueprints.customer import customer_bp
from app.blueprints.mechanics import mechanics_bp
from app.blueprints.service_tickets import tickets_bp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
    db.init_app(app)
    ma.init_app(app)
    
    
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(mechanics_bp, url_prefix='/mechanics')
    app.register_blueprint(tickets_bp, url_prefix='/tickets')

    return app