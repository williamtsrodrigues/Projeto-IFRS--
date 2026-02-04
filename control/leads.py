from flask import Blueprint, request, jsonify
from conf.database import db

leads_bp = Blueprint('leads', __name__, url_prefix='/leads')

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Novo')
    score = db.Column(db.Integer, default=0)


@leads_bp.route("/", methods='POST')
def new_lead():
    data = request.get_json()

    if not data or 'nome' not in data:
        return jsonify({"Error": "Nome do lead é obrigatório"}), 400
    
    novo_lead = Lead(
        nome=data['nome'],
        status=data.get('status', 'Novo'),
        score=data.get('score', 0)
    )

    db. session.add(novo_lead)
    db.session.commit()

    return jsonify({"message": "Lead criado!", "id": novo_lead.id}), 201