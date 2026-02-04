from flask import Flask
from conf.database import init_db


from control.user import user_bp
from control.user import leads_bp


app = Flask(__name__)


#Conexao Geral do app
init_db(app)


#Registro de controladores 
app.register_blueprint(user_bp)
app.register_blueprint(leads_bp)



if __name__ == "__main__":
    app.run(debug=True)


