from flask import Blueprint, render_template, jsonify
from app.models import Produto


produtos_bp = Blueprint("produtos", __name__, template_folder="../templates/produtos")

@produtos_bp.route("/", methods=["GET"])
def lista_produtos():
    # Simulação de produtos (substituir com consulta ao banco de dados)
    produtos = [
        {"id": 1, "nome": "Produto A", "preco": 19.99},
        {"id": 2, "nome": "Produto B", "preco": 29.99},
        {"id": 3, "nome": "Produto C", "preco": 39.99},
    ]
    return render_template("lista_produtos.html", produtos=produtos)

@produtos_bp.route("/detalhe/<int:produto_id>", methods=["GET"])
def detalhe_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "estoque": produto.estoque
    })