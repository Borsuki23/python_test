FROM python:3.10.3-slim

WORKDIR /app

COPY . .


CMD ["python", "docker_function.py", "10"]

