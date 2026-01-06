from flask import Flask, Blueprint, request, jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy 

from conf.database import db


user_bp = Blueprint('user', __name__, url_prefix = '/user') 


@user_bp.route("/", methods = ["POST"])
def verificarUser():
    return ""

    