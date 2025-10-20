from game_logic import GameLogic # Import GameLogic (backend)
import tkinter as tk 

"""Initiate and create window with title"""
window = tk.Tk()
window.title("SOS TicTacToe")

"""Variables for Game"""
game = None
board_buttons = []
board_size = tk.IntVar(value=3)
mode = tk.StringVar(value="Simple Game")

"""Board Size widget""" 
boardSize_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#008B8B") 
boardSize_label = tk.Label(master=boardSize_frame, text="Game Board Size: 5x6", fg="black", bg="#E0FFFF")

# Format the board size widget 
boardSize_label.grid(row=0, column=6, padx=5, pady=5)
boardSize_frame.grid(row=0, column=6, padx=5, pady=5)

window.mainloop()