# config.py
import os

class Config:
    """Configurações padrão para a aplicação."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///db.sqlite3"
    )  # Banco padrão SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False