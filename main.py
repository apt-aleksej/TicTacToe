# Tic-Tac-Toe Console Game
# Created by Aleksej Patkevič <opat74@gmail.com>

def show(ground):
    """Shows the current state of the playing field."""
    print('_____A___B___C___')
    print('1 |', ground['1a'], ground['1b'], ground['1c'], '|')
    print('2 |', ground['2a'], ground['2b'], ground['2c'], '|')
    print('3 |', ground['3a'], ground['3b'], ground['3c'], '|')
    print('_________________')

def decide_win(ground):
    """Checks the playing field for lines of three identical symbols."""
    win = False

    # finding in rows
    for row in ('1', '2', '3'):
        if ground[row + 'a'] == ground[row + 'b'] == ground[row + 'c'] and ground[row + 'a'] != ' . ':
            win = True
            break

    # finding in columns
    for col in ('a', 'b', 'c'):
        if ground['1' + col] == ground['2' + col] == ground['3' + col] and ground['1' + col] != ' . ':
            win = True
            break

    # finding in diagonal 1
    if ground['1a'] == ground['2b'] == ground['3c'] and ground['1a'] != ' . ':
        win = True

    # finding in diagonal 2
    if ground['3a'] == ground['2b'] == ground['1c'] and ground['3a'] != ' . ':
        win = True

    return win


if __name__ == '__main__':

    my_field = {
        '1a':' . ', '1b':' . ', '1c':' . ',
        '2a':' . ', '2b':' . ', '2c':' . ',
        '3a':' . ', '3b':' . ', '3c':' . '
    }
    
    valid_inputs = {"1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"}

    print("Let's start!")
    print()

    turn = 1
    player = ' X '

    while turn <= 9:
        show(my_field)
        print()
        print("Turn = ", turn, "Player =", player)

        while True:
            user_input = input(f"Player {player}, please input coordinate (a1–c3): ").strip().lower()
            if user_input in valid_inputs and my_field[user_input] == ' . ':
                print(f"Ok: {player} to {user_input}")
                my_field[user_input] = player
                break
            elif user_input == 'exit':
                break
            else:
                print("Wrong input! Try again")

        if user_input == 'exit':
            print("Game cancelled.")
            break

        if decide_win(my_field) == True:
            print()
            print(f"Player {player} wins!")
            show(my_field)
            print()
            break

        if player == ' X ':
            player = ' O '
        else:
            player = ' X '

        turn += 1

    print("Game Over!")