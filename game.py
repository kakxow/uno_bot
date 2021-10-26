from cards import cards, Card
from stuff import Deck, Player


player_number = 4


deck = Deck(cards)
players: list[Player] = []


class Game:
    def __init__(self):
        pass

    def get_next_player(self) -> Player:
        pass

    def reverse_players(self):
        pass

    def start_session(self):
        """ Start a session of several games. """
        pass

    def play_card(self, card: Card):
        getattr(self, card.action)()

    def reverse(self):
        self.reverse_players()

    def skip(self):
        self.get_next_player()

    def draw_two(self):
        self.get_next_player().draw(2)

    def start_game(self, ):
        """ Start a game (one of many!) during this playing session. """
        deck.shuffle()
        self.players = [Player(str(i), [], deck) for i in range(1, player_number + 1)]  # temp
        current_player = self.get_next_player()
        last_card = current_player.play()
        while True:
            current_player = self.get_next_player()
            if last_card.action:
                self.play_card(last_card)
            else:
                pass
