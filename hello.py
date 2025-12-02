
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
            h1 {
                color: #006400;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
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
        <p>Há 100 anos, Calamity Ganon devastou Hyrule. Link desperta sem memórias e deve explorar um vasto mundo aberto, recuperar forças, libertar as Bestas Divinas e derrotar Ganon no Castelo de Hyrule. Com ajuda de Zelda, Ganon é selado e o reino começa a ser restaurado.</p>
        
        <div class="carousel">
            <div class="slides" id="slides">
                https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000000025/7137262b5a64d921e193653f8aa0b722925abc5680380ca0e18a5cfd91697f58
                https://wallpapercave.com/wp/wp3277308.jpg
                https://jogorama.com.br/arquivos/telas/the-legend-of-zelda-breath-of-the-wild/the-legend-of-zelda-breath-of-the-wild-24.jpg
                <img src="https://zelda.nintendo.com/breath-of-the-wild/es/media/" alt="Link e Zelda juntos">
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
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
