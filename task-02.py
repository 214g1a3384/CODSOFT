import random

def print_board(board):
    row1 = " | {} | {} | {} | ".format(board[0], board[1], board[2])
    row2 = " | {} | {} | {} | ".format(board[3], board[4], board[5])
    row3 = " | {} | {} | {} | ".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(board, icon, name):
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

def is_victory(board, icon):
    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],    # Rows
        [0,3,6],[1,4,7],[2,5,8],    # Columns
        [0,4,8],[2,4,6]             # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == icon for i in combo):
            return True
    return False

def is_draw(board):
    return " " not in board

def available_moves(board):
    return [i for i in range(9) if board[i] == " "]

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def minimax(board, depth, is_maximizing):
    if is_victory(board, "X"):
        return -10 + depth
    elif is_victory(board, "O"):
        return 10 - depth
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    best_move = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_tic_tac_toe():
    while True:
        board = [" " for _ in range(9)]

        print("Welcome to Tic-Tac-Toe!")
        player_name = input("Enter your name: ")
        player_icon = input("Choose your icon (X/O): ").upper()
        ai_icon = 'X' if player_icon == 'O' else 'O'

        print("{} will play with {} and AI will play with {}".format(player_name, player_icon, ai_icon))

        while True:
            print_board(board)
            if player_icon == 'X':
                player_move(board, player_icon, player_name)
                if is_victory(board, player_icon):
                    print_board(board)
                    print("Congratulations, {} wins!".format(player_name))
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw.")
                    break
                move = best_move(board)
                board[move] = ai_icon
                if is_victory(board, ai_icon):
                    print_board(board)
                    print("AI wins!")
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw.")
                    break
            else:
                move = best_move(board)
                board[move] = ai_icon
                if is_victory(board, ai_icon):
                    print_board(board)
                    print("AI wins!")
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw.")
                    break
                print_board(board)
                player_move(board, player_icon, player_name)
                if is_victory(board, player_icon):
                    print_board(board)
                    print("Congratulations, {} wins!".format(player_name))
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw.")
                    break

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
