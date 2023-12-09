FROM python:3.11.6-slim

COPY iss_tracker.py /app/iss_tracker.py

RUN pip install requests

WORKDIR /app

CMD ["python", "iss_tracker.py"]
