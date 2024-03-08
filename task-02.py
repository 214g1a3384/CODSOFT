#TASK-02
import math
import random

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    # Function to check if a player has won by checking rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # Function to check if the board is full, indicating a tie
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def evaluate(board):
    # Function to evaluate the current state of the board (win, lose, or tie)
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player):
    # Minimax algorithm with Alpha-Beta Pruning for optimal move calculation
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    # Function to find the best move for the AI player (X) using the minimax algorithm
    best_val = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    # Main function to initiate and control the Tic-Tac-Toe game
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            # AI (X) makes a move
            row, col = find_best_move(board)
            print("AI (X) plays at ({}, {})".format(row, col))
        else:
            # Human player (O) makes a move
            while True:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print("{} wins!".format(current_player))
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if _name_ == "_main_":
    play_tic_tac_toe()