from typing import List

from pydantic import BaseModel

import api.Wrapper
from api import Types
from api.CardTemplate import CardTemplate
from api.Helpers import PositionExtension
from api.Maps import Maps
from api.Types import (MapInfo, DeckAPI, APIGameStartState, APIGameState, Position2D,
                       APICommand, APICommandProduceSquad,
                       APICommandGroupAttack)
from api.Wrapper import BotImpl


# /AI: add PythonExampleBot MA_spam 4


class MyBot(BotImpl, BaseModel):
    def __init__(self, map_info: MapInfo, deck: DeckAPI):
        super().__init__(map_info, deck)
        self._my_id = 0
        self._my_team = 0
        self._opponents: List[int] = []
        self._my_start = Position2D(x=0.0, y=0.0)
        self._deck = deck

    def set_id(self, my_id: int):
        self._my_id = my_id

    def get_id(self) -> int:
        return self._my_id

    def set_team(self, team: int):
        self._my_team = team

    def get_team(self) -> int:
        return self._my_team

    def set_opponents(self, opponents: List[int]):
        self._opponents = opponents

    def push_opponent(self, opponent: int):
        self._opponents.append(opponent)

    def get_opponents(self) -> List[int]:
        return self._opponents

    def set_start(self, my_start: Position2D):
        self._my_start = my_start

    def get_start(self) -> Position2D:
        return self._my_start

    def set_deck(self, deck: DeckAPI):
        self._deck = deck

    @staticmethod
    def name() -> str:
        return "PythonExampleBot"

    @staticmethod
    def decks_for_map(map_info: MapInfo) -> List[DeckAPI]:
        masterarcher_spam_deck_cards = [CardTemplate.MasterArchers, CardTemplate.IceBarrier, CardTemplate.HomeSoil,
                                        CardTemplate.GlyphofFrost, CardTemplate.NotACard, CardTemplate.NotACard,
                                        CardTemplate.NotACard, CardTemplate.NotACard, CardTemplate.NotACard,
                                        CardTemplate.NotACard, CardTemplate.NotACard, CardTemplate.NotACard,
                                        CardTemplate.NotACard, CardTemplate.NotACard, CardTemplate.NotACard,
                                        CardTemplate.NotACard, CardTemplate.NotACard, CardTemplate.NotACard,
                                        CardTemplate.NotACard, CardTemplate.NotACard]
        masterarcher_spam_deck = DeckAPI(name="MA_spam", cover_card_index=0, cards=masterarcher_spam_deck_cards)
        match map_info.map:
            case Maps.Elyon:
                # Select a deck specifically for Elyon
                pass
            case Maps.Haladur:
                # Select a deck specifically for Haladur
                pass

        return [masterarcher_spam_deck]

    def match_start(self, start_state: APIGameStartState):
        your_player_id = start_state.your_player_id
        self.set_id(your_player_id)

        entities = start_state.entities

        for player in start_state.players:
            if player.entity.id == your_player_id:
                self._my_team = player.entity.team

        for player in start_state.players:
            if player.entity.team != self.get_team():
                self.push_opponent(player.entity.id)

        for entity in entities:
            if entity.specific.__class__ is Types.APIEntitySpecificPowerSlot:
                if entity.player_entity_id == your_player_id:
                    print("I own powerwell " + str(entity.id) + " at position " + str(entity.position))
            elif entity.specific.__class__ is Types.APIEntitySpecificTokenSlot:
                if entity.player_entity_id == your_player_id:
                    print("I own monument " + str(entity.id) + " at position " + str(entity.position))
                    self.set_start(PositionExtension.to2d(entity.position))

    def tick(self, state: APIGameState) -> List[APICommand]:
        current_tick = state.current_tick
        entities = state.entities
        print("Current tick: " + str(current_tick) + " entities count: " + str(len(entities)))

        my_army = []
        target = None
        my_power = 0.0

        for player in state.players:
            if player.id == self.get_id():
                my_power = player.power

        for entity in entities:
            if entity.specific.__class__ is Types.APIEntitySpecificSquad:
                if self.get_id() == entity.player_entity_id:
                    my_army.append(entity.id)
            elif entity.specific.__class__ is Types.APIEntitySpecificTokenSlot:
                if entity.player_entity_id in self.get_opponents():
                    target = entity.id

        print(f'Current tick: {current_tick} target: {target} my power: {my_power} my army: {my_army}')

        commands: List[APICommand] = []
        if my_power >= 50.0:
            spawn = APICommandProduceSquad(card_position=0, xy=self.get_start())
            commands.append(spawn)
        if target is not None and len(my_army) > 0:
            attack = APICommandGroupAttack(squads=my_army, target_entity_id=target, force_attack=False)
            commands.append(attack)

        return commands


def main(port: int):
    mapinfo = MapInfo(map=Maps.ElyonSpectator, community_map_details=None)
    deck = MyBot.decks_for_map(mapinfo)[0]
    bot = MyBot(mapinfo, deck)
    api.Wrapper.run(bot, port)
