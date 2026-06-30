Tic-Tac-Toe

A simple two-player Tic-Tac-Toe game played on a 3 × 3 grid, built in Python for the command line. Two human players take turns marking the grid as X and O until one wins or the game ends in a draw.

📌 Features


Two-Player Gameplay (X vs O)
3 × 3 Grid Board Display
Turn-Based Input via Number Keys (1–9)
Win Detection (rows, columns & diagonals)
Draw Detection
Input Validation (rejects invalid or already-taken positions)
Play Again Option
Interactive Command Line Interface


🛠️ Technologies Used


Python 3
Tuples (for storing winning position combinations)


📂 Project Structure

tic_tac_toe/
│
├── tic_tac_toe.py   # Main game source code
├── README.md        # Project documentation

▶️ How to Run


Make sure Python 3 is installed.
Clone or download this repository.
Open a terminal in the project folder and run:


bashpython tic_tac_toe.py


Follow the on-screen prompts to play!


💬 How to Play


The board is numbered 1–9, matching the layout below:


 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9


Player X goes first, followed by Player O, alternating each turn.
On your turn, enter the number of the cell where you want to place your mark.
The first player to align three of their marks in a row, column, or diagonal wins.
If all 9 cells are filled with no winner, the game ends in a draw.
After the game ends, you'll be asked if you want to play again (Y/N).


💬 Example Round

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
Enter player X's choice (1-9): 5

 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
Enter player O's choice (1-9): 1
...
🎉 *** Player X won! *** 🎉

Do you want to play again? (Y/N): N

👋 Thanks for playing Tic-Tac-Toe!

⚙️ How It Works


The board is stored as a list called mesh, initialized with the strings "1"–"9" so empty cells display their position number.
display_board() prints the current state of the grid in a 3×3 format.
game(player) prompts the current player for a move, validates it, updates the board, and checks the win_positions tuple to see if that move resulted in a win.
The main loop alternates turns between X and O for up to 9 moves, checking for a win after each move and a draw if no winner is found after all cells are filled.
After each game, the player is asked whether they'd like to play again.


⚠️ Notes & Limitations


This is a two-player game only — there is no AI/computer opponent, despite the algorithm reference in the file's docstring (Minimax is mentioned as a common approach for AI opponents but is not implemented here).
Input validation relies on checking whether the chosen cell still holds its original number string, so re-entering an already-taken cell is correctly rejected.
The game runs entirely in the terminal with no graphical interface.