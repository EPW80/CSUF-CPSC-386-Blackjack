# Erik Williams
# CPSC 386-02
# 2023-02-24
# epwilliams@csu.fullerton.edu
# @EPW80
#
# Lab 02-00
#
# A simple blackjack game.
#

""" A Deck of 52 cards """

import random
from blackjackgame.cards import Deck
from blackjackgame.player import Player


class BlackjackGame:
    """Game logic for a Blackjack game"""

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.players = {}
        self.deck = Deck()
        self.cut_card = None
        self.dealer_hand = []
        self.game_over = False

        # Create players
        for i in range(self.number_of_players):
            name = input(f"Enter name for player {i + 1}: ")
            player = Player(name, player_id=i)
            player.prompt_for_bet()
            self.players[player.player_id] = player

            while True:
                response = self.players[player.player_id].ask_for_hit()
                if response.lower() == "y":
                    card = self.deck.draw_card()
                    self.players[player.player_id].hand.append(card)
                    print(f"{name} was dealt {card}")
                elif response.lower() == "n":
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue
                player_score = self.calculate_score(
                    self.players[player.player_id].hand
                )
                if player_score > 21:
                    print(f"{name} busts with {player_score}.")
                    break
                if player_score == 21:
                    print(f"{name} has blackjack!")
                    break

            self.check_for_game_over()

    def shuffle_deck(self):
        """Shuffles the deck of cards"""
        self.deck.shuffle()

    def cut_deck(self):
        """Cuts the deck of cards"""
        num_cards = len(self.deck.cards)
        while num_cards < 81:
            self.deck = Deck()
            num_cards = len(self.deck.cards)
        cut_index = random.randint(60, 80)
        self.cut_card = self.deck.cards[cut_index]
        self.cut_card = self.deck.cards[cut_index]
        self.deck.cards = (
            self.deck.cards[cut_index:] + self.deck.cards[:cut_index]
        )

    def deal_cards(self):
        """Deals initial cards to all players and the dealer"""
        for i in range(2):
            for name, player in self.players.items():
                card = self.deck.draw_card()
                player.hand.append(card)
                print(f"{name} was dealt {card}")
            card = self.deck.draw_card()
            self.dealer_hand.append(card)
            if i == 0:
                print(f"Dealer was dealt {card}")
            else:
                print("Dealer was dealt a face-down card")

    def deal_dealer_hand(self):
        """Deals the dealer's second card and reveals the first card"""
        self.dealer_hand[1] = self.deck.draw_card()
        print(f"Dealer's face-down card was {self.dealer_hand[0]}")
        print(f"Dealer's face-up card is {self.dealer_hand[1]}")

    def calculate_score(self, hand):
        """Calculates the score of a hand of cards"""
        ace_count = sum([1 for card in hand if card.rank == "Ace"])
        score = sum([self.card_value(card.rank) for card in hand])
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    def card_value(self, rank):
        """Returns the numerical value of a card rank"""
        if rank in ["Jack", "Queen", "King"]:
            return 10
        if rank == "Ace":
            return 11
        return int(rank)

    def check_for_game_over(self):
        """
        Check if the game is over and determine the winner(s) of the game.

        Returns:
        None
        """
        for name, player in self.players.items():
            player_score = self.calculate_score(player.hand)
            if player_score > 21:
                print(f"{name} busts with {player_score}.")
            elif player_score == 21:
                print(f"{name} has blackjack!")
            else:
                while not player.finished:
                    response = player.ask_for_hit()
                    if response.lower() == "y":
                        card = self.deck.draw_card()
                        player.hand.append(card)
                        print(f"{name} was dealt {card}")
                        player_score = self.calculate_score(player.hand)
                        if player_score > 21:
                            print(f"{name} busts with {player_score}.")
                            player.finished = True
                        elif player_score == 21:
                            print(f"{name} has blackjack!")
                            player.finished = True
                    elif response.lower() == "n":
                        print(f"{name} stays with {player_score}.")
                        player.finished = True
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

        dealer_score = self.calculate_score(self.dealer_hand)
        while dealer_score < 17:
            card = self.deck.draw_card()
            self.dealer_hand.append(card)
            dealer_score = self.calculate_score(self.dealer_hand)
            print(f"Dealer hits and is dealt {card}.")
            if dealer_score > 21:
                print("Dealer busts!")
                break

        print(f"Dealer stays with {dealer_score}.")

        for name, player in self.players.items():
            player_score = self.calculate_score(player.hand)
            if player_score > 21:
                print(f"{name} loses ${player.bet}.")
            elif dealer_score > 21 or player_score > dealer_score:
                print(f"{name} wins ${player.bet}.")
            elif player_score == dealer_score:
                print(f"{name} pushes.")
            else:
                print(f"{name} loses ${player.bet}.")
                self.game_over = True

    def play_game(self):
        """Play one game of Blackjack, from shuffling the
        deck to determining the winner of the game."""
        for player in self.players.values():
            player.hand = []
            player.finished = False
        self.dealer_hand = []
        self.shuffle_deck()
        self.cut_deck()
        self.deal_cards()
        self.deal_dealer_hand()
        self.check_for_game_over()

    def run(self):
        """
        Run a series of Blackjack games until the player decides to stop.

        Returns:
        None
        """
        while not self.game_over:
            self.play_game()

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "n":
            self.game_over = True
