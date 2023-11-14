from api.Types import Position, Position2D, CardId, Upgrade
from api.CardTemplate import CardTemplate


class PositionExtension:
    @staticmethod
    def to2d(position: Position) -> Position2D:
        return Position2D(x=position.x, y=position.z)


class Position2DExt:
    @staticmethod
    def zero() -> Position2D:
        return Position2D(x=0.0, y=0.0)


def new_card_id(ct: CardTemplate, u: Upgrade):
    return CardId(ct + u)
