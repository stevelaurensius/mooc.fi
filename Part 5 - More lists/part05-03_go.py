# In a game of Go two players take turns to place black and white stones on a game board.
# The winner is the player who manages to encircle a bigger area on the board with their
# own game pieces.

# Please write a function named who_won(game_board: list), which takes a two-
# dimensional array as its argument. The array consists of integer values, which represent
# the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare
# the number of pieces each player has on the game board. Also, the size of the game
# board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If
# both players have the same number of pieces on the board, the function should return
# the value 0.


def who_won(game_board: list):
    player_one = 0
    player_two = 0
    for string in game_board:
        for substring in string:
            if substring == 1:
                player_one += 1
            elif substring == 2:
                player_two += 1
            else:
                pass
    if player_one > player_two:
        return 1
    elif player_two > player_one:
        return 2
    else:
        return 0
