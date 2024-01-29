FROM python:alpine3.19
WORKDIR /app
COPY main.py main.py
CMD ["python3", "main.py"]
