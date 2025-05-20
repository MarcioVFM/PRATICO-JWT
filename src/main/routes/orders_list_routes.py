from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpResquest
from src.main.composer.create_order_composer import create_orders_composer
from src.main.composer.list_orders_composer import list_orders_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_registry_composer import user_registry_composer

bank_routes_bp = Blueprint('orders_routes', __name__)

@bank_routes_bp.route('/user/registry', methods=['POST'])
def registy_user():
    try:
        http_request = HttpResquest(body=request.json)
        http_response = user_registry_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:
        return jsonify(exception), 500
    
@bank_routes_bp.route('/user/login', methods=['GET'])
def create_login():
    try:
        http_request = HttpResquest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify
    
    except Exception as exception:
        pass