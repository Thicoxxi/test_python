from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Retorna uma página HTML com efeito Star Wars
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Star Wars Crawl</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                overflow: hidden;
                background: black;
                color: yellow;
                font-family: 'Arial', sans-serif;
            }
            .star-wars {
                position: relative;
                height: 100vh;
                perspective: 400px;
                overflow: hidden;
            }
            .crawl {
                position: absolute;
                bottom: -100%;
                width: 100%;
                transform-origin: 50% 100%;
                transform: rotateX(20deg);
                animation: crawl 60s linear infinite;
                text-align: center;
                font-size: 2em;
                line-height: 1.5em;
            }
            @keyframes crawl {
                0% { bottom: -100%; }
                100% { bottom: 100%; }
            }
        </style>
    </head>
    <body>
        <div class="star-wars">
            <div class="crawl">
                <p>Há muito tempo, em uma galáxia muito, muito distante...</p>
                <p>Este é um teste de página Flask com efeito Star Wars!</p>
                <p>Que a Força esteja com você.</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
