from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurar a URL do banco de dados a partir da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")  # Railway define automaticamente esta variável
if DATABASE_URL is None:
    raise ValueError("A variável DATABASE_URL não está definida!")

# Ajustar a URL do banco de dados para ser compatível com o SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo de exemplo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Rota inicial para verificar se o app está rodando
@app.route("/")
def index():
    return jsonify({
