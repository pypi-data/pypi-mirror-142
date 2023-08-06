class Card(object):
    def __init__(self, image: str, value: str, suit: str, code: str):
        self.image = image
        self.value = value
        self.suit = suit
        self.code = code