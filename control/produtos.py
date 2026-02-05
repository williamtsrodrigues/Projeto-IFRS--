from conf.database import db
from flask import Blueprint, jsonify


produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, default=0)

#listar produtos
@produtos_bp.route("/", methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    lista = []
    for p in produtos:
        lista.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco,
            "estoque": p.estoque
        })

    return jsonify(lista)