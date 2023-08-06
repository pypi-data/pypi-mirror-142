import json

from src.api.deck import Deck
from src.api.drawncards import DrawnCards
from src.api.fetchcache import FetchCache

class ApiClient(object):
    def __init__(self, key: str, **options):
        self.__key = key
        logger = options.get('logger', False)
        if logger:
            self.__logger = logger
        else:
            self.__logger = print
        self.__cache = FetchCache(ttl_ms=5 * 1000)

    @staticmethod
    def __shuffle_new_deck(count: int):
        return f'https://deckofcardsapi.com/api/deck/new/shuffle?count={count}'

    @staticmethod
    def __draw_from_deck_url(deck_id: str, count: int):
        return f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}'

    @staticmethod
    def __reshuffle_deck(deck_id: str, remaining: bool):
        return f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle?remaining={remaining}'

    @staticmethod
    def __get_new_deck_url():
        return 'https://deckofcardsapi.com/api/deck/new'

    def draw_cards(self, deck_id: str, count: int):
        try:
            r = self.__cache.get(self.__draw_from_deck_url(deck_id, count))
            j = json.loads(r.text)
            cards = j['cards']
            mapped_cards = map(lambda card: card(image=card['image'], value=card['value'], suit=card['suit'], code=card['code']), cards)
            d = DrawnCards(cards=list(mapped_cards), deck_id=j['deck_id'], remaining=j['remaining'])
            return d
        except Exception as e:
            print(f'Request failed, retrying, {e}')
            return None

    def get_new_deck(self):
        try:
            r = self.__cache.get(ApiClient.__get_new_deck_url())
            j = json.loads(r.text)
            d = Deck(deck_id=j['deck_id'], shuffled=j['shuffled'], remaining=j['remaining'])
            return d
        except Exception as e:
            print(f'Request failed, retrying, {e}')
            return None



