from pydantic import BaseModel
from typing import List, Optional


class GameCreateRequest(BaseModel):
    players: List[str]


class GameResponse(BaseModel):
    id: int
    players: List[str]
    state: Optional[str] = None