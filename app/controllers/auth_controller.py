import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
# Correção de um erro de não reconhecimento da pasta "app"

from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import User
from database import db

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

        # Verificar se todos os campos foram preenchidos
        if not username or not password or not confirm_password:
            flash("Por favor, preencha todos os campos.", "danger")
            return redirect(url_for("auth.register"))

        # Verificar se as senhas coincidem
        if password != confirm_password:
            flash("As senhas não coincidem.", "danger")
            return redirect(url_for("auth.register"))

        # Gera o hash da senha
        hashed_password = generate_password_hash(password)

        # Salva o usuário no banco de dados
        novo_usuario = User(nome=username, email=f"{username}@example.com", senha=hashed_password)
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Usuário registrado com sucesso!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("auth.login"))
