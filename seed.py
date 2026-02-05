from app import app
from conf.database import db
from control.produtos import Produto

def seed_products():
    # Entrar no 'contexto' do app para ter permissão de usar o banco
    with app.app_context():
        print("Limpando tabela de produtos...")
        # Deleta o que já existe para não duplicar toda vez que rodar
        db.session.query(Produto).delete()


        print("Gerando 50 produtos fictícios...")
        produtos_ficticios = []

        for i in range(1,51):
            novo_produto = Produto(
                nome=f"Produto ERP {i:03d}",  # Gera nomes como Produto ERP 001
                preco=25.50 * i,              # Preços variados
                estoque=10 * i                # Estoques variados
            )
            produtos_ficticios.append(novo_produto)
        
        # Envia a lista inteira para o banco de uma só vez 
        db.session.add_all(produtos_ficticios)

        # Salva as alterações definitivamente
        db.session.commit()
        print("Sucesso!")

if __name__ == "__main__":
    seed_products()