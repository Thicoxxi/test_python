
FROM python:3.13
WORKDIR /app

# Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os scripts Python
COPY *.py .

# Define script fixo
CMD ["python", "/app/hello.py"]
