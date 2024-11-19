# define a rota users com uma blueprint
import os
from flask import Blueprint, jsonify, request, redirect, render_template, url_for
from app.models.user import *
from http import HTTPStatus

blueprint = Blueprint('users', __name__)

@blueprint.route('/users', methods=['GET'])
def get_all():
    users = get_all_users()
    return users

@blueprint.route('/users/id/<id>')
def get_user_with_id(id):
    return get_user_with_id(id)

@blueprint.route('/users/email/<email>')
def get_user_with_email(email):
    return get_user_with_email(email)

@blueprint.route('/users/signup', methods=['POST','GET'])
def register():
    if request.method == "POST":
        sucess, result = register_user(request)
        if sucess:
            return jsonify(result), HTTPStatus.CREATED
        else:
            return jsonify({"message": "not ok","what_happened": f"{result}"}), HTTPStatus.BAD_REQUEST

    if request.method == "GET":
        return render_template("signup.html")

@blueprint.route('/users/signup_sucess')
def register_sucess():
    return render_template('signup_sucess.html')

@blueprint.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login')
    
    if request.method == "POST":
        sucess, result = login_user(request)
        if sucess:
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(result), HTTPStatus.BAD_REQUEST
