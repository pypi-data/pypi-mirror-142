import json
import requests
import time


class Deck(object):
    def __init__(self, deck_id: str, shuffled: bool, remaining: int):
        self.deck_id = deck_id
        self.shuffled = shuffled
        self.remaining = remaining


class FetchCache(object):
    cache = {}

    def __init__(self, **options):
        self.ttl_ms = options.get('ttl_ms')
        self.response = {}
        logger = options.get('logger', False)
        if logger:
            self.logger = logger
        else:
            self.logger = print

    def get(self, url: str):
        self.__trim_cache()
        try:
            hit = FetchCache.cache[url]
            return hit[1]
        except KeyError:
            ms = int(time.time() * 1000.0)
            response = self.__get_url_with_retry(url)
            FetchCache.cache[url] = [ms, response]
            return response

    def __trim_cache(self):
        keys_to_delete = []
        for url, items in FetchCache.cache.items():
            now = int(time.time() * 1000.0)
            should_purge = (items[0] + self.ttl_ms) < now
            if should_purge:
                keys_to_delete.append(url)
        for key in keys_to_delete:
            del FetchCache.cache[key]

    @staticmethod
    def __get_url_with_retry(url: str):
        attempts = 0
        max_attempts = 3
        backoff_times = [10, 1000, 10000]
        while attempts < max_attempts:
            try:
                response = requests.get(url)
                return response
            except Exception as e:
                time.sleep(backoff_times[attempts])
                print(f'Request failed, retrying, {e}')
                attempts += 1

        raise Exception(f'Maximum attempts ({attempts}) made to the resource with no valid response')


class Card(object):
    def __init__(self, image: str, value: str, suit: str, code: str):
        self.image = image
        self.value = value
        self.suit = suit
        self.code = code


class DrawnCards(object):
    def __init__(self, cards: list[Card], deck_id: str, remaining: int):
        self.cards = cards
        self.deck_id = deck_id
        self.remaining = remaining


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



