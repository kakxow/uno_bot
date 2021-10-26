from dataclasses import dataclass
import random

from cards import Card, special_colors
from game_setup import starting_hand_size


class Deck(list):
    def draw(self, x: int = 1):
        res = self[:x]
        self = self[x:]  # type: ignore
        return res

    def shuffle(self):
        random.shuffle(self)


@dataclass()
class Player:
    name: str
    hand: list[Card]
    score: int = 0

    def __init__(self, name: str, hand: list[Card], deck: Deck, score: int = 0):
        self.name = name
        self.hand = hand
        self.deck = deck
        self.score = score
        self.draw(starting_hand_size)

    def is_eligible_for_play(self, card_in_hand: Card, card_on_table: Card) -> bool:
        return (card_in_hand.color == card_on_table.color or
                card_in_hand.value == card_on_table.value or
                card_in_hand.action == card_on_table.action or
                card_in_hand.color in special_colors)

    def check_hand(self, last_played_card: Card) -> list[Card]:
        return [card for card in self.hand if self.is_eligible_for_play(card, last_played_card)]

    def is_win(self, play_choices: list[Card]) -> bool:
        return len(play_choices) == 1 and len(self.hand) == 2

    def play(self):
        return self.hand.pop(random.randint(0, len(self.hand) + 1))

    def draw(self, x: int):
        self.hand += self.deck.draw(x)
