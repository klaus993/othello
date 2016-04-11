# BOARD_SIZE must be between [4, 26] and even
BOARD_SIZE = 8
WHITE_PLAYER = 'B'
BLACK_PLAYER = 'N'

def check_boardsize(BOARD_SIZE):
    ''' Checks if the board size is even or odd
    '''
    if BOARD_SIZE%2 != 0:
        return 'Board size must be even'

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
    board[center_index_2][center_index_2] = WHITE_PLAYER
    board[center_index_2][center_index_1] = BLACK_PLAYER
    board[center_index_1][center_index_2] = BLACK_PLAYER
    board[center_index_1][center_index_1] = WHITE_PLAYER
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

def ask_input_white():
    ''' Asks the user the position to enter a chip (column,row)
    and returns the chip location as a string
    '''
    chip_location = input('Color blanco: ingrese una ficha (columna,fila): ')
    return chip_location

def ask_input_black():
    ''' Asks the user the position to enter a chip (column,row)
    and returns the chip location as a string
    '''
    chip_location = input('Color negro: ingrese una ficha (columna,fila): ')
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

def enter_black_chip(board):
    ''' Enters a black chip in the board given a board (list)
    and returns the resulting board (list)
    '''
    chip_location = ask_input_black()
    column = return_column(chip_location)
    row = int(return_row(chip_location))
    board[row - 1][ord(column) - 65] = BLACK_PLAYER
    return board

def enter_white_chip(board):
    ''' Enters a white chip in the board given a board (list)
    and returns the resulting board (list)
    '''
    chip_location = ask_input_white()
    column = return_column(chip_location)
    row = int(return_row(chip_location))
    column_ascii=ord(column)
    board[row - 1][ord(column) - 65] = WHITE_PLAYER
    return board

def capture_chip():
    pass

def main():
    turn_count=1
    playing = True
    board = initialize_board()
    while playing:
        print_board(board)
        board = enter_white_chip(board)
        print_board(board)
        board = enter_black_chip(board)
        print_board(board)
        turn_count+=1
        if turn_count == 60:
            playing = False

main()