FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY alembic.ini ./
COPY migrations/ ./migrations/

RUN useradd --create-home app
USER app

EXPOSE 8000

CMD ["uvicorn", "webhook_delivery.main:app", "--host", "0.0.0.0", "--port", "8000"]