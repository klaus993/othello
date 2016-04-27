from time import sleep
from play import *
from board import *
from winner import *


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
