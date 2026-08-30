FROM python:3.13-slim

WORKDIR /app
COPY src/hivebox/version.py .

ENTRYPOINT ["python", "version.py"]
