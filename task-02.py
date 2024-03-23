def print_board():
    row1 = " | {} | {} | {} | ".format(board[0], board[1], board[2])
    row2 = " | {} | {} | {} | ".format(board[3], board[4], board[5])
    row3 = " | {} | {} | {} | ".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon, name):
    print("Your turn, {} ({})".format(name, icon))
    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if 1 <= choice <= 9 and board[choice - 1] == " ":
                board[choice - 1] = icon
                break
            else:
                print("Invalid move. Please choose an empty cell (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def is_victory(icon):
    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],    # Rows
        [0,3,6],[1,4,7],[2,5,8],    # Columns
        [0,4,8],[2,4,6]             # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == icon for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def play_tic_tac_toe():
    player1_score = 0
    player2_score = 0

    while True:
        global board
        board = [" " for _ in range(9)]

        print("Welcome to Tic-Tac-Toe!")
        player1_name = input("Enter Player 1's name: ")
        player2_name = input("Enter Player 2's name: ")
        player1_icon = input("Choose {}'s icon (X/O): ".format(player1_name)).upper()
        player2_icon = 'X' if player1_icon.upper() == 'O' else 'O'

        print("{} will play with {} and {} will play with {}".format(player1_name, player1_icon, player2_name, player2_icon))

        while True:
            print_board()
            player_move(player1_icon, player1_name)
            if is_victory(player1_icon):
                print_board()
                print("{} wins! Congratulations!!".format(player1_name))
                player1_score += 1
                break
            elif is_draw():
                print("It's a draw.")
                break
            print_board()
            player_move(player2_icon, player2_name)
            if is_victory(player2_icon):
                print_board()
                print("{} wins! Congratulations!!".format(player2_name))
                player2_score += 1
                break
            elif is_draw():
                print("It's a draw.")
                break

        print("Scores:")
        print("{}: {}".format(player1_name, player1_score))
        print("{}: {}".format(player2_name, player2_score))

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
