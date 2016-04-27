from position_getters import *
from constants import *


def enter_chip(board, player):
    """ Enters a chip in the board given a board (list)
    and a player (0 or 1), turns the chips that must be turned
    given the game rules and returns the resulting board (list).
    Also checks syntax for user chip input and move validity.
    If it's invalid returns False
    """
    chip_location = ask_input(player)
    if not is_valid_location(chip_location):
        return False
    literal_row, literal_col = get_row_col_literals(chip_location)  # Column and row numbers corresponding to list index.
    if literal_row not in range(BOARD_SIZE) or literal_col not in range(BOARD_SIZE) or board[literal_row][literal_col]:
        return False
    flag = False
    for i, j in augmenters:
        if is_valid_direction(literal_row, literal_col, i, j, board, player):
            board = chip_turn(literal_row, literal_col, i, j, board, player)
            flag = True
    if flag:
        board[literal_row][literal_col] = PLAYER_CHIPS[player]
        return board
    else:
        return False


def check_all_moves(board, player):
    """Given a board, checks all the remaining empty slots and returns True
    if a conversion in *any* direction is valid
    """
    moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if not board[i][j]:
                for row_add, col_add in augmenters:
                    moves.append(is_valid_direction(i, j, row_add, col_add, board, player))
    return True in moves


def is_valid_direction(old_row, old_col, row_add, col_add, board, player):
    """ Returns True if the move is valid in a given direction.
    Direction is given by row_add and col_add augmenters.
    """
    current_row = old_row + row_add
    current_col = old_col + col_add
    if (current_row in range(BOARD_SIZE) and current_col in range(BOARD_SIZE) and board[current_row][current_col]):
        if (board[old_row][old_col] == PLAYER_CHIPS[player - 1] and
                board[current_row][current_col] == PLAYER_CHIPS[player]):
            return True
        if (board[current_row][current_col] == PLAYER_CHIPS[player - 1]):
            return is_valid_direction(current_row, current_col, row_add, col_add, board, player)
    return False


def chip_turn(row, col, row_add, col_add, board, player):
    """Pre: given direction must be a valid move.
    Turns all the chips between the desired location
    and the next current player chip.
    """
    row += row_add
    col += col_add
    if (board[row][col] == PLAYER_CHIPS[player - 1]):
        board[row][col] = PLAYER_CHIPS[player]
    else:
        return board
    return chip_turn(row, col, row_add, col_add, board, player)


def ask_input(player):
    """ Asks the user the position to enter a chip (col,row)
    and returns the chip location as a string (i.e. A 5)
    """
    chip_location = input('Color ' + PLAYER_COLORS[player] + ': ' + INPUT_PROMPT)
    return chip_location


def is_valid_location(chip_location):
    """Gets chip location as a parameter.
    Checks whether the chip location is on the board,
    and if the syntax is correct (row column)
    """
    return not len(chip_location) < 3 and chip_location and chip_location[0].isalpha() and chip_location[1].isspace() and not chip_location.isspace() and chip_location[2:].isdigit()
