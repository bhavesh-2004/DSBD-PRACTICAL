 # Initialize an empty board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print("| {} | {} | {} |".format(board[i], board[i+1], board[i+2]))
    print()

# Function to handle the player's move
def player_move(icon):
    while True:
        try:
            choice = int(input(f"Player {icon}'s turn. Enter your move (1-9): ")) - 1
            if board[choice] == " ":
                board[choice] = icon
                break
            else:
                print("That space is already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to check for a win
def is_victory(icon):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == icon for a, b, c in win_conditions)

# Function to check for a draw
def is_draw():
    return " " not in board

# Main game loop
while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print_board()
        print("Player X wins! Congratulations!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break

    print_board()
    player_move("O")
    if is_victory("O"):
        print_board()
        print("Player O wins! Congratulations!")
        break
    elif is_draw():
        print_board()
        print("It's a draw!")
        break


 