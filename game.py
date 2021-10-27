from cards import cards, Card, colors
from stuff import Deck, Player


player_number = 2


class Game:
    def __init__(self):
        self.deck = Deck(cards)
        self.discard: list[Card] = []
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
        if card.action in self.__dict__:
            getattr(self, card.action)()

    def reverse(self):
        self.reverse_players()

    def skip(self):
        pass

    def draw_two(self):
        self.current_player.draw(2)

    def wild(self):
        pass

    def wild_draw_four(self):
        self.current_player.draw(4)

    def wild_swap_hands(self):
        print(*enumerate([player.name for player in self.players if player != self.current_player]), sep="\n")
        while True:
            player_id_raw = input("Select a player: ")
            if player_id_raw.isdecimal():
                player_id = int(player_id_raw)
                if 0 <= player_id <= len(self.players):
                    break
        self.current_player.hand, self.players[player_id].hand = self.players[player_id].hand, self.current_player.hand

    def wild_shuffle_hands(self):
        hands_combined = [card for player in self.players for card in player.hand]
        temp_deck = Deck(hands_combined)
        temp_deck.shuffle()
        new_hand_size = round(len(temp_deck) / len(self.number_of_players))
        for player in self.players:
            player.draw(new_hand_size)

    def check_black(self, played_card: Card) -> Card:
        if played_card.color == "black":
            color = ""
            while color not in colors:
                color = input("Select a new color - red, blue, yellow, green. ")
            played_card.color = color
        return played_card

    def check_wild_at_start(self):
        while self.last_card.action == "wild_draw_four":
            self.deck.return_card(self.last_card)
            self.last_card = self.deck.draw()[0]
        if self.last_card.action == "wild_shuffle_hands":
            self.last_card.is_active = False

    def start_game(self):
        """ Start a game (one of many!) during this playing session. """
        self.deck.shuffle()
        self.players = [Player(str(i), [], self.deck) for i in range(player_number)]
        self.current_player = self.players[0]
        self.last_card = self.current_player.discard()
        self.check_wild_at_start()
        self.discard.append(self.last_card)
        self.last_card = self.check_black(self.last_card)
        print(self.last_card, self.last_card.is_active)
        while True:
            if not self.deck:
                self.deck = Deck(self.discard)
            self.current_player = self.get_next_player()
            print(self.current_player)
            if self.last_card.action and self.last_card.is_active:
                self.card_action(self.last_card)
                self.last_card.is_active = False
                print(self.last_card, self.last_card.is_active)
            else:
                self.last_card = self.current_player.turn(self.last_card)
                self.discard.append(self.last_card)
                if len(self.current_player.hand) == 1:
                    print("UNO!")
                self.last_card = self.check_black(self.last_card)
                if not self.current_player.hand:
                    print(f"Player {self.current_player.name} won!")
                    break
        # self.score()


game = Game()
game.start_game()
