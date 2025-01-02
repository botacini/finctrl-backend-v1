from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import os

# Obter a variável de ambiente DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não está definida!")

# Conectar ao banco de dados
import psycopg2
from flask import Flask

app = Flask(__name__)

try:
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute("SELECT 1;")  # Teste básico para verificar a conexão
    cursor.close()
    connection.close()
except Exception as e:
    raise ValueError(f"Erro ao conectar ao banco de dados: {e}")

@app.route("/")
def hello():
    return "Conexão com o banco de dados foi bem-sucedida!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
