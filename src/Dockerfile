FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]