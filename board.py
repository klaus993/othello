from constants import *


def check_boardsize():
    """Checks if the board size is even or odd
    Returns True if even, False if odd.
    """
    return BOARD_SIZE % 2 == 0


def create_board():
    """ Returns an empty board, a list
    """
    empty_list = ['']
    board = []
    for i in range(BOARD_SIZE):
        board.append(empty_list * BOARD_SIZE)
    return board


def create_and_initialize_board():
    """ Creates an empty board and initializes it,
    takes the empty board and adds starting chips in the center
    """
    board = create_board()
    center_index_1 = BOARD_SIZE // 2
    center_index_2 = center_index_1 - 1
    board[center_index_2][center_index_2] = PLAYER_CHIPS[0]
    board[center_index_2][center_index_1] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_2] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_1] = PLAYER_CHIPS[0]
    return board


def print_col_letters():
    """ Prints the column identification letters
    (A,B,C,..) in the upper side of the board
    """
    print(' ' * 4, end='')    # Spaces printed for column letter fitting
    for i in range(len(create_and_initialize_board())):
        print(chr(i + 65), end=' ')  # Adds 65 to match ASCII uppercase code
    print()                        # Ends with a new line for board print


def print_board(board):
    """Prints the board, given by parameter (a list)
    separated by pipes "|"
    """
    print_col_letters()
    for index, row in enumerate(board):
        if (index + 1) < 10:                      # Validates if row number is 10
            print(' ' + str(index + 1), end=' ')    # or more for space fitting
        else:
            print(index + 1, end=' ')
        for col in row:
            if col == '':
                print('|' + ' ', end='')
            else:
                print('|' + col, end='')
        print('|')