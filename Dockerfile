FROM python:3.13
WORKDIR /app
COPY requiments.txt .
# instala bibliotecas necessarias para rodar a aplicação
RUN pip install --no-cache-dir -r requiments.txt
# Copia todos os scripts Python
COPY *.py .

# Define argumento para escolher o script
ARG SCRIPT=hello.py
ENV SCRIPT=${SCRIPT}

# Executa o script definido
CMD ["python", "${SCRIPT}"]