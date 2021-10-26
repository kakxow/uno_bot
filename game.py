from typing import Generator
from cards import cards, Card, colors
from stuff import Deck, Player


player_number = 2


deck = Deck(cards)
players: list[Player] = []


class Game:
    def __init__(self):
        self.number_of_players = player_number
        self.current_player_id = 0
        self.player_increment = 1

    def get_next_player(self) -> Player:
        self.current_player_id += self.player_increment
        if self.current_player_id > self.number_of_players - 1:
            self.current_player_id = 0
        elif self.current_player_id < 0:
            self.current_player_id = self.number_of_players - 1
        return self.players[self.current_player_id]

    def reverse_players(self):
        self.player_increment *= -1

    def card_action(self, card: Card):
        getattr(self, card.action)()

    def reverse(self):
        self.reverse_players()
        # self.get_next_player()  # cuz next player is picked before the card action plays.

    def skip(self):
        pass
        # self.get_next_player()

    def draw_two(self):
        self.current_player.draw(2)

    def wild(self):
        pass

    def wild_draw_four(self):
        self.current_player.draw(4)
    
    def start_game(self):
        """ Start a game (one of many!) during this playing session. """
        deck.shuffle()
        self.players: list[Player] = []
        for i in range(player_number):
            self.players.append(Player(str(i), [], deck))
        # breakpoint()
        print(*self.players, sep="\n")
        
        # self.players = [Player(str(i), [], deck) for i in range(1, player_number + 1)]  # temp
        self.current_player = self.get_next_player()
        self.last_card = self.current_player.drop()
        breakpoint()
        while True:
            self.current_player = self.get_next_player()
            if self.last_card.action and self.last_card.is_active:
                self.card_action(self.last_card)
                self.last_card.is_active = False
                print(self.last_card)
            else:
                self.last_card = self.current_player.turn(self.last_card)
                if not self.current_player.hand:
                    print(f"{self.current_player.name} won!")
                    break
        # self.score()

game = Game()
game.start_game()

