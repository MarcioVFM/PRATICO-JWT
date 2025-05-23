from flask import Flask
from src.models.settings.db_connection_handle import dbconnectionhandler
from src.main.routes.orders_list_routes import orders_routes_bp

dbconnectionhandler.connect()

app = Flask(__name__)

app.register_blueprint(orders_routes_bp)