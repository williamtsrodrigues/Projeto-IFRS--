import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

db = SQLAlchemy()

def init_db(app):
    # Puxa a string de conexão do .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)