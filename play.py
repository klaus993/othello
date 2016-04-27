from time import sleep
from board import *
from moves import *


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
                    break      # Breaks and the game ends
                sleep(1)
                print('Color ' + PLAYER_COLORS[i] + ': no tienes jugadas posibles')
        turn_count += 1
        if turn_count == MAX_TURNS:
            playing = False
    return board
