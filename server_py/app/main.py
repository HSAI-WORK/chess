from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import games
from .core.config import settings

app = FastAPI(title="Chess Backend (FastAPI)", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(games.router, prefix="/api/v1/games", tags=["games"])


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}