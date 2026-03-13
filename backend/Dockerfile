FROM python:3.11

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -r backend/requirements.txt

CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8000"]