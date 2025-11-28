from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Retorna uma página HTML simples
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Teste Flask</title>
    </head>
    <body>
        <h1>Hello, GitHub Actions!</h1>
        <p>Este é um teste de página HTML servida pelo Flask.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    # roda na porta 5000
    app.run(host="0.0.0.0", port=5000)
