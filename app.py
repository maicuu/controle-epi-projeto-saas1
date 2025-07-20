# app.py
from flask import Flask, render_template

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define uma rota (URL) para a página inicial
@app.route('/')
def home():
    # Retorna uma simples mensagem de texto para o navegador
    return "Olá, mundo! Nosso projeto está começando!"

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento do Flask
    # debug=True permite que o servidor se recarregue automaticamente ao detectar mudanças
    app.run(debug=True)