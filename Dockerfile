
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia dependências primeiro (melhor para cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código e arquivos estáticos
COPY app.py .
COPY static ./static

# Expõe a porta do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]