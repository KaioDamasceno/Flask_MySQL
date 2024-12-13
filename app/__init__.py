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

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de Blueprints
    from app.rotas.auth import auth_bp
    from app.rotas.produtos import produtos_bp
    from app.rotas.carrinho import carrinho_bp
    from app.rotas.users import users_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(produtos_bp, url_prefix="/produtos")
    app.register_blueprint(carrinho_bp, url_prefix="/carrinho")
    app.register_blueprint(users_bp, url_prefix="/users")

    return app
