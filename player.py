from dataclasses import dataclass
import random

from card import Card
from deck import Deck
from game_setup import starting_hand_size


@dataclass()
class Player:
    name: str
    id: int
    hand: list[Card]
    score: int = 0

    def __init__(self, name: str, id: int, hand: list[Card], deck: Deck, score: int = 0):
        self.name = name
        self.id = id
        self.hand = hand
        self.deck = deck
        self.score = score
        self.draw(starting_hand_size)

    def is_eligible_for_play(self, card_in_hand: Card, card_on_table: Card) -> bool:
        return (card_in_hand.color == card_on_table.color or  # same color
                card_in_hand.value == card_on_table.value and card_in_hand.value is not None or  # or same value
                card_in_hand.action == card_on_table.action and card_in_hand.action != "")  # or same action

    def check_hand(self, last_played_card: Card) -> list[Card]:
        regular_cards: list[Card] = []
        wild: list[Card] = []
        wild4: list[Card] = []
        for card in self.hand:
            if self.is_eligible_for_play(card, last_played_card):
                regular_cards.append(card)
            else:
                match card.action:
                    case "wild": wild.append(card)
                    case "wild_draw_four": wild4.append(card)
                    case _: pass
        return regular_cards + wild or wild4

    def discard(self) -> Card:
        """ Play random card. """
        card = self.hand.pop(random.randint(0, len(self.hand)-1))
        return card

    def play_card(self, card: Card) -> Card:
        self.hand.remove(card)
        return card

    def choose_card(self, play_choices: list[Card]) -> Card | None:
        while True:
            card_id_raw = input("Select card id to play or type 'draw' to draw a card.")
            if card_id_raw.isdecimal():
                card_id = int(card_id_raw)
                if 0 <= card_id <= len(play_choices):
                    played_card = play_choices[card_id]
                    return played_card
            elif card_id_raw == "draw":
                print("draws a card")
                self.draw()
                return

    def turn(self, last_card: Card, new_card: bool = False) -> Card:
        """ play a card if can """
        play_choices = self.check_hand(last_card)
        if play_choices:
            print(*enumerate(play_choices), sep="\n")
            chosen_card = self.choose_card(play_choices)
            if chosen_card:
                return self.play_card(chosen_card)
            else:
                return last_card
        else:
            if new_card:
                return last_card
            print("draws a card")
            self.draw()
            return self.turn(last_card, True)

    def draw(self, x: int = 1):
        self.hand += self.deck.draw(x)
