from flask import Blueprint, jsonify, request
from app.models.user import *
from http import HTTPStatus

blueprint = Blueprint('users', __name__)

@blueprint.route('/users', methods=['GET'])
def get_all():
    sucess, users = get_all_users()
    if sucess:
        return jsonify(users), HTTPStatus.OK
    else:
        return {"message": "No users found"}, HTTPStatus.NOT_FOUND

@blueprint.route('/users/<id>', methods=['GET', 'DELETE', 'PATCH'])
def user_with_id(id):
    sucess, result = get_user_with_id(id)
    if not sucess:
        return {'message:': 'User not found'}, HTTPStatus.NOT_FOUND
    
    if request.method == 'GET':
        return jsonify(result)
    
    if request.method == 'DELETE':
        auth_header = request.headers.get("Authorization")
        sucess, user = validate_jwt(auth_header)

        if user.get("role") != "Administrator":   
            if not user["sub"] == str(id):
                return jsonify(), HTTPStatus.FORBIDDEN
        
        sucess, result = delete_user(id)
        if sucess:
            return jsonify(result), HTTPStatus.NO_CONTENT
        else:
            return jsonify(result), HTTPStatus.INTERNAL_SERVER_ERROR
        
    if request.method == 'PATCH':
        auth_header = request.headers.get("Authorization")
        sucess, user = validate_jwt(auth_header)
        
        if user.get("role") != "Administrator":   
            if not user["sub"] == str(id):
                return jsonify(), HTTPStatus.FORBIDDEN
        
        sucess, result = update_user(id, request)
        if sucess:
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(result), HTTPStatus.INTERNAL_SERVER_ERROR

@blueprint.route('/users/email/<email>')
def user_with_email(email):
    return get_user_with_email(email)
