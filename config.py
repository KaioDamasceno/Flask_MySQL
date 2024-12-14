import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "uma_chave_secreta_muito_segura")  # Substitua por uma chave única e forte
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"  # Banco de dados SQLite (ou ajuste conforme necessário)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
