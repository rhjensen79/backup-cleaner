FROM python:3.12-alpine
WORKDIR /app
COPY main.py main.py
CMD ["python3", "main.py"]
