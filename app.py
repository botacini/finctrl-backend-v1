from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")  # Railway define automaticamente esta variável
if DATABASE_URL is None:
    raise ValueError("A variável DATABASE_URL não está definida!")

# Ajustar a URL para SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo de exemplo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Rota inicial
@app.route("/")
def index():
    return jsonify({"message": "Backend funcionando corretamente!"})

# Inicializar o banco de dados
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
