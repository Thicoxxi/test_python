
FROM python:3.13

# Define diretório de trabalho
WORKDIR /app

# Copia dependências primeiro (melhor para cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código e arquivos estáticos
COPY hello.py .
COPY static ./static

# Expõe a porta do Flask
EXPOSE 5000

CMD ["python", "hello.py"]
