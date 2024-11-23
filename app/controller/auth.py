import os
from flask import Blueprint, jsonify, request, redirect, render_template, url_for
from app.models.user import *
from http import HTTPStatus

blueprint = Blueprint('auth', __name__)

@blueprint.route('/auth/signup', methods=['POST','GET'])
def register():
    if request.method == "POST":
        sucess, result = register_user(request)
        if sucess:
            return jsonify(result), HTTPStatus.CREATED
        else:
            return jsonify({"message": "not ok", "what_happened": f"{result}"}), HTTPStatus.BAD_REQUEST

    if request.method == "GET":
        return render_template("signup.html")

@blueprint.route('/auth/signup_sucess')
def register_sucess():
    return render_template('signup_sucess.html')

@blueprint.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('auth')
    
    if request.method == "POST":
        sucess, result = auth_user(request)
        if sucess:
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(result), HTTPStatus.BAD_REQUEST

@blueprint.route('/auth/logout', methods=['POST'])
def logout():
    if request.method == "POST":
        print("no saibo fazer isso")
        return HTTPStatus.OK