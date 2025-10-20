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

window.mainloop()