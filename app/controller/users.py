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

@blueprint.route('/users/<id>', methods=['GET', 'DELETE', 'PATCH'])
def user_with_id(id):
    if request.method == 'GET':
        return get_user_with_id(id)
    if request.method == 'DELETE':
        return delete_user(id)
    if request.method == 'PATCH': #                    Fazer o PATCH aq
        return patch_user()

@blueprint.route('/users/email/<email>')
def get_user_with_email(email):
    return get_user_with_email(email)
