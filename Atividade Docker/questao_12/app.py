# Arquivo: app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá! O Flask está rodando dentro do Docker na porta 5000!"

if __name__ == '__main__':
    # Define a porta 5000 e libera o acesso externo ao container
    app.run(host='0.0.0.0', port=5000)