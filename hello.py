
from flask import Flask

app = Flask(__name__)

@app.route("/")
def zelda_crawl():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>The Legend of Zelda Crawl</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            overflow: hidden;
            background: black;
            color: #00ff00;
            font-family: 'Arial', sans-serif;
        }
        .zelda {
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
    <div class="zelda">
        <div class="crawl">
            <p>Há muito tempo, no reino de Hyrule...</p>
            <p>Calamity Ganon despertou e trouxe destruição.</p>
            <p>Link deve recuperar suas memórias e salvar Zelda.</p>
            <p>Que a Triforce guie sua jornada!</p>
        </div>
    </div>
</body>
</html>
    """

@app.route("/zelda")
def zelda_story():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>História de Zelda</title>
    <style>
        body {
            background: #f4f4f4;
            font-family: 'Arial', sans-serif;
            color: #333;
            padding: 20px;
            text-align: center;
        }
        h1 { color: #006400; }
        .carousel {
            position: relative;
            width: 80%;
            margin: 20px auto;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .slides {
            display: flex;
            transition: transform 0.5s ease-in-out;
        }
        .slides img {
            width: 100%;
            border-radius: 10px;
        }
        .buttons {
            position: absolute;
            top: 50%;
            width: 100%;
            display: flex;
            justify-content: space-between;
            transform: translateY(-50%);
        }
        .buttons button {
            background: rgba(0,0,0,0.5);
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>The Legend of Zelda: Breath of the Wild</h1>
    <p>Há 100 anos, Calamity Ganon devastou Hyrule, mergulhando o reino em caos e destruição.</p>
    <p>Link desperta após um longo sono sem memórias, guiado por uma voz misteriosa que o chama para salvar a princesa Zelda.</p>
    <p>Para derrotar Ganon, Link deve explorar um vasto mundo aberto, enfrentar inimigos poderosos, recuperar suas forças e libertar as quatro Bestas Divinas.</p>
    <p>Cada passo revela segredos antigos, desafios épicos e a verdadeira história da Triforce.</p>
    <p>Com coragem e determinação, Link embarca em uma jornada para restaurar a paz em Hyrule e cumprir seu destino como herói lendário.</p>

    <div class="carousel">
        <div class="slides" id="slides">
            <img src="/static/images/zelda1.jpg" altmg src="/static/images/zelda2.jpg
            <img src="/static/images/zelda3.jpg
        </div>
        <div class="buttons">
            <button onclick="prevSlide()">&#10094;</button>
            <button onclick="nextSlide()">&#10095;</button>
        </div>
    </div>

    <script>
        let index = 0;
        const slides = document.getElementById('slides');
        const totalSlides = slides.children.length;

        function showSlide() {
            slides.style.transform = 'translateX(' + (-index * 100) + '%)';
        }

        function nextSlide() {
            index = (index + 1) % totalSlides;
            showSlide();
        }

        function prevSlide() {
            index = (index - 1 + totalSlides) % totalSlides;
            showSlide();
        }

        // Mostra a primeira imagem ao carregar
        showSlide();
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
