# Blackjack

## Rules

- There is at least one players playing the game and at most four.
- To start the game, a player can enter the number 1 through 4 to establish how many players there are.
- All players start with $10,000.00 in their bank balance.
- The dealer is always a computer AI and has unlimited funds.
- The game is turn based.
- All players have a name, including the _computer AI_. Players' names may be used as unique identifiers or additional information can be gathered.
- Unique identifiers are used to serialize the game state to a file so that a player can have their bank balance upon return to the game.
- The game is played with 8 decks of cards. The cards are typical cards with the ranks Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King and the suits Clubs, Hearts, Spades, Diamonds. There are no jokers.
- The value of the cards is the rank of the card except for Ace, Jack, Queen, and King. An Ace's value is either 1 or 11 depending on what is most advantageous to the hand in question. Jacks, Queens, and Kings have a value of 10.
- Before playing, the cards must be shuffled and cut.
- A cut card is placed randomly between the 60th and 80th card from the bottom of the deck.
- The players play in the order their names are entered when the program starts. The dealer always goes last.
- Once each player has had a turn in ascending order, the turn returns to the first player. (The process is a circular queue.)
- The game is made up of many games. The players continue playing games of blackjack. At the end of every game, the game prompts the first player if they would like to play again. An answer of _yes_ means the dealer will deal cards out to the same players who played previously. With multiple players, should one choose to leave then the first player must answer _no_ to end the game and exit the program.
- At the start of every game, before cards are dealt, each player must place a wager. A wager can be at least $1 and at most their bank balance.
- A player may not wager more money than she has in her bank balance.
- The cards are dealt one by one, starting with the first player and ending on the dealer.
- The dealer's second card is kept hidden from the players; all other cards are dealt face up.
- At the beginning of every turn, the game displays what cards the current player is holding and what face up card the dealer has showing.
- Whenever a card is dealt, it is printed or shown to the players before taking any other action.
- When it is the dealer's turn, the dealer must turn over (print or show) the face down card before taking any other action.
- All bets pay out 2 to 1.
- When a players turn begins, they have the option to _double down_.
- A player may not _surrender_, _split_, or buy _insurance_.
- The player may _double down_ when her turn starts and never later.
- The player may _double down_ if and only if there is sufficient funds in her balance to double her wager.
- A player is prompted to _hit_ or _stand_ unless they are _busted_ or have _21_. If they have _busted_ or have _21_ then a message is shown stating that they have _busted_ or reached _21_.
- The dealer must _hit_ on a hand that is less than 17. The dealer must _stand_ on a hand that is 17 or greater.
- The dealer only _hits_ if there are players who are not _busted_.
- No one wins or loses when there is a _push_.
- A dealer does not place bets which means the dealer does not _double down_.

## Install

To run the game, the command must be `./blackjack.py`. This means that the file `blackjack.py` must have a shebang and call the main game loop. This file contains only a call to the game's main loop which is defined in the `blackjackgame` package.

- `__init__.py`
- `cards.py`
- `game.py`
- `player.py`
