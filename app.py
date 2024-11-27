# função : instancia o app, registra blueprints e roda o server
from http import HTTPStatus
from flask import Flask, render_template, request, jsonify
from app.controller import users
from app.controller import auth
from app.commons.jwt import validate_jwt
from app.commons.constants import PUBLIC_ROUTES

app = Flask(__name__)

app.register_blueprint(users.blueprint)
app.register_blueprint(auth.blueprint)


@app.before_request
def check_authentication():
    if request.method.lower() == "options":
        return
    if request.path in PUBLIC_ROUTES:
        return
    try:
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Missing token"}), HTTPStatus.UNAUTHORIZED
        
        is_valid, user = validate_jwt(auth_header)
        if not is_valid:
            return jsonify({"message": "Not a valid token"}), HTTPStatus.UNAUTHORIZED
        
    except Exception as e:
        print('Error', e)
        return e
    

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)