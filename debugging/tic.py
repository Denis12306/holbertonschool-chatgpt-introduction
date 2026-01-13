#!/usr/bin/python3
def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 11)   # Adjusted for 3 columns, Plateau mal formaté dans version donné (*5)

def check_winner(board):
    """Return the winning player ('X' or 'O') if there is one, else None."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """Check if the board is full (draw)."""            # Pas de détection d’égalité, vérifier si le plateau est plein
    return all(cell != " " for row in board for cell in row)

def get_valid_input(player):
    """
    Prompt the player for a valid row and column.
    Repeat until the input is valid.
    """
    while True:
        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))        # utiliser try/except + vérifier que la valeur est entre 0 et 2.

            # Check if input is within bounds
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Coordinates must be 0, 1, or 2. Try again.")
                continue

            return row, col
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

def tic_tac_toe():
    """Play a secure Tic-Tac-Toe game with full input validation."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        while True:
            row, col = get_valid_input(player)

            # Check if the cell is empty
            if board[row][col] == " ":       # refaire demander l’entrée tant que la case n’est pas vide.
                break
            else:
                print("That spot is already taken! Try again.")

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"      # Error on the first code 

if __name__ == "__main__":
    tic_tac_toe()
