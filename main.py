# Tic-Tac-Toe Game
# Created by Aleksej Patkevič <opat74@gmail.com>

from functions import *


if __name__ == '__main__':

    my_field = {
        i: {letter: 'EMPTY_CELL' for letter in 'ABC'}
        for i in range(1, 4)
    }

    winner = 'No winner'
    player = 'X'
    turn = 1
    print()
    while turn <= 9:
        show_txt(my_field)
        print("Turn = ", turn, "Player =", player)
        turn_coord = read_turn(player, my_field)
        print()
        if turn_coord == 'QUIT_GAME':
            break
        my_field = make_turn(player, turn_coord, my_field)
        print(my_field)

        #if detect_win_row(my_field) == True or detect_win_column(my_field) == True or detect_win_diagonals(my_field) == True:
        if any([detect_win_row(my_field), detect_win_column(my_field), detect_win_diagonals(my_field)]):
            winner = player
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        turn+=1

    if turn_coord == 'QUIT_GAME':
        print('Game cancelled!')
    elif turn_coord != 'QUIT_GAME' and winner != 'No winner':
        print(f"Player {winner} wins!")
        show_txt(my_field)
        print('Game Over!')
    else:
        print('Game Over!')