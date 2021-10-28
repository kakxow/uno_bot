import random

from card import Card


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = list(cards)

    def draw(self, x: int = 1) -> list[Card]:
        res = self.cards[:x]
        self.cards = self.cards[x:]
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def return_card(self, card: Card):
        self.cards.append(card)
        self.shuffle()

    def __len__(self):
        return len(self.cards)
