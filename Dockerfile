FROM python:3.13

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install --upgrade pip

CMD ["python", "app/main.py"]
