from DeckOfCard import Deck
from Player import Player


class CardGame:
    # new_deck = Deck()
    # player1 = Player("name")
    # player2 = Player("name")

    def __init__(self, player1_name = "player1", player2_name = "player2", num_of_cards: int = 26):
        self.num_of_cards = num_of_cards
        self.new_deck = Deck()
        self.player1 = Player(player1_name, self.num_of_cards)
        self.player2 = Player(player2_name, self.num_of_cards)
        self.was_already_new_game_used = False######  4b
        self.new_game()

    def new_game(self):

        #   4b   if called again
        if self.was_already_new_game_used:
            print("Error. Can run new game only once")
            return

        self.was_already_new_game_used = True###############   4b
        self.new_deck.cards_shuffle()
        self.player1.set_hand(self.new_deck)
        self.player2.set_hand(self.new_deck)

    def get_winner(self):
        #return only player
        if len(self.player1.player_cards) > len(self.player2.player_cards):
            return self.player1
        elif len(self.player1.player_cards) == len(self.player2.player_cards):
            return None
        else:
            return self.player2
        # if self.player1.player_cards > self.player2.player_cards:
        #     return f'Player 2 have less of cards', {self.player1}, 'Wins!'
        # elif self.player1.player_cards == self.player2.player_cards:
        #     return None
        # else:
        #     return f'Player 1 have less of cards', {self.player2}, 'Wins!'

    def __str__(self):
        return f"{self.player1} , {self.player2}"
