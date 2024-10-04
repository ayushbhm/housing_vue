from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User  # Adjust the import based on your project structure
from models.user import db  # Adjust the import based on your project structure

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == password:  # Replace with hashed password check
        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        
        if user.role == 'admin':
            return jsonify(access_token=access_token), 200
        elif user.role == 'professional':
            return jsonify(access_token=access_token, redirect_url='/professional/dashboard'), 200
        elif user.role == 'customer':
            return jsonify(access_token=access_token, redirect_url='/user/dashboard'), 200

    return jsonify({"msg": "Bad username or password"}), 401
