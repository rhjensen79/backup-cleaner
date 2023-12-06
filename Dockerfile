FROM python:3.11.7-alpine
LABEL org.opencontainers.image.description Backup-Cleaner container for project https://github.com/rhjensen79/backup-cleaner
WORKDIR /app
COPY main.py main.py
CMD ["python3", "main.py"]
