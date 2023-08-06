from src.api.Card import Card


class DrawnCards(object):
    def __init__(self, cards: list[Card], deck_id: str, remaining: int):
        self.cards = cards
        self.deck_id = deck_id
        self.remaining = remaining