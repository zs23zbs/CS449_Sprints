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

"""Creating the mode widget"""
game_modes = ["Simple Game", "General Game"] # List of options for user to pick for game mode / creating a radio button
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#20B2AA")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="#E0FFFF")

def pick_mode(): # Fuction for selecting whichever game mode for the radio button
    mode_label.config(text=f"MODE:")
variable1 = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes): # Iterate through the game_modes list to display the different game versions the user may want to play in 
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable1,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0,padx=4, pady=4)

mode_label.grid(row=0, column=0)
mode_frame.grid(row=0, column=0)

window.mainloop()