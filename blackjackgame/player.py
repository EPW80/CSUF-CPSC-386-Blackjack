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

"""
Module player.py represents a player in a game of blackjack.
"""

from locale import currency


class Player:
    """
    A class representing a player.
    """

    def __init__(self, name, player_id):
        """
        Initialize the Player object.

        Args:
            name (str): The name of the player.
            player_id (int): The ID of the player.
        """
        self._name = name
        self.player_id = player_id
        self.hand = []
        self.bet = 0
        self.finished = False

    def prompt_for_bet(self):
        """
        Prompts the player for their bet.
        """
        while True:
            bet = input(f"{self.name}, enter your bet: ")
            try:
                self.bet = int(bet)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if self.bet > 0:
                break

            print("Invalid input. Please enter a positive number.")

    def ask_for_hit(self):
        """
        Prompts the player if they want to hit.

        Returns:
            str: The player's response ('y' or 'n').
        """
        while True:
            response = input(f"{self.name}, do you want to hit? (y/n): ")
            if response.lower() in ["y", "n"]:
                return response.lower()

            print("Invalid input. Please enter 'y' or 'n'.")

    @property
    def pid(self):
        """
        Returns the player ID.
        """
        return self.player_id

    @property
    def name(self):
        """
        Returns the player name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the player name.
        """
        self._name = value

    def is_ai(self):
        """
        Checks if the player is an AI.

        Returns:
            bool: True if the player is an AI, False otherwise.
        """
        return False

    def __str__(self):
        """
        Returns the string representation of the player.
        """
        return self._name

    def __repr__(self):
        """
        Returns the official string representation of the player.
        """
        return f"Player({self.player_id}, '{self._name}')"


class BlackJackPlayer(Player):
    """
    A class representing a blackjack player.
    """

    def __init__(self, player_id, name, bankroll=10000):
        """Initialize the BlackJackPlayer object"""
        super().__init__(name, player_id)
        self._balance = bankroll
        self._bet = 0

    @property
    def bankroll(self):
        """
        Returns the bankroll of the player.
        """
        return currency(self._balance, grouping=True)

    @property
    def bet(self):
        """
        Returns the bet of the player.
        """
        return currency(self._bet, grouping=True)

    @bet.setter
    def bet(self, wager):
        """
        Sets the bet of the player.
        """
        self._bet = wager

    def deduct_bet(self):
        """
        Deducts the bet from the player's bankroll.
        """
        self._balance -= self._bet

    def __repr__(self):
        return (
            f"BlackJackPlayer({self.player_id}, '{self._name}', "
            f"bankroll={self._balance})"
        )
