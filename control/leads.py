from flask import Blueprint, request, jsonify
from conf.database import db

leads_bp = Blueprint('leads', __name__, url_prefix='/leads')

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    telefone = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), default='Novo')
    score = db.Column(db.Integer, default=0)

#capturar leads e classificar
@leads_bp.route("/", methods=["POST"])
def new_lead():
    data = request.get_json()

    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')


    if not nome:
        return jsonify({"Error": "Nome é obrigatório"}), 400
    

    if email and telefone:
        score_calculado = 100
    else:
        score_calculado = 50


    novo_lead = Lead(
        nome=nome,
        email=email,
        telefone=telefone,
        score=score_calculado,
        status="novo"
    )

    db. session.add(novo_lead)
    db.session.commit()

    return jsonify({
        "id": novo_lead.id,
        "message": "Lead criado!",
        "score_atribuido": novo_lead.score
    }), 201