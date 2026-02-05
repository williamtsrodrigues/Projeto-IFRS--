from flask import Flask
from conf.database import init_db

#controlador

from control.user import user_bp
from control.leads import leads_bp
from control.produtos import produtos_bp


app = Flask(__name__)


#Conexao Geral do app
init_db(app)


#Registro de controladores 
app.register_blueprint(user_bp)
app.register_blueprint(leads_bp)
app.register_blueprint(produtos_bp)



if __name__ == "__main__":
    app.run(debug=True)


