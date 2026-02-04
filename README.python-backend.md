# Python backend (FastAPI) — scaffold

How to run locally:
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r server_py/requirements.txt
4. uvicorn server_py.app.main:app --reload --host 0.0.0.0 --port 8000

Run tests:
- pytest -q

Dev notes:
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health
