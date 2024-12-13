from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint("auth", __name__, template_folder="../templates/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Autenticação simulada (substituir por lógica real)
        if username == "admin" and password == "admin":
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Credenciais inválidas.", "danger")

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Validação simples
        if password != confirm_password:
            flash("As senhas não coincidem.", "danger")
        else:
            # Registro simulado (substituir por lógica real)
            flash("Usuário registrado com sucesso!", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("auth.login"))
