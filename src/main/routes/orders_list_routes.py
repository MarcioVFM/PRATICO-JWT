from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpResquest
from src.main.composer.create_order_composer import create_orders_composer
from src.main.composer.list_orders_composer import list_orders_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.user_registry_composer import user_registry_composer

from src.main.middlerwares.auth_jwt import auth_jwt_verify
from src.errors.errors_handler import handle_error

orders_routes_bp = Blueprint('orders_routes', __name__)

@orders_routes_bp.route('/user/registry', methods=['POST'])
def registy_user():
    try:
        http_request = HttpResquest(body=request.json)
        http_response = user_registry_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
    
@orders_routes_bp.route('/user/login', methods=['POST'])
def create_login():
    try:
        http_request = HttpResquest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@orders_routes_bp.route('/orders/create/<user_id>', methods=['POST'])
def create_order(user_id):
    try:
        token_information = auth_jwt_verify(user_id)
        http_request = HttpResquest(
            body=request.json,
            params={'user_id': user_id},
            token_infos=token_information
        )
        http_response = create_orders_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
    
@orders_routes_bp.route('/orders/list/<user_id>', methods=['GET'])
def list_order(user_id):
    try:
        token_information = auth_jwt_verify(user_id)
        http_request = HttpResquest(
            params={'user_id': user_id},
            token_infos= token_information
        )
        http_response = list_orders_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code