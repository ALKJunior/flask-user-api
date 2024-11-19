# função : instancia o app, registra blueprints e roda o server
from http import HTTPStatus
from flask import Flask, render_template, request, jsonify
from app.controller import users

app = Flask(__name__)

app.register_blueprint(users.blueprint)
@app.route('/')
def home():
    return render_template('home.html')

@app.before_request
def check_authentication():
    if request.method.lower() == "options":
        return
    
    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"message": "Missing Token"}), HTTPStatus.UNAUTHORIZED

    except:
        return 


if __name__ == '__main__':
    app.run(debug=True, port=5000)