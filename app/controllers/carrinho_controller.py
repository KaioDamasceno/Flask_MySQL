from flask import Blueprint, render_template, request, redirect, url_for, flash

carrinho_bp = Blueprint("carrinho", __name__, template_folder="../templates/carrinhos")

# Simulação de um carrinho de compras (substituir com lógica real)
carrinho = []

@carrinho_bp.route("/", methods=["GET"])
def visualizar_carrinho():
    total = sum(item["preco"] for item in carrinho)
    return render_template("view_cart.html", carrinho=carrinho, total=total)

@carrinho_bp.route("/adicionar/<int:produto_id>", methods=["POST"])
def adicionar_ao_carrinho(produto_id):
    # Simulação de produto (substituir com consulta ao banco de dados)
    produto = {"id": produto_id, "nome": f"Produto {chr(64 + produto_id)}", "preco": 19.99 * produto_id}
    carrinho.append(produto)
    flash(f"{produto['nome']} foi adicionado ao carrinho.", "success")
    return redirect(url_for("produtos.lista_produtos"))

@carrinho_bp.route("/remover/<int:produto_id>", methods=["POST"])
def remover_do_carrinho(produto_id):
    global carrinho
    carrinho = [item for item in carrinho if item["id"] != produto_id]
    flash(f"Produto removido do carrinho.", "info")
    return redirect(url_for("carrinho.visualizar_carrinho"))