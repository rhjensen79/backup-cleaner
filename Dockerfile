FROM python:3.11-alpine
WORKDIR /app
COPY main.py main.py
CMD ["python3", "main.py"]
