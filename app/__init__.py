# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicializa as extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Inicializa a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Garante que uma SECRET_KEY esteja definida
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY não definida. Configure-a no Config.")

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.produtos_controller import produtos_bp
    from app.controllers.carrinho_controller import carrinho_bp
    from app.controllers.users_controller import users_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(produtos_bp, url_prefix="/produtos")
    app.register_blueprint(carrinho_bp, url_prefix="/carrinho")
    app.register_blueprint(users_bp, url_prefix="/users")

    return app


