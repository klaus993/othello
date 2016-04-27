from constants import *


def count_chips(board, player):
    """Given a board, counts the chips of a given player
    """
    cont = 0
    for row in board:
        for col in row:
            if col == PLAYER_CHIPS[player]:
                cont += 1
    return cont


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
