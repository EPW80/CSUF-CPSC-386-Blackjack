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

"""program that shows how to use Python's pickle module."""

import os
import os.path
import pickle
from blackjackgame.player import Player


def main():
    """Load or create player data and save it to a file."""

    main_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(main_dir, "data")
    pickle_file = os.path.join(data_dir, "players.pkl")

    # create some player data
    players = [
        Player(name="Erik", player_id=1),
        Player(name="Kylie", player_id=2),
        Player(name="Angie", player_id=3),
        Player(name="Mom", player_id=4),
    ]

    # save the player data to the pickle file
    with open(pickle_file, "wb") as file_handle:
        pickle.dump(players, file_handle, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
