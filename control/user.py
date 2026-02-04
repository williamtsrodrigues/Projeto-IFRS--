from flask import Blueprint, request, jsonify
from sqlalchemy import text
from conf.database import db


user_bp = Blueprint('auth', __name__, url_prefix = '/auth') 


class User(db.Model):
    __tabblename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@user_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Dados Insuficientes"}), 400
    
    new_user = User(username=data['username'], password=data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso!"})


@user_bp.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.password == data.get('password'):
        return jsonify(True), 200
    return jsonify(False), 401