from flask import Blueprint, request, jsonify
from models import User
from database import db
from utils import hash_password, verify_password

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return jsonify({"message": "User Management API is running"}), 200

@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    # Create and save user
    new_user = User(name=name, email=email, password=hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created", "user_id": new_user.id}), 201

@api.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

@api.route('/search', methods=['GET'])
def search_users():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400

    users = User.query.filter(User.name.ilike(f"%{name}%")).all()
    return jsonify([user.to_dict() for user in users]), 200

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing credentials"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if user and verify_password(data["password"], user.password):
        return jsonify({"status": "success", "user_id": user.id}), 200
    return jsonify({"status": "failed"}), 401
