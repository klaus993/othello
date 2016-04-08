from string import ascii_uppercase

BOARDSIZE=10

def initialize_board():
    ''' Initializes the board, as an empty board.
    Returns the board (list)
    '''
    emptylist=['']
    board=[]
    for i in range(BOARDSIZE):
        board.append(emptylist*BOARDSIZE)
    return board

def print_column_letters():
    '''Prints the column identificatory letters (A,B..) 
    in the upper side of the board
    '''
    RANGE='1234567890'
    for letter in RANGE[:BOARDSIZE]:   #THIS COMMIT IS FOR TESTS 2
        print(letter,end=' ')
    print()

def print_board(board):
    '''Prints the board, given by parameter (a list)
    '''
    print(' '*4,end='')                         # Spaces printed for column letter fitting
    print_column_letters()
    for index,row in enumerate(board):
        if index+1<10:                         # Validates if row number is 10 
            print(' '+str(index+1),end=' ')    # or more for space fitting
        else:
            print(index+1,end=' ')
        for column in row:
            if column=='':
                print('|'+' ',end='')
            else:
                print('|'+column,end='')
        print('|')

print_board(initialize_board())
