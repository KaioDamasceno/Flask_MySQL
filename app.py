# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.controllers import auth_bp, produtos_bp, carrinho_bp, users_bp
from database import db, init_db
# Inicialização do banco de dados e migração




 # Registro de Blueprints (rotas modularizadas)
app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(produtos_bp, url_prefix="/produtos")
app.register_blueprint(carrinho_bp, url_prefix="/carrinho")
app.register_blueprint(users_bp, url_prefix="/users")

    

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)