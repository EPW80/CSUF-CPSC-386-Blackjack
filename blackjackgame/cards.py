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

from collections import namedtuple
from random import shuffle, randrange
from math import ceil

Card = namedtuple("Card", ["rank", "suit"])


def str_card(card):
    """Returns a string representation of the card"""
    return f"{card.rank} of {card.suit}"


Card.__str__ = str_card


def is_ace(card):
    """Checks if the card is an Ace"""
    return card.rank == "Ace"


Card.is_ace = is_ace


def is_ten(card):
    """Checks if the card has a rank of 10, Jack, Queen, or King"""
    return card.rank in "10 Jack Queen King".split()


Card.is_ten = is_ten


class Deck:
    """A deck of cards"""

    ranks = ["Ace"] + [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King"]
    suits = "♣️ ♥️ ♠️ ♦️".split()
    values = list(range(1, 11)) + [10, 10, 10]
    value_dict = dict(zip(ranks, values))

    def __init__(self):
        self.cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]
        self.cursor = 0

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(self.cards):
            pos = self.cursor
            self.cursor += 1
            return self.cards[pos]
        self.cursor = 0
        raise StopIteration

    def shuffle(self, num_shuffles=1):
        """Shuffles the deck"""
        for _ in range(num_shuffles):
            shuffle(self.cards)

    def cut(self):
        """Cuts the deck"""
        extra = ceil(len(self.cards) * 0.2)
        half = (len(self.cards) // 2) + randrange(-extra, extra)
        top_half = self.cards[:half]
        bottom_half = self.cards[half:]
        self.cards = bottom_half + top_half

    def deal(self, num_cards=1):
        """Deals a specified number of cards"""
        return [self.cards.pop() for _ in range(num_cards)]

    def draw_card(self):
        """Draws a card from the top of the deck"""
        if len(self.cards) == 0:
            raise Exception("No cards left in the deck")
        return self.cards.pop(0)

    def merge(self, other_deck):
        """Merges this deck with another deck"""
        self.cards += other_deck.cards

    def __str__(self):
        """Returns a string representation of the deck"""
        return ", ".join(map(str, self.cards))


def card_value(card):
    """Returns the value of a card"""
    return Deck.value_dict[card.rank]


Card.value = card_value
Card.__int__ = card_value
