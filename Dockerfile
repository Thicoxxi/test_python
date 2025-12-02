
FROM python:3.13
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

ARG SCRIPT=hello.py
ENV SCRIPT=$SCRIPT

CMD sh -c "python /app/$SCRIPT"
