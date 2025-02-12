
```markdown
# Tic-Tac-Toe Game with Tkinter

This is a simple Tic-Tac-Toe game built using Python's `Tkinter` library. The game allows users to play against the computer with three different difficulty levels: **Easy**, **Medium**, and **Hard**. The game board is displayed using a GUI, and the player can click on the grid to make moves.

## Features
- **Easy Mode**: The computer makes random moves.
- **Medium Mode**: The computer tries to block the player’s winning moves but still has some randomness in its moves.
- **Hard Mode**: The computer uses an optimal algorithm (like Minimax) to always make the best possible move and can defeat the player.
- GUI with Tkinter for a user-friendly interface.

## Requirements

Before running the game, make sure you have Python 3.x and Tkinter installed.

To install Tkinter (if not already installed), you can use the following:

```bash
# For Ubuntu/Debian-based systems:
sudo apt-get install python3-tk

# For macOS:
brew install python-tk

# For Windows, Tkinter comes bundled with Python.
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

2. If you are using a virtual environment, activate it, and install any dependencies (if applicable).

```bash
# Example for virtualenv
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Run the Tic-Tac-Toe game:

```bash
python tic_tac_toe.py
```

## How to Play

1. When the game starts, you will be prompted to choose a difficulty level (Easy, Medium, or Hard).
2. Click on any cell in the 3x3 grid to make your move (you will be **X**).
3. The computer will take its turn immediately after you make your move.
4. The game will continue until either you win, the computer wins, or it's a draw.

## Game Modes

- **Easy Mode**: In this mode, the computer picks a random move and doesn't strategize, making it easier for the player to win.
- **Medium Mode**: The computer tries to block your winning moves but is not perfect, so there are still chances to win.
- **Hard Mode**: The computer plays optimally using an algorithm to minimize your chances of winning. It is nearly unbeatable.

## Example Screenshots

### Game 
![Easy Mode Screenshot](![image](https://github.com/user-attachments/assets/646bf34d-7450-47c9-8b43-b0538c9478d0))

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Please make sure to follow the code style and include tests where applicable.

1. Fork the repository
2. Create a new branch for your feature/bug fix
3. Make your changes
4. Commit your changes and push to your fork
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy playing Tic-Tac-Toe! 🕹️
```

### Instructions:

- **Easy Mode**: The computer makes random moves and doesn’t strategize.
- **Medium Mode**: The computer tries to block you from winning but is still imperfect.
- **Hard Mode**: The computer plays optimally using an algorithm like Minimax to minimize your chances of winning.

You can use this exact content for your `README.md` file.

Let me know if you need further modifications or assistance!
