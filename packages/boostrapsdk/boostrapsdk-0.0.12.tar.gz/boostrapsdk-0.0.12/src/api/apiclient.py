import json

from src.api.card import card
from src.api.deck import deck
from src.api.drawncards import drawncards
from src.api.fetchcache import fetchcache


class apiclient(object):
    def __init__(self, key: str, **options):
        self.key = key
        logger = options.get('logger', False)
        if logger:
            self.logger = logger
        else:
            self.logger = print
        self.cache = fetchcache(ttl_ms=5 * 1000)

    @staticmethod
    def shuffle_new_deck(count: int):
        return f'https://deckofcardsapi.com/api/deck/new/shuffle?count={count}'

    @staticmethod
    def draw_from_deck_url(deck_id: str, count: int):
        return f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}'

    @staticmethod
    def reshuffle_deck(deck_id: str, remaining: bool):
        return f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle?remaining={remaining}'

    @staticmethod
    def get_new_deck_url():
        return 'https://deckofcardsapi.com/api/deck/new'

    def draw_cards(self, deck_id: str, count: int):
        try:
            r = self.cache.get(apiclient.draw_from_deck_url(deck_id, count))
            j = json.loads(r.text)
            cards = j['cards']
            mapped_cards = map(lambda card: card(image=card['image'], value=card['value'], suit=card['suit'], code=card['code']), cards)
            d = drawncards(cards=list(mapped_cards), deck_id=j['deck_id'], remaining=j['remaining'])
            return d
        except Exception as e:
            print(f'Request failed, retrying, {e}')
            return None

    def get_new_deck(self):
        try:
            r = self.cache.get(apiclient.get_new_deck_url())
            j = json.loads(r.text)
            d = deck(deck_id=j['deck_id'], shuffled=j['shuffled'], remaining=j['remaining'])
            return d
        except Exception as e:
            print(f'Request failed, retrying, {e}')
            return None



