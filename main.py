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
    print()


def print_board(board):
    """Prints the board, given by parameter (a list)
    separated by pipes "|"
    """
    print_col_letters()
    for index, row in enumerate(board):
        if (index+1) < 10:                      # Validates if row number is 10
            print(' '+str(index+1), end=' ')  # or more for space fitting
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
    string_col = chip_location[0]
    string_space = chip_location[1]
    string_row = chip_location[2]
    if not chip_location or string_col not in ascii_letters or string_row != ' ' or not string_row.isdigit():
        return False
    col = return_col(chip_location)
    row = int(return_row(chip_location))
    col_ascii = ord(col)
    literal_col = col_ascii-65
    literal_row = row-1
    if (not True in valid_directions(literal_row, literal_col, board, player)):
        return False
    flag = False
    for i in range(8):
        if valid_directions(literal_row, literal_col, board, player)[i]:
            board = chip_turn(literal_row, literal_col, incrementers[i][0], incrementers[i][1], board, player)
            flag = True
    if flag:
        board[literal_row][literal_col] = PLAYER_CHIPS[player]
    return board


def is_valid_direction(old_row, old_col, row_add, col_add, board, player):
    """ Returns True if the move is valid in a given direction.
    Direction is given by row_add and col_add augmenters.
    """
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
        return True
    return is_valid_direction(current_row, current_col, row_add, col_add, board, player)


def valid_directions(row, col, board, player):
    """
    """
    moves = []
    for i, j in incrementers:
        moves.append(is_valid_direction(row, col, i, j, board, player))
    return moves


def chip_turn(row, col, row_add, col_add, board, player):
    """
    """
    row += row_add
    col += col_add
    if (board[row][col] != PLAYER_CHIPS[player]):
        board[row][col] = PLAYER_CHIPS[player]
    else:
        return board
    return chip_turn(row, col, row_add, col_add, board, player)


def count_chips(board, player):
    cont = 0
    for row in board:
        for col in row:
            if col == PLAYER_CHIPS[player]:
                cont += 1
    return cont


def check_all_moves(board, player):
    moves = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            for k,l in incrementers:
                if not board[i][j]:
                    moves.append(is_valid_direction(i, j, k, l, board, player))
    return True in moves


def winner(board):
    """
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
    """Main function.
    """
    print('¡Bienvenido al Reversi!')
    sleep(1)
    turn_count = 1
    playing = True
    board = create_and_initialize_board()
    if check_boardsize():
        while playing:
            print('Turn '+str(turn_count))
            for i in range(2):
                print_board(board)
                if check_all_moves(board, i):
                    while not enter_chip(board, i):
                        print('Sintaxis incorrecta o movimiento inválido. Vuelva a ingresar la ficha.')
                else:
                    print('Color '+PLAYER_COLORS[i]+': no tienes jugadas posibles')
                    sleep(1)
                    break
            turn_count += 1
            if turn_count == 4:
                playing = False
        winner(board)
    else:
        print('El tamaño del tablero debe ser par')

main()
