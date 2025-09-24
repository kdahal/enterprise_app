# Dockerfile
# Configures the production environment using Docker.

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

CMD ["uvicorn", "enterprise_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
