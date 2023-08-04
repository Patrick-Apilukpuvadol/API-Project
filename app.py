import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, json, jsonify, request
from init import db, ma, bcrypt, jwt
from controllers.cli_controllers import db_commands
from controllers.auth_controllers import auth_bp
from controllers.tour_guide_controller import tour_guide_bp
from controllers.agent_controller import agent_bp
from controllers.tour_group_log_controller import tour_group_bp
from controllers.customer_controller import customer_bp
from controllers.customer_tour_booking_controller import customer_tour_bp

def create_app():
    app = Flask(__name__)

    # app.config['JSON_SORT_KEYS'] = False

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")


    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(tour_guide_bp)
    app.register_blueprint(tour_group_bp)
    app.register_blueprint(customer_tour_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(agent_bp)

    return app