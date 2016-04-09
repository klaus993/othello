# from string import ascii_uppercase


BOARD_SIZE = 8
WHITE_PLAYER = '0'
BLACK_PLAYER = 'O'

def check_boardsize(BOARD_SIZE):
    ''' Checks if the board size is even or odd
    '''
    if BOARD_SIZE%2 != 0:
        return 'Board size must be even'

def create_board():
    ''' Returns an empty board, returns a list
    '''
    emptylist = ['']
    board = []
    for i in range(BOARD_SIZE):
        board.append(emptylist*BOARD_SIZE)
    return board

def initialize_board():
    ''' Initializes the board: takes the empty
    board and adds starting chips in the center
    '''
    board = create_board()
    centerindex2 = BOARD_SIZE//2
    centerindex1 = centerindex2 - 1
    board[centerindex1][centerindex1] = WHITE_PLAYER
    board[centerindex1][centerindex2] = BLACK_PLAYER
    board[centerindex2][centerindex1] = BLACK_PLAYER
    board[centerindex2][centerindex2] = WHITE_PLAYER
    return board


def print_column_letters():
    '''Prints the column identificatory letters (A,B..) 
    in the upper side of the board
    '''
    print(' '*4,end='')  # Spaces printed for column letter fitting
    for i in range(len(initialize_board())):
        print(chr(i+65),end=' ')  # Adds 65 to match ascii uppercase code
    print()
    # for letter in ascii_uppercase[:BOARD_SIZE]:
    #     print(letter,end=' ')
    # print()

def print_board(board):
    '''Prints the board, given by parameter (a list)
    '''
    # print(' '*4,end='')                        
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

# print_board(initialize_board())

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
    ''' Returns the column location
    '''
    return chip_location[0]

def return_row(chip_location):
    ''' Returns the row location
    '''
    return chip_location[2]

def enter_black_chip(board):
    ''' Enters a chip in the board given a board (list)
    and a player ('B' or 'N') and returns the resulting board (list)
    '''
    chip_location = ask_input_black()             #B,2
    column = return_column(chip_location)   #B
    row = int(return_row(chip_location))         #2
    board[row - 1][ord(column) - 65]=BLACK_PLAYER
    return board

def enter_white_chip(board):
    ''' Enters a chip in the board given a board (list)
    and a player ('B' or 'N') and returns the resulting board (list)
    '''
    chip_location = ask_input_white()             #B,2
    column = return_column(chip_location)   #B
    row = int(return_row(chip_location))         #2
    board[row - 1][ord(column) - 65]=WHITE_PLAYER
    return board

def capture_chip():
    pass

def main():
    turn_number=1
    playing = True
    board = initialize_board()
    while playing:
        print_board(board)
        board = enter_white_chip(board)
        print_board(board)
        board = enter_black_chip(board)
        print_board(board)
        turn_number+=1
        if turn_number == 60:
            playing = False

main()

# print_board(enter_chip(initialize_board(),'B'))