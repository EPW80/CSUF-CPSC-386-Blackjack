#!/usr/bin/env python3
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

"""Simple blackjack game."""


from blackjackgame.game import BlackjackGame

if __name__ == "__main__":
    BlackjackGame(number_of_players=4).run()
