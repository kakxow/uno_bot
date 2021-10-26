from dataclasses import dataclass
import random
from typing import MutableSequence

from cards import Card, colors
from game_setup import starting_hand_size


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = list(cards)

    def draw(self, x: int = 1):
        res = self.cards[:x]
        self.cards = self.cards[x:]
        return res

    def shuffle(self):
        random.shuffle(self.cards)


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
        return regular_cards or wild or wild4

    def drop(self) -> Card:
        card = self.hand.pop(random.randint(0, len(self.hand)-1))
        if card.color == "black":
            color = ""
            while color not in colors:
                color = input("Select a new color - red, blue, yellow, green")
            card.color = color
        print(card)
        return card

    def play(self, play_choices: list[Card]) -> Card:
        #for i, card in enumerate(self.hand):
        #    print(i, card)
        print(*enumerate(play_choices), sep="\n")
        while True:
            card_id_raw = input("Select card id to play.")
            if card_id_raw.isdecimal():
                card_id = int(card_id_raw)
                if 0 <= card_id <= len(play_choices):
                    break
        played_card = play_choices[card_id]
        self.hand.remove(played_card)
        return played_card

    def turn(self, last_card: Card) -> Card:
        """ play a card if can """
        print(self)
        play_choices = self.check_hand(last_card)
        if play_choices:
            
            played_card = self.play(play_choices)
            if played_card.color == "black":
                color = ""
                while color not in colors:
                    color = input("Select a new color - red, blue, yellow, green")
                played_card.color = color
            print(played_card)
            return played_card
        else:
            print("draws a card")
            self.draw()
            return last_card

    def draw(self, x: int = 1):
        self.hand += self.deck.draw(x)
