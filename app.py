# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicialização do banco de dados e migração
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de Blueprints (rotas modularizadas)
    from app.rotas.auth import auth_bp
    from app.rotas.produtos import produtos_bp
    from app.rotas.carrinho import carrinho_bp
    from app.rotas.users import users_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(produtos_bp, url_prefix="/produtos")
    app.register_blueprint(carrinho_bp, url_prefix="/carrinho")
    app.register_blueprint(users_bp, url_prefix="/users")

    # Página inicial
    @app.route("/")
    def index():
        return "gap"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)