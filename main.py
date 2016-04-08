from string import ascii_uppercase

BOARDSIZE=8

def initialize_board():
    ''' Initializes the board, as an empty board.
    Returns the board (list)
    '''
    board=[]
    for i in range(BOARDSIZE):
        board.append([])
        for x in range(BOARDSIZE):
            board[i].append('')
    return board

def print_column_letters():
    '''Prints the column identificatory letters (A,B..) 
    in the upper side of the board
    '''
    for letter in ascii_uppercase[:BOARDSIZE]:
        print(letter,end=' ')
    print()

def print_board(board):
    '''Prints the board, given by parameter (a list)
    '''
    print(' '*4,end='')
    print_column_letters()
    rowcount=1
    for row in board:
        if rowcount<10:
            print(' '+str(rowcount),end=' ')
        else:
            print(rowcount,end=' ')
        for column in row:
            if column=='':
                print('|'+' ',end='')
            else:
                print('|'+column,end='')
        print('|')
        rowcount+=1

print_board(initialize_board())