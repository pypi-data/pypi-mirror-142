class deck(object):
    def __init__(self, deck_id: str, shuffled: bool, remaining: int):
        self.deck_id = deck_id
        self.shuffled = shuffled
        self.remaining = remaining
