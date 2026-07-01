FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .

EXPOSE 8080

CMD ["python", "main.py"]
