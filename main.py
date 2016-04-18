from time import sleep
from string import ascii_letters


# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 8
PLAYER_0 = '\033[01mB\033[0m'           # White bold 'B'
PLAYER_1 = '\033[01m\033[90mN\033[0m'   # Dark grey bold 'N'
PLAYER_CHIPS = (PLAYER_0, PLAYER_1)
INPUT_PROMPT = 'ingrese una ficha (columna fila): '
PLAYER_COLORS = ('blanco', 'negro')
incrementers = (1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)


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
        board.append(empty_list*BOARD_SIZE)
    return board


def create_and_initialize_board():
    """ Creates an empty board and initializes it,
    takes the empty board and adds starting chips in the center
    """
    board = create_board()
    center_index_1 = BOARD_SIZE//2
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
    print(' '*4, end='')    # Spaces printed for column letter fitting
    for i in range(len(create_and_initialize_board())):
        print(chr(i+65), end=' ')  # Adds 65 to match ASCII uppercase code
    print()                        # Ends with a new line for board print


def print_board(board):
    """Prints the board, given by parameter (a list)
    separated by pipes "|"
    """
    print_col_letters()
    for index, row in enumerate(board):
        if (index+1) < 10:                      # Validates if row number is 10
            print(' '+str(index+1), end=' ')    # or more for space fitting
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
    and returns the chip location as a string (i.e. A 5)
    """
    chip_location = input('Color '+PLAYER_COLORS[player]+': '+INPUT_PROMPT)
    return chip_location


def return_col(chip_location):
    """ Given a string chip_location, splits the string into
    a list and returns the column location (string, a letter) uppercase.
    """
    return chip_location.split()[0].upper()


def return_row(chip_location):
    """ Given a string chip_location, splits the string into
    a list and returns the row location (string, a number).
    """
    return chip_location.split()[1]


def enter_chip(board, player):
    """ Enters a chip in the board given a board (list)
    and a player (0 or 1), turns the chips that must be turned
    given the game rules and returns the resulting board (list).
    Also checks syntax for user chip input and move validity.
    """
    chip_location = ask_input(player)
    if not chip_location or chip_location[0] not in ascii_letters or chip_location[1] != ' ' or not chip_location[2].isdigit():
    # Covers every other input than the correct syntax (column row)
        return False
    col = return_col(chip_location)
    row = int(return_row(chip_location))
    col_ascii = ord(col)
    literal_col = col_ascii-65     # Column number corresponding to list index.
    literal_row = row-1            # Row number corresponding to list index.
    flag = False
    for i in range(8):
        if valid_directions(literal_row, literal_col, board, player)[i]:
            # Checks directions in which to convert enemy chips
            board = chip_turn(literal_row, literal_col, incrementers[i][0], incrementers[i][1], board, player)
            flag = True
    if flag:
        board[literal_row][literal_col] = PLAYER_CHIPS[player]
        return board
    else:
        return False


def is_valid_direction(old_row, old_col, row_add, col_add, board, player):
    """ Returns True if the move is valid in a given direction.
    Direction is given by row_add and col_add augmenters.
    """
    current_row = old_row + row_add
    current_col = old_col + col_add
    if (current_row >= BOARD_SIZE or current_col >= BOARD_SIZE or      # Checks all the posibilities
        (board[current_row][current_col] == PLAYER_CHIPS[player] and   # which result in an invalid conversion
            board[old_row][old_col] == PLAYER_CHIPS[player]) or
        (board[old_row][old_col] == PLAYER_CHIPS[player] or
            (not board[current_row][current_col]) or
            (not board[old_row][old_col] and
                board[current_row][current_col] == PLAYER_CHIPS[player]))):
        return False
    if (board[old_row][old_col] != PLAYER_CHIPS[player] and            # Checks whether previous chip is 
            board[current_row][current_col] == PLAYER_CHIPS[player]):  # from the enemy player, and current 
        return True                                                    # if is of the current player
    return is_valid_direction(current_row, current_col, row_add, col_add, board, player)


def valid_directions(row, col, board, player):
    """Checks validity of move in all directions and 
    appends the boolean value to a list. Returns a list with
    8 boolean values (corresponding to the 8 senses).
    """
    moves = []
    for i, j in incrementers:
        moves.append(is_valid_direction(row, col, i, j, board, player))
    return moves


def chip_turn(row, col, row_add, col_add, board, player):
    """Pre: given direction must be a valid move.
    Turns all the chips between the desired location
    and the next current player chip.
    """
    row += row_add
    col += col_add
    if (board[row][col] != PLAYER_CHIPS[player]):
        board[row][col] = PLAYER_CHIPS[player]
    else:
        return board
    return chip_turn(row, col, row_add, col_add, board, player)


def count_chips(board, player):
    """Given a board, counts the chips of a given player
    """
    cont = 0
    for row in board:
        for col in row:
            if col == PLAYER_CHIPS[player]:
                cont += 1
    return cont


def check_all_moves(board, player):
    """Given a board, checks all the remaining empty slots and returns True
    if a conversion in *any* direction is valid
    """
    moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            for k,l in incrementers:
                if not board[i][j]:
                    moves.append(is_valid_direction(i, j, k, l, board, player))
    return True in moves


def declare_winner(board):
    """Given a board, checks the winner of the game by counting
    the chips of both players. Prints a message and the correspondings points
    """
    player_0_points = count_chips(board, 0)
    player_1_points = count_chips(board, 1)
    if player_0_points > player_1_points:
        print('¡El color '+PLAYER_COLORS[0]+' ha ganado la partida!')
    elif player_0_points == player_1_points:
        print('¡Empate!\n')
    else:
        print('¡El color '+PLAYER_COLORS[1]+' ha ganado la partida!')
    print('Puntajes:')
    print(PLAYER_COLORS[0].title()+': '+str(player_0_points)+' punto(s)')
    print(PLAYER_COLORS[1].title()+': '+str(player_1_points)+' punto(s)')


def main():
    """Main function. Main flow of the game.
    """
    print('¡Bienvenido al Reversi!')
    sleep(1)
    turn_count = 1         # Turn counter, used for 60 turns limit.
    no_plays_count = 0     # Used in case there is no more possible moves for 
    playing = True         # any player, if it reaches 2, breaks the cycle and ends the game.
    board = create_and_initialize_board()
    if check_boardsize():
        while playing:
            print('Turn '+str(turn_count))
            for i in range(2):
                print_board(board)
                if check_all_moves(board, i):
                    while not enter_chip(board, i):  # Enters the cycle only if there is an input error.
                        print('Sintaxis incorrecta o movimiento inválido. Vuelva a ingresar la ficha.')
                    if no_plays_count != 0:         # Resets counter in case there was
                        no_plays_count = 0          # only one play with no possible moves.
                else:
                    print('Color '+PLAYER_COLORS[i]+': no tienes jugadas posibles')
                    no_plays_count += 1
                    sleep(1)
            if no_plays_count == 2:      # If it reaches 2 it means that two consecutive
                break                    # plays were not possible, in that case the cycle
            turn_count += 1              # breaks and the game ends.
            if turn_count == 61:
                playing = False
        declare_winner(board)
    else:
        print('El tamaño del tablero debe ser par')

main()
