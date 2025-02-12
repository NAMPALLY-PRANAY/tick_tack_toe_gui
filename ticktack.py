import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="#282c34")

player = "X"
ai_player = "O"
difficulty = "Easy"
board = [" " for _ in range(9)]
buttons = []
winning_line = None

def reset_game():
    global board, player, winning_line
    board = [" " for _ in range(9)]
    player = "X"
    if winning_line:
        canvas.delete(winning_line)
        winning_line = None
    update_buttons()

def update_buttons():
    for i, btn in enumerate(buttons):
        btn.config(text=board[i], state="normal" if board[i] == " " else "disabled")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            draw_winning_line(condition)
            return True
    return False

def draw_winning_line(condition):
    global winning_line
    positions = [(50, 50), (150, 50), (250, 50),
                 (50, 150), (150, 150), (250, 150),
                 (50, 250), (150, 250), (250, 250)]
    start = positions[condition[0]]
    end = positions[condition[2]]
    winning_line = canvas.create_line(start, end, fill="red", width=4)
    canvas.tag_raise(winning_line)  # Ensure the line is on top of buttons

def is_full(board):
    return " " not in board

def ai_move():
    if difficulty == "Easy":
        easy_ai()
    elif difficulty == "Medium":
        medium_ai()
    else:
        hard_ai()
    update_buttons()
    if check_winner(board, ai_player):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        reset_game()
    elif is_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_game()

def easy_ai():
    available_moves = [i for i in range(9) if board[i] == " "]
    if available_moves:
        move = random.choice(available_moves)
        board[move] = ai_player

def medium_ai():
    for i in range(9):
        if board[i] == " ":
            board[i] = ai_player
            if check_winner(board, ai_player):
                return
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board, player):
                board[i] = ai_player
                return
            board[i] = " "

    easy_ai()

def hard_ai():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = ai_player
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = ai_player

def minimax(board, depth, is_maximizing):
    if check_winner(board, ai_player):
        return 1
    elif check_winner(board, player):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = ai_player
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def player_move(index):
    global player
    if board[index] == " ":
        board[index] = player
        update_buttons()
        if check_winner(board, player):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            reset_game()
        elif is_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            ai_move()

def set_difficulty(level):
    global difficulty
    difficulty = level
    reset_game()

canvas = tk.Canvas(root, width=300, height=300, bg="#282c34", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

for i in range(9):
    btn = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                    bg="#61afef", fg="#282c34", activebackground="#98c379",
                    command=lambda i=i: player_move(i))
    btn_window = canvas.create_window((50 + (i % 3) * 100, 50 + (i // 3) * 100), window=btn, anchor="center")
    buttons.append(btn)

difficulty_frame = tk.Frame(root, bg="#282c34")
difficulty_frame.grid(row=1, column=0, columnspan=3, pady=10)

tk.Button(difficulty_frame, text="Easy", font=("Helvetica", 12),
          command=lambda: set_difficulty("Easy"), bg="#98c379", fg="#282c34").pack(side=tk.LEFT, padx=10)
tk.Button(difficulty_frame, text="Medium", font=("Helvetica", 12),
          command=lambda: set_difficulty("Medium"), bg="#e5c07b", fg="#282c34").pack(side=tk.LEFT, padx=10)
tk.Button(difficulty_frame, text="Hard", font=("Helvetica", 12),
          command=lambda: set_difficulty("Hard"), bg="#e06c75", fg="#282c34").pack(side=tk.LEFT, padx=10)

root.mainloop()
