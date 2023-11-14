from abc import ABC, abstractmethod
from typing import List
from api.Types import (MapInfo, DeckAPI, APIGameStartState, APIGameState, APICommand, ApiHello, APIPrepare, AiForMapAPI,
                       VERSION)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

global _BOT


class BotImpl(ABC, BaseModel):
    @abstractmethod
    def __init__(self, map_info: MapInfo, deck: DeckAPI):
        super().__init__()

    @staticmethod
    @abstractmethod
    def name() -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def decks_for_map(map_info: MapInfo) -> List[DeckAPI]:
        raise NotImplementedError

    @abstractmethod
    def match_start(self, state: APIGameStartState):
        raise NotImplementedError

    @abstractmethod
    def tick(self, state: APIGameState) -> List[APICommand]:
        raise NotImplementedError


app = FastAPI()


@app.post("/hello")
async def hello_endpoint(hello: ApiHello) -> AiForMapAPI:
    if hello.version != VERSION:  # Check version compatibility
        raise HTTPException(status_code=422, detail="Version mismatch")

    decks = _BOT.decks_for_map(hello.map)
    return AiForMapAPI(name=_BOT.name(), decks=decks)


@app.post("/prepare")
async def prepare_endpoint(prepare: APIPrepare):
    deck = prepare.deck
    decks = _BOT.decks_for_map(prepare.map_info)
    supported_deck = next((d for d in decks if d.name == deck), None)
    if supported_deck is None:
        raise HTTPException(status_code=422, detail="Deck not supported on map")


@app.post("/start")
async def start_endpoint(start: APIGameStartState):
    _BOT.match_start(start)


@app.post("/tick")
async def tick_endpoint(state: APIGameState):
    commands = _BOT.tick(state)
    return commands


def run(bot: BotImpl, port: int):
    global _BOT
    _BOT = bot
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=port)
