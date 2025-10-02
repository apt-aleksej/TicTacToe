# Functions for Tic-Tac-Toe Game
# Created by Aleksej Patkevič <opat74@gmail.com>

import string


def show_txt(external_ground):
    """Shows the current state of the playing field."""
    import copy
    ground = copy.deepcopy(external_ground)
    # Change 'EMPTY_CELL' to ' ' for printing
    for key1 in [1, 2, 3]:
        for key2 in ['A', 'B', 'C']:
            if ground[key1][key2] == 'EMPTY_CELL':
                ground[key1][key2] = ' '

    print(f" ____A___B___C__ \n", \
    f"1 | {ground[1]['A']} | {ground[1]['B']} | {ground[1]['C']} | \n", \
    f"2 | {ground[2]['A']} | {ground[2]['B']} | {ground[2]['C']} | \n", \
    f"3 | {ground[3]['A']} | {ground[3]['B']} | {ground[3]['C']} | \n", \
    f"__|___________|")

def valid_coord():
    """Generate a list of valid coordinates for a turn."""
    result = []
    for row_num in range(1, 4):
        for column_num in range(0, 3):
            result.append(str(row_num) + string.ascii_uppercase[column_num])
    return result

def read_turn(player, ground):
    """Read a turn coordinates from the keyboard and check if it is correct."""
    while True:
        user_input = input(f"Player {player}, please input coordinate (1A–3C): ").strip().upper()
        if user_input[0] in ('1', '2', '3')\
                and user_input[1] in ('A', 'B', 'C')\
                and ground[int(user_input[0])][user_input[1]] == 'EMPTY_CELL':
            print(f"Ok: {player} to {user_input}")
            break
        elif user_input in ['EXIT', 'QUIT', 'exit', 'quit', 'Q', 'q']:
            user_input = 'QUIT_GAME'
            break
        else:
            print("Wrong input! Try again")
    return user_input

def make_turn(player, coord, ground):
    """Insert the players name to the turn coordinates"""
    ground[int(list(coord)[0])][list(coord)[1]] = player
    return ground

def detect_win_row(ground):
    """Checks the playing rows for lines of three identical symbols."""
    win = False
    for row in (1, 2, 3):
        if ground[row]['A'] == ground[row]['B'] == ground[row]['C'] and ground[row]['A'] != 'EMPTY_CELL':
            win = True
            break
    return win

def detect_win_column(ground):
    """Checks the playing column for lines of three identical symbols."""
    win = False
    for column in ('A', 'B', 'C'):
        if ground[1][column] == ground[2][column] == ground[3][column] and ground[1][column] != 'EMPTY_CELL':
            win = True
            break
    return win


def detect_win_diagonals(ground):
    """Checks the playing diagonals for lines of three identical symbols."""
    win = False
    # finding in diagonal 1
    if ground[1]['A'] == ground[2]['B'] == ground[3]['C'] and ground[1]['A'] != 'EMPTY_CELL':
        win = True
    # finding in diagonal 2
    if ground[3]['A'] == ground[2]['B'] == ground[1]['C'] and ground[3]['A'] != 'EMPTY_CELL':
        win = True
    return win