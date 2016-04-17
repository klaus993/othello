# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 8
PLAYER_0 = '\033[01mB\033[0m'           # White bold 'B'
PLAYER_1 = '\033[01m\033[90mN\033[0m'   # Dark grey bold 'N'
PLAYER_CHIPS = (PLAYER_0, PLAYER_1)
INPUT_PROMPT = 'ingrese una ficha (columna fila): '
PLAYER_COLORS = ('blanco', 'negro')


def check_boardsize():
    """ Checks if the board size is even or odd
    Returns True if even, False if odd¿ m¿  .
    """
    return BOARD_SIZE % 2 == 0


def create_board():
    """ Returns an empty board, returns a list

    """
    empty_list = ['']
    board = []
    for i in range(BOARD_SIZE):
        board.append(empty_list*BOARD_SIZE)
    return board


def create_and_initialize_board():
    """ Creates an empty board and initializes it:
    takes the empty board and adds starting chips in the center
    """
    board = create_board()
    center_index_1 = BOARD_SIZE//2
    center_index_2 = center_index_1 - 1
    board[center_index_2][center_index_2] = PLAYER_CHIPS[0]
    board[center_index_2][center_index_1] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_2] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_1] = PLAYER_CHIPS[0]
    board[5][3] = PLAYER_CHIPS[1]
    return board


def print_col_letters():
    """ Prints the col identificatory letters
    (A,B,C,..) in the upper side of the board
    """
    print(' '*4, end='')    # Spaces printed for col letter fitting
    for i in range(len(create_and_initialize_board())):
        print(chr(i+65), end=' ')  # Adds 65 to match ascii uppercase code
    print()


def print_board(board):
    """Prints the board, given by parameter (a list)

    """
    print_col_letters()
    for index, row in enumerate(board):
        if (index+1) < 10:                     # Validates if row number is 10
            print(' '+str(index + 1), end=' ') # or more for space fitting
        else:
            print(index+1, end=' ')
        for col in row:
            if col == '':
                print('|'+' ', end='')
            else:
                print('|'+col, end='')
        print('|')


def ask_input(player):
    """ Asks the user the position to enter a chip (col,row)
    and returns the chip location as a string
    """
    chip_location = input('Color '+PLAYER_COLORS[player]+': '+INPUT_PROMPT)
    return chip_location


def return_col(chip_location):
    """ Given a string chip_location, returns
    the col location (string, a letter) in uppercase
    """
    return chip_location.split()[0].upper()
    # return chip_location[0].upper()


def return_row(chip_location):
    """ Given a string chip_location, returns
    the row location (string, a number)
    """
    return chip_location.split()[1]


def enter_chip(board, player):
    """ Enters a black chip in the board given a board (list)
    and a player (0 or 1) and returns the resulting board (list)
    """
    chip_location = ask_input(player)
    col = return_col(chip_location)
    row = int(return_row(chip_location))
    col_ascii = ord(col)
    literal_col = col_ascii-65
    literal_row = row-1
    moves = []
    # for i, j in (1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1):
    #     moves.append(is_valid_direction(literal_row, literal_col, i, j, board, player))

    if is_valid_direction(literal_row, literal_col, 1, -1, board, player)[0]:
        board[literal_row][literal_col] = PLAYER_CHIPS[player]
        return board
    else:
        return 1


def is_valid_direction(old_row, old_col, row_add, col_add, board, player):
    """ Returns True if the move is valid in a given direction.
    Direction is given by row_add and col_add incrementers.
    """
    if player == 1:
        other_player = 0
    else:
        other_player = 1
    current_row = old_row + row_add
    current_col = old_col + col_add
    if (current_row >= BOARD_SIZE or current_col >= BOARD_SIZE or
        (board[current_row][current_col] == PLAYER_CHIPS[player] and
            board[old_row][old_col] == PLAYER_CHIPS[player]) or
        (board[old_row][old_col] == PLAYER_CHIPS[player] or
            (not board[current_row][current_col]) or
            (not board[old_row][old_col] and
                board[current_row][current_col] == PLAYER_CHIPS[player]))):
        return False
    if (board[old_row][old_col] != PLAYER_CHIPS[player] and
            board[current_row][current_col] == PLAYER_CHIPS[player]):
        return True, old_row, old_col
    else:
        return '1'
    is_valid_move(current_row, current_col, row_add, col_add, board, player)


def main():
    turn_count = 1
    play_count = 1
    playing = True
    board = create_and_initialize_board()
    if check_boardsize():
        while playing:
            print('Turn '+str(turn_count))
            for i in range(2):
                print('Play '+str(play_count))
                print_board(board)
                board = enter_chip(board, i)
                print_board(board)
                play_count += 1
            turn_count += 1
            if turn_count == 60:
                playing = False
    else:
        print('El tamaño del tablero debe ser par')
        return

main()
