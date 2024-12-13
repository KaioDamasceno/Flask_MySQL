from flask import Blueprint, render_template, request, redirect, url_for, flash

users_bp = Blueprint("users", __name__, template_folder="../templates")

# Simulação de usuários (substituir com consulta ao banco de dados)
usuarios = [
    {"id": 1, "nome": "Admin", "email": "admin@example.com", "role": "admin"},
    {"id": 2, "nome": "User", "email": "user@example.com", "role": "user"}
]

@users_bp.route("/", methods=["GET"])
def listar_usuarios():
    return render_template("index.html", usuarios=usuarios)

@users_bp.route("/editar/<int:user_id>", methods=["GET", "POST"])
def editar_usuario(user_id):
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if not usuario:
        flash("Usuário não encontrado.", "danger")
        return redirect(url_for("users.listar_usuarios"))

    if request.method == "POST":
        usuario["nome"] = request.form.get("nome")
        usuario["email"] = request.form.get("email")
        flash("Usuário atualizado com sucesso!", "success")
        return redirect(url_for("users.listar_usuarios"))

    return render_template("editar.html", usuario=usuario)

@users_bp.route("/remover/<int:user_id>", methods=["POST"])
def remover_usuario(user_id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != user_id]
    flash("Usuário removido com sucesso!", "info")
    return redirect(url_for("users.listar_usuarios"))