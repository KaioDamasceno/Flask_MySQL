from database import db

class Carrinho(db.Model):
    __tablename__ = 'carrinhos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    produtos = db.relationship('CarrinhoProduto', back_populates='carrinho')

class CarrinhoProduto(db.Model):
    __tablename__ = 'carrinho_produtos'
    id = db.Column(db.Integer, primary_key=True)
    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinhos.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    carrinho = db.relationship('Carrinho', back_populates='produtos')
    produto = db.relationship('Produto')
