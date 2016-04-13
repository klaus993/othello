# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 14
PLAYER_0 = '\033[01mB\033[0m'           # White bold 'B'
PLAYER_1 = '\033[01m\033[90mN\033[0m'   # Dark grey bold 'N'
PLAYER_CHIPS = (PLAYER_0, PLAYER_1)
INPUT_PROMPT = 'ingrese una ficha (columna fila): '
PLAYER_COLORS = ('blanco', 'negro')


def check_boardsize():
    ''' Checks if the board size is even or odd
    Returns True if even, False if odd.
    '''
    return BOARD_SIZE % 2 == 0


def create_board():
    ''' Returns an empty board, returns a list
    '''
    empty_list = ['']
    board = []
    for i in range(BOARD_SIZE):
        board.append(empty_list*BOARD_SIZE)
    return board


def create_and_initialize_board():
    ''' Creates an empty board and initializes it:
    takes the empty board and adds starting chips in the center
    '''
    board = create_board()
    center_index_1 = BOARD_SIZE//2
    center_index_2 = center_index_1 - 1
    board[center_index_2][center_index_2] = PLAYER_CHIPS[0]
    board[center_index_2][center_index_1] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_2] = PLAYER_CHIPS[1]
    board[center_index_1][center_index_1] = PLAYER_CHIPS[0]
    return board


def print_column_letters():
    ''' Prints the column identificatory letters
    (A,B,C,..) in the upper side of the board
    '''
    print(' '*4, end='')    # Spaces printed for column letter fitting
    for i in range(len(create_and_initialize_board())):
        print(chr(i+65), end=' ')  # Adds 65 to match ascii uppercase code
    print()


def print_board(board):
    '''Prints the board, given by parameter (a list)
    '''
    print_column_letters()
    for index, row in enumerate(board):
        if (index+1) < 10:                     # Validates if row number is 10 
            print(' '+str(index + 1), end=' ') # or more for space fitting
        else:
            print(index+1, end=' ')
        for column in row:
            if column == '':
                print('|'+' ', end='')
            else:
                print('|'+column, end='')
        print('|')


def ask_input(player):
    ''' Asks the user the position to enter a chip (column,row)
    and returns the chip location as a string
    '''
    chip_location = input('Color '+PLAYER_COLORS[player]+': '+INPUT_PROMPT)
    return chip_location


def return_column(chip_location):
    ''' Given a string chip_location, returns
    the column location (string, a letter) in uppercase
    '''
    return chip_location.split()[0].upper()
    # return chip_location[0].upper()


def return_row(chip_location):
    ''' Given a string chip_location, returns
    the row location (string, a number)
    '''
    return chip_location.split()[1]


def enter_chip(board, player):
    ''' Enters a black chip in the board given a board (list)
    and a player (0 or 1) and returns the resulting board (list)
    '''
    chip_location = ask_input(player)
    column = return_column(chip_location)
    row = int(return_row(chip_location))
    column_ascii = ord(column)
    board[row - 1][column_ascii - 65] = PLAYER_CHIPS[player]
    return board


def is_valid_move(row, column, row_add, column_add, board, player):
    # if not board[row][column]:
    #     return False
    if player == 1:
        other_player = 0
    else:
        other_player = 1
    row += row_add
    column += column_add
    if (row >= BOARD_SIZE or column >= BOARD_SIZE or
        (board[row-row_add][column-column_add] != PLAYER_CHIPS[player] and
            board[row][column] != PLAYER_CHIPS[player]) or
        (board[row-row_add][column-column_add] != PLAYER_CHIPS[other_player]) and
            board[row][column] != PLAYER_CHIPS[other_player]):
        return False
    else:
        return False
    # if (board[row][column] == PLAYER_CHIPS[player]):
    #     return True
    is_valid_move(row, column, row_add, column_add, board, player)


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

# board = create_and_initialize_board()
# print(is_valid_move(0,1,0,1,board,1))
# print_board(board)

# print(return_row('B 03'))
