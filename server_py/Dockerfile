FROM python:3.11-slim

WORKDIR /app

COPY server_py/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server_py/ ./server_py/

ENV PYTHONPATH=/app

CMD ["uvicorn", "server_py.app.main:app", "--host", "0.0.0.0", "--port", "8000"]