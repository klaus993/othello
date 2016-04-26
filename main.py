from time import sleep


# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 8
PLAYERS = 0, 1
PLAYER_0 = '\033[01mB\033[0m'           # White bold 'B'
PLAYER_1 = '\033[01m\033[90mN\033[0m'   # Dark grey bold 'N'
PLAYER_CHIPS = (PLAYER_0, PLAYER_1)
INPUT_PROMPT = 'ingrese una ficha (columna fila): '
PLAYER_COLORS = ('blanco', 'negro')
MAX_TURNS = 61
augmenters = (1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)


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


def ask_input(player):
    """ Asks the user the position to enter a chip (col,row)
    and returns the chip location as a string (i.e. A 5)
    """
    chip_location = input('Color ' + PLAYER_COLORS[player] + ': ' + INPUT_PROMPT)
    return chip_location


def get_row_col(chip_location):
    """Gets chip location as a parameter
    Returns raw row and col
    """
    return chip_location.split()[1], chip_location.split()[0].upper()


def get_row_col_literals(chip_location):
    """Gets chip location as a parameter.
    Returns literal row and col position as a tuple
    """
    row = int(get_row_col(chip_location)[0]) - 1
    col = ord(get_row_col(chip_location)[1]) - 65
    return row, col


def is_valid_location(chip_location):
    """Gets chip location as a parameter.
    Checks whether the chip location is on the board,
    and if the syntax is correct (row column)
    """
    return not(len(chip_location) < 3 or not chip_location or not chip_location[0].isalpha() or not chip_location[1].isspace() or chip_location.isspace() or not chip_location[2:].isdigit())


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
            if not board[i][j]:
                for row_add, col_add in augmenters:
                    moves.append(is_valid_direction(i, j, row_add, col_add, board, player))
    return True in moves


def declare_winner(board):
    """Given a board, checks the winner of the game by counting
    the chips of both players. Prints a message and the correspondings points
    """
    results = count_chips(board, 0), count_chips(board, 1)
    winner = '¡El color {} ha ganado la partida!'
    for i in range(2):
        if results[i] > results[i - 1]:
            print(winner.format(PLAYER_COLORS[i]) + '\n')
    if results[0] == results[1]:
        print('¡Empate!\n')
    print('Puntajes:')
    for i in range(2):
        print('{}: {} punto(s)'.format(PLAYER_COLORS[i].title(), results[i]))


def play(board):
    """Playing cycle, plays until both players have no moves left or
    until 60 turns are played. Returns the final board.
    """
    playing = True
    turn_count = 1     # Turn counter, used for 60 turns limit.
    while playing:
        print('Turno ' + str(turn_count))
        for i in range(2):
            print_board(board)
            if check_all_moves(board, PLAYERS[i]):
                while not enter_chip(board, i):  # Enters the cycle only if there is an input error.
                    print('Sintaxis incorrecta o movimiento inválido. Vuelva a ingresar la ficha.')
            else:
                if not check_all_moves(board, PLAYERS[i - 1]):
                    print('Ningun color tiene jugadas posibles.')
                    playing = False
                    break
                sleep(1)
                print('Color ' + PLAYER_COLORS[i] + ': no tienes jugadas posibles')
        turn_count += 1              # breaks and the game ends.
        if turn_count == MAX_TURNS:
            playing = False
    return board


def main():
    """Main flux of the game.
    """
    print('¡Bienvenido al Reversi!')
    sleep(1)
    board = create_and_initialize_board()
    if check_boardsize():
        board = play(board)
        declare_winner(board)
    else:
        print('El tamaño del tablero debe ser par')


main()
