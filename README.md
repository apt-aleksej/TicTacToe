# Tic-Tac-Toe Console Game
# Created by Aleksej Patkevič <opat74@gmail.com>

A simple console-based implementation of the classic Tic-Tac-Toe game in Python. Two players take turns placing their symbols (`X` and `O`) on a 3×3 grid until one wins or the game ends in a draw.

---

## Features

- Two-player turn-based gameplay
- Input validation for grid coordinates
- Win detection for rows, columns, and diagonals
- Option to exit the game early
- Clean and readable output of the playing field

---

## Getting Started

### Requirements

- Python 3.6 or higher

### How to Run

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Run the script:

```bash
python tic_tac_toe.py
```

---

## How to Play

- The grid is labeled with coordinates like `1a`, `2b`, `3c`, etc.
- Players take turns entering a coordinate to place their symbol.
- Valid inputs include: `1a`, `1b`, `1c`, `2a`, `2b`, `2c`, `3a`, `3b`, `3c`
- To exit the game early, type `exit`.

---

## Game Logic

- The board is represented as a dictionary with keys like `'1a'`, `'2b'`, etc.
- The `show()` function displays the current state of the board.
- The `decide_win()` function checks for three identical symbols in a row, column, or diagonal.

---

## Code Style

This project follows [PEP 8](https://peps.python.org/pep-0008/) guidelines:
- Consistent indentation and spacing
- Descriptive function names
- Proper use of docstrings
- Avoids redundant code and unnecessary comparisons

---

## File Structure

```
tic_tac_toe.py       # Main game script
README.md            # Project documentation
```

---

## License

This project is open-source and free to use under the MIT License.

---

## AI Assistance

This project was developed with support from Microsoft Copilot, an AI companion that helped refine code structure, ensure PEP 8 compliance, and generate documentation

---

## Acknowledgments

Thanks to Python for making game development fun and accessible!