# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 8
PLAYER_1 = '\033[01mB\033[0m'
PLAYER_2 = '\033[01m\033[90mN\033[0m'
PLAYER_CHIPS = (PLAYER_1,PLAYER_2)
INPUT_PROMPT = 'Ingrese una ficha (columna,fila): '
PLAYER_1_PROMPT = 'Color blanco: '
PLAYER_2_PROMPT = 'Color negro: '
PROMPTS = (PLAYER_1_PROMPT,PLAYER_2_PROMPT)

def check_boardsize():
    ''' Checks if the board size is even or odd
    Returns True if even, False if odd.
    '''
    return BOARD_SIZE%2 == 0

def create_board():
    ''' Returns an empty board, returns a list
    '''
    empty_list = ['']
    board = []
    for i in range(BOARD_SIZE):
        board.append(empty_list*BOARD_SIZE)
    return board

def initialize_board():
    ''' Initializes the board: takes the empty
    board and adds starting chips in the center
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
    '''Prints the column identificatory letters (A,B..) 
    in the upper side of the board
    '''
    print(' '*4,end='')  # Spaces printed for column letter fitting
    for i in range(len(initialize_board())):
        print(chr(i+65),end=' ')  # Adds 65 to match ascii uppercase code
    print()

def print_board(board):
    '''Prints the board, given by parameter (a list)
    '''
    print_column_letters()
    for index,row in enumerate(board):
        if index+1 < 10:                         # Validates if row number is 10 
            print(' '+str(index+1),end=' ')      # or more for space fitting
        else:
            print(index+1,end=' ')
        for column in row:
            if column == '':
                print('|'+' ',end='')
            else:
                print('|'+column,end='')
        print('|')

def ask_input(player_prompt):
    ''' Asks the user the position to enter a chip (column,row)
    and returns the chip location as a string
    '''
    chip_location = input(player_prompt+INPUT_PROMPT)
    return chip_location

def return_column(chip_location):
    ''' Given a string chip_location, returns
    the column location (string, a letter) in uppercase
    '''
    return chip_location[0].upper()

def return_row(chip_location):
    ''' Given a string chip_location, returns
    the row location (string, a number)
    '''
    return chip_location[2]

def enter_chip(board,player_prompt,player):
    ''' Enters a black chip in the board given a board (list)
    and returns the resulting board (list)
    '''
    chip_location = ask_input(player_prompt)
    column = return_column(chip_location)
    row = int(return_row(chip_location))
    column_ascii = ord(column)
    board[row - 1][column_ascii - 65] = player
    return board

def main():
    turn_count=1
    playing = True
    board = initialize_board()
    if check_boardsize():
        while playing:
            print_board(board)
            board = enter_chip(board,PROMPTS[0],PLAYER_CHIPS[0])
            print_board(board)
            board = enter_chip(board,PROMPTS[1],PLAYER_CHIPS[1])
            print_board(board)
            turn_count+=1
            if turn_count == 60:
                playing = False
    else:
        print('El tamaño del tablero debe ser par')
        return

main()