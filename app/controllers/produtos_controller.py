from flask import Blueprint, render_template

produtos_bp = Blueprint("produtos", __name__, template_folder="../templates/produtos")

@produtos_bp.route("/", methods=["GET"])
def lista_produtos():
    # Simulação de produtos (substituir com consulta ao banco de dados)
    produtos = [
        {"id": 1, "nome": "Produto A", "preco": 19.99},
        {"id": 2, "nome": "Produto B", "preco": 29.99},
        {"id": 3, "nome": "Produto C", "preco": 39.99},
    ]
    return render_template("lista.html", produtos=produtos)

@produtos_bp.route("/<int:produto_id>", methods=["GET"])
def detalhe_produto(produto_id):
    # Simulação de detalhe de produto (substituir com consulta ao banco de dados)
    produto = {"id": produto_id, "nome": f"Produto {chr(64 + produto_id)}", "preco": 19.99 * produto_id}
    return render_template("detalhe.html", produto=produto)