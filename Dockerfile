FROM python:3.11-slim

WORKDIR /app
COPY requiments.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello.py .

CMD ["python", "hello.py"]
