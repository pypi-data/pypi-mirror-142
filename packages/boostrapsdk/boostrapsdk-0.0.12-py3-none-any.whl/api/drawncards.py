from src.api.card import card


class drawncards(object):
    def __init__(self, cards: list[card], deck_id: str, remaining: int):
        self.cards = cards
        self.deck_id = deck_id
        self.remaining = remaining