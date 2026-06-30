'''
Tic-Tac-Toe is a simple two-player AI game played on a 3 × 3 grid.
most popular algorithm used for Tic-Tac-Toe AI game is Minimax Algorithm
There are two players:
Player 1 uses X
Player 2 uses O
'''
# Tuple to store winning positions.
win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def display_board():
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))

def game(player):
    display_board()

    while True:
        try:
            ch = int(input(f"Enter player {player}'s choice (1-9): "))

            if ch < 1 or ch > 9 or str(ch) not in mesh:
                raise ValueError

            mesh[ch - 1] = player
            break

        except ValueError:
            print("Invalid position number. Try again.")

    for wp in win_positions:
        if all(mesh[pos] == player for pos in wp):
            return wp
    return None


# Main game loop
while True:

    player1 = "X"
    player2 = "O"
    player = player1
    mesh = list("123456789")

    winner = False

    for i in range(9):
        won = game(player)

        if won:
            display_board()
            print(f"\n🎉 *** Player {player} won! *** 🎉")
            winner = True
            break

        player = player1 if player == player2 else player2

    if not winner:
        display_board()
        print("\n🤝 Game ends in a draw! 🤝")

    # Ask user to play again
    choice = input("\nDo you want to play again? (Y/N): ").upper()

    if choice != "Y":
        print("\n👋 Thanks for playing Tic-Tac-Toe!")
        break