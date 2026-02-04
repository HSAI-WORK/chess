from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import GameCreateRequest, GameResponse

router = APIRouter()

# in-memory store for scaffold (replace with DB in full migration)
_games = {}
_next_id = 1


@router.post("/", response_model=GameResponse)
async def create_game(payload: GameCreateRequest):
    global _next_id
    game_id = _next_id
    _next_id += 1
    game = {"id": game_id, "players": payload.players, "state": "new"}
    _games[game_id] = game
    return game


@router.get("/", response_model=List[GameResponse])
async def list_games():
    return list(_games.values())


@router.get("/{game_id}", response_model=GameResponse)
async def get_game(game_id: int):
    game = _games.get(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game