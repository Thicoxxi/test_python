FROM python:3.13
WORKDIR /app
COPY requiments.txt .
RUN pip install --no-cache-dir -r requiments.txt

COPY hello.py .

CMD ["python", "hello.py"]
