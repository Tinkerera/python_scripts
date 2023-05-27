import random

# The TicTacToe board
board = [' '] * 9

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]

# Function to draw the TicTacToe board
def draw_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if a player has won
def check_winner(board, player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function for the AI player to make a move
def make_ai_move(board):
    best_score = float('-inf')
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Function to evaluate the score of a board configuration
def evaluate(board):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    else:
        return 0

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score != 0:
        return score

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function for the human player to make a move
def make_human_move(board):
    while True:
        move = int(input("Enter your move (0-8): "))
        if 1 <= move <= 9 and board[move-1] == ' ':
            move -=1
            board[move] = 'X'
            break
        else:
            print("Invalid move. Try again.")

# Main game loop
def play_game():
    print("Welcome to TicTacToe!")

    while True:
        board = [' '] * 9
        draw_board(board)

        while not is_board_full(board):
            make_human_move(board)
            draw_board(board)

            if check_winner(board, 'X'):
                print("Congratulations! You won!")
                break

            if is_board_full(board):
                print("It's a draw!")
                break

            print("AI is making its move...")
            make_ai_move(board)
            draw_board(board)

            if check_winner(board, 'O'):
                print("Sorry, you lost!")
                break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

play_game()
